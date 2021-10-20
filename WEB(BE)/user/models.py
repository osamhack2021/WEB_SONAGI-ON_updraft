from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):    
    use_in_migrations = True

    def create_user(self, email, password=None):        
        if not email :            
            raise ValueError('must have user email')        
        user = self.model(            
            email = self.normalize_email(email),                
        )        
        user.set_password(password)        
        user.save(using=self._db)        
        return user

    def create_superuser(self, email, password):        
        user = self.create_user(           
            email = self.normalize_email(email),                         
        )
        user.set_password(password)             
        user.is_superuser = True        
        user.is_staff = True 
        user.save(using=self._db)
        return user 

class User(AbstractBaseUser,PermissionsMixin):    
    objects = UserManager()
    
    email = models.EmailField(        
        max_length=255, 
        null=False,       
        unique=True,
        verbose_name="이메일",    
    )     
    is_active = models.BooleanField(default=True)      
    is_superuser = models.BooleanField(default=False)    
    is_staff = models.BooleanField(default=False)     
    date_joined = models.DateTimeField(auto_now_add=True)     
    USERNAME_FIELD = 'email'    

    def __str__(self):
        return self.email