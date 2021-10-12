import names
import datetime
from django.contrib.auth import get_user_model
from usersetting.models import UserSetting

# util functions for project

User = get_user_model()

def initialize_usersetting(email):
    while(True):
        try:
            nickname = names.get_first_name()
            UserSetting.objects.get(nickname=nickname)
        except:
            break
    enlisted_date = datetime.datetime.now().strftime("%Y-%m-%d")
    delisted_date = (datetime.datetime.now() + datetime.timedelta(days=548)).strftime("%Y-%m-%d")
    promotion1_date = (datetime.datetime.now() + datetime.timedelta(days=60)).strftime("%Y-%m-%d")
    promotion2_date = (datetime.datetime.now() + datetime.timedelta(days=240)).strftime("%Y-%m-%d")
    promotion3_date = (datetime.datetime.now() + datetime.timedelta(days=400)).strftime("%Y-%m-%d")
    UserSetting.objects.create(email=User.objects.get(email=email),
                               nickname=nickname,
                               major='army',
                               type='soldier',
                               enlisted_date=enlisted_date,
                               delisted_date=delisted_date,
                               promotion1_date=promotion1_date,
                               promotion2_date=promotion2_date,
                               promotion3_date=promotion3_date)