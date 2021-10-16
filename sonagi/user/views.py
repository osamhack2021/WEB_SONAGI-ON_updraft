from django.contrib.auth import get_user_model
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.conf import settings
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserDisplaySerializer
import requests
from rest_framework import status
from json.decoder import JSONDecodeError
from django.http import JsonResponse
from allauth.socialaccount.models import SocialAccount
from sonagi.utils import initialize_usersetting
import rest_framework

# Create your views here.

User = get_user_model()
BASE_URL = getattr(settings, "BASE_URL")
GOOGLE_CALLBACK_URI = BASE_URL + 'api/user/social-login/google/callback'

class UserShowView(APIView):
    def get(self, request):
        serializer = UserDisplaySerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

def google_login_redirect(request):
    """
    Code Request
    """
    scope = "https://www.googleapis.com/auth/userinfo.email"
    client_id = getattr(settings, "SOCIAL_AUTH_GOOGLE_CLIENT_ID")
    return redirect(f"https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}&response_type=code&redirect_uri={GOOGLE_CALLBACK_URI}&scope={scope}")

def UserGoogleLoginView(request):
    client_id = getattr(settings, "SOCIAL_AUTH_GOOGLE_CLIENT_ID")
    client_secret = getattr(settings, "SOCIAL_AUTH_GOOGLE_SECRET")
    state = getattr(settings, 'STATE')
    code = request.GET.get('code')
    """
    Access Token Request
    """
    token_req = requests.post(
        f"https://oauth2.googleapis.com/token?client_id={client_id}&client_secret={client_secret}&code={code}&grant_type=authorization_code&redirect_uri={GOOGLE_CALLBACK_URI}&state={state}")
    token_req_json = token_req.json()

    #error = token_req_json.get("error")
    #if error is not None:
    #    raise JSONDecodeError(error)

    access_token = token_req_json.get('access_token')

    """
    Email Request
    """
    email_req = requests.get(
        f"https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={access_token}")
    email_req_status = email_req.status_code
    if email_req_status != 200:
        return JsonResponse({'detail': '이메일 정보를 가져올 수 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    email_req_json = email_req.json()
    email = email_req_json.get('email')

    """
    Signup or Signin Request
    """
    try:
        user = User.objects.get(email=email)
        # 기존에 가입된 유저의 Provider가 google이 아니면 에러 발생, 맞으면 로그인
        # 다른 SNS로 가입된 유저
        social_user = SocialAccount.objects.get(user=user)
        if social_user is None:
            return JsonResponse({'detail': '소셜 계정으로 가입된 유저가 아닙니다.'}, status=status.HTTP_400_BAD_REQUEST)
        if social_user.provider != 'google':
            return JsonResponse({'detail': '구글 계정으로 가입된 유저가 아닙니다.'}, status=status.HTTP_400_BAD_REQUEST)
        # 기존에 Google로 가입된 유저
        data = {'access_token': access_token, 'code': code}
        accept = requests.post(
            f"{BASE_URL}api/user/social-login/google/login_finish", data=data)
        accept_status = accept.status_code
        if accept_status != 200:
            return JsonResponse({'detail': '로그인에 실패했습니다. 잠시 후 다시 시도해주세요.'}, status=accept_status)
        accept_json = accept.json()
        accept_json.pop('user', None)
        return JsonResponse(accept_json)
    except User.DoesNotExist:
        # 기존에 가입된 유저가 없으면 새로 가입
        data = {'access_token': access_token, 'code': code}
        accept = requests.post(
            f"{BASE_URL}api/user/social-login/google/login_finish", data=data)
        accept_status = accept.status_code
        if accept_status != 200:
            return JsonResponse({'detail': '구글 계정을 통한 회원가입에 실패했습니다. 잠시 후 다시 시도해주세요.'}, status=accept_status)

        # initializer(create) usersetting for new user
        initialize_usersetting(email)

        accept_json = accept.json()
        accept_json.pop('user', None)
        return JsonResponse(accept_json)

class UserGoogleCallbackView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = GOOGLE_CALLBACK_URI
    client_class = OAuth2Client