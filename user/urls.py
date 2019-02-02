# File urls created on: 10-05-16 by: ejah
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import RedirectView, TemplateView
from .views import DisableAccount, CreateAccount, ActivateAccount, ResendActivationEmail

password_urls = [
    url(r'^$', RedirectView.as_view(pattern_name=('ej-user:pw_reset_start'), permanent=False)),
    url(r'^wijzigen/$', auth_views.PasswordChangeView,
        {"template_name": "user/password_change_form.html",
         "post_change_redirect": reverse_lazy('ej-user:pw_change_done')},
        name="pw_change"),
    url(r'^wijzigen/gereed/$', auth_views.PasswordChangeDoneView, {'template_name': "user/password_change_done.html"},
        name="pw_change_done"),
    url(r'reset/$', auth_views.PasswordResetView, {"template_name": "user/password_reset_form.html",
                                                "email_template_name": "user/password_reset_email.txt",
                                                "subject_template_name": "user/password_reset_subject.txt",
                                                "post_reset_redirect": reverse_lazy("ej-user:pw_reset_sent")},
        name='pw_reset_start'),
    url(r'^reset/verzonden/$', auth_views.PasswordResetDoneView, {"template_name": "user/password_reset_sent.html"},
        name="pw_reset_sent"),
    url(r'^reset/'
        r'(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}'
        r'-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView,
        {"template_name": "user/password_reset_confirm.html",
         "post_reset_redirect": reverse_lazy("ej-user:pw_reset_complete")},
        name="pw_reset_confirm"),
    url(r'^reset/gereed/$', auth_views.PasswordResetCompleteView,
        {"template_name": "user/password_reset_complete.html", "extra_context": {"form": AuthenticationForm}},
        name="pw_reset_complete"),
]

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='ej-user:login', permanent=False)),
    url(r'^login/$', auth_views.LoginView, {"template_name": "user/login.html"}, name="login"),
    url(r'^logout/$', auth_views.LogoutView, {'template_name': "user/logged_out.html",
                                          "extra_context": {"form": AuthenticationForm}},
        name="logout"),
    url(r'^password/', include(password_urls)),
    url(r'^disable/$', DisableAccount.as_view(), name='disable'),
    url(r'^create/$', CreateAccount.as_view(), name="create"),
    url(r'^create/done/$', TemplateView.as_view(template_name='user/create_done.html'), name='create_done'),
    url(r'^activate/'
        r'(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}'
        r'-[0-9A-Za-z]{1,20})/$',
        ActivateAccount.as_view(), name='activate'),
    url(r'^activate/resend/$', ResendActivationEmail.as_view(), name="resend_activation"),
    url(r'activate', RedirectView.as_view(pattern_name=('ej-user:resend_activation'), permanent=False)),

]
