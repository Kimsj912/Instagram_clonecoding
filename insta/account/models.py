from django.db import models
from django.contrib.auth.models import ( BaseUserManager, AbstractBaseUser,PermissionsMixin)

class MyUserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        if not email:
            raise ValueError('Users must have an email address') #raise는 예외 지정한거 발생시키는 것.
        user = self.model(
            email=MyUserManager.normalize_email(email),
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, nickname, password):
        u = self.create_user(email=email, name=name, nickname=nickname, password=password, )
        u.is_admin = True
        u.save(using=self._db)
        return u

class MyUser(AbstractBaseUser,  PermissionsMixin):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        u'닉네임', 
        max_length=30, 
        blank=False, 
        default='')
    name = models.CharField(
        u'이름', 
        max_length=10, 
        blank=False, 
        default='')

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # def get_full_name(self):
    #     # The user is identified by their email address
    #     return self.email

    # def get_short_name(self):
    #     # The user is identified by their email address
    #     return self.email

    # def __str__(self):
    #     return self.email

    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin

# class userInfo(models.Model):
#     email = models.EmailField(max_length=254)
#     phoneNum = models.CharField(max_length=50)
#     name=models.CharField(max_length=40)
#     username=models.CharField(max_length=40)
#     password = models.CharField(max_length=50)

#     def get_absolute_url(self): # redirect시 활용
#         return reverse('profile:profile_detail', args=[self.id])