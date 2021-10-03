from allauth.socialaccount.providers.oauth2.views import OAuth2Adapter
import requests
from allauth.socialaccount.providers.google.provider import GoogleProvider

class GoogleOAuth2RestAdapter(OAuth2Adapter):
    provider_id = GoogleProvider.id
    token_url = 'https://www.googleapis.com/oauth2/v1/tokeninfo'

    def complete_login(self, request, app, token, **kwargs):
        resp = requests.get(self.token_url,
                            params={'id_token': token.token,
                                    'alt': 'json'})
        resp.raise_for_status()
        extra_data = resp.json()
        login = self.get_provider() \
            .sociallogin_from_response(request,
                                       extra_data)
        return login