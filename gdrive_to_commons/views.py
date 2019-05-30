from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView


class UserLogoutView(LogoutView):
    template_name = "home.html"


class PrivacyPolicyTemplateView(TemplateView):
    template_name = "privacy_policy.html"
