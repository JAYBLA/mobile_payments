from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from .models import Profile

no_space_validator = RegexValidator(
    r' ',
    _('No spaces allowed'),
    inverse_match=True,
    code='invalid_username')


def clean_unique(form, field, exclude_initial=True, 
                 format="The %(field)s %(value)s has already been taken."):
    value = form.cleaned_data.get(field)
    if value:
        qs = form._meta.model._default_manager.filter(**{field:value})
        if exclude_initial and form.initial:
            initial_value = form.initial.get(field)
            qs = qs.exclude(**{field:initial_value})
        if qs.count() > 0:
            raise forms.ValidationError(format % {'field':field, 'value':value})
    return value


class CustomSignupForm(SignupForm):

    username = forms.CharField(required=True, label='Username',validators=[no_space_validator])

    # Override the init method
    def __init__(self, *args, **kwargs):
        # Call the init of the parent class
        super().__init__(*args, **kwargs)
        
        self.fields["username"].widget.attrs["placeholder"] = 'username'


    # Put in custom signup logic
    # def custom_signup(self, request, user):
    #     user_profile = Profile(user=user)
    #     user_profile.save()

    #     user.save()


class MyAuthForm(AuthenticationForm):
    error_messages = {
        'invalid_login': _(
            "Email or Password is not correct"
        ),
        'inactive': _("This account is inactive."),
    }


class ProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False, \
     error_messages ={'invalid':("Image files only")},\
     widget=forms.FileInput)


    class Meta:
        model = Profile
        fields = ['profile_picture','website', 'country', 'location', 'bio', 'youtube_link', 'facebook_link', 'instagram_link', 'linkedin_link','twitter_link','github_link',]
        widgets = {
			'bio': forms.Textarea(attrs={'rows': 3}),
		}