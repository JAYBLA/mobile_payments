import uuid
from uuid import uuid4
from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

from .manager import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='Email Address',
        max_length=150,
        unique=True,
    )
    username = models.CharField(
        verbose_name='Username',
        max_length=100,
        unique=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_tutor = models.BooleanField(default=False)

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_superuser


def profile_pic_filename(instance, filename):
    ext = filename.split('.')[1]
    new_filename = f'{uuid4()}.{ext}'
    return f'profile_pics/{new_filename}'


class Profile(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
 
    profile_picture = models.ImageField(upload_to=profile_pic_filename, default='default.png')
    website = models.URLField(blank=True, max_length=200)
    country = CountryField(default='TZ', verbose_name='Country')
    location = models.CharField(max_length=200)
    bio = models.TextField(blank=True)

    #Social media links
    youtube_link = models.URLField(verbose_name='Youtube URL', blank=True, null=True)
    facebook_link = models.URLField(verbose_name='Facebook URL', blank=True, null=True)
    instagram_link = models.URLField(verbose_name='Instagram URL', blank=True, null=True)
    linkedin_link = models.URLField(verbose_name='Linkedin URL', blank=True, null=True)
    twitter_link = models.URLField(verbose_name='Twitter URL', blank=True, null=True)
    github_link = models.URLField(verbose_name='Github URL', blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('account:profile_detail', kwargs={'username':self.user.username})

    class Meta:
        ordering = ('-created_at',)