from django.shortcuts import render, get_object_or_404,redirect,reverse
from django.contrib.auth.views import LoginView, LogoutView

from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
import urllib.parse

from .models import Profile
from .forms import ProfileForm,MyAuthForm


def profile_detail(request, username):

    username = urllib.parse.unquote(username)

    profile = get_object_or_404(Profile, user__username=username)

    context = {
        'profile':profile,
    }

    template_name = 'profile/profile_detail.html'

    return render(request, template_name, context=context)


@login_required
def profile_update(request, id):

    profile = get_object_or_404(Profile, user_id=id)

    if profile.user != request.user: 
        raise PermissionDenied()

    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)

    if form.is_valid():
        form.save()

        return redirect(reverse("account:profile_detail", kwargs={
            'username': request.user.username
        }))
        messages.success(request, "You are successfully update profile")
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form':form,
        'profile':profile
    }

    template_name = 'profile/profile_update.html'

    return render(request, template_name, context)

class UserLoginView(LoginView):
    template_name = 'admins/login.html'
    form_class = MyAuthForm

    def get_success_url(self):
        url = self.get_redirect_url()
        if url:
            return url
        if self.request.user.is_admin:
            return reverse('admins:admin_dashboard')
        if self.request.user.is_superuser:
            return f'/superuser/'
        else:
            return f'/'