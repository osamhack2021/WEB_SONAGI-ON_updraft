from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):    
    use_in_migrations = True

    def create_user(self, username, email, nickname, password=None):        
        if not email :            
            raise ValueError('must have user email')        
        user = self.model(            
            username = username,
            email = self.normalize_email(email),            
            nickname = nickname,      
        )        
        user.set_password(password)        
        user.save(using=self._db)        
        return user

    def create_superuser(self, username, email, nickname, password):        
        user = self.create_user(     
            username = username,       
            email = self.normalize_email(email),            
            nickname = nickname,                
        )
        user.set_password(password)             
        user.is_superuser = True        
        user.is_staff = True 
        user.save(using=self._db)
        return user 

class CustomUser(AbstractBaseUser,PermissionsMixin):    
    objects = UserManager()
    
    username = models.CharField(
        max_length=17,
        null=False,
        unique=True,
        verbose_name="아이디",
    )
    email = models.EmailField(        
        max_length=255, 
        null=False,       
        unique=True,
        verbose_name="이메일",    
    )    
    nickname = models.CharField( # 군 구분
        max_length=10,
        null=False,
        unique=True,
        verbose_name="닉네임",
    )   
    is_active = models.BooleanField(default=True)      
    is_superuser = models.BooleanField(default=False)    
    is_staff = models.BooleanField(default=False)     
    date_joined = models.DateTimeField(auto_now_add=True)     
    USERNAME_FIELD = 'username'    
    REQUIRED_FIELDS = ['email', 'nickname']

    def __str__(self):
        return self.username