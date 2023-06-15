from . models import Users
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

class ActiveAccount:
    def __init__(self, user: Users):
        if not isinstance(user, Users):
            raise ValueError("User should be an instance of Users")
        self._user = user
        
    def _generate_url(self) -> str:
        protocol = 'http' if settings.DEBUG else 'https'
        domain = settings.DOMAIN
        uid = urlsafe_base64_encode(force_bytes(self._user.pk))
        token = default_token_generator.make_token(self._user)
        
        return f"{protocol}://{domain}{reverse('active_account', kwargs={'uidb4': uid, 'token': token})}"
    
    def active_account_mail(self):
        active_url = self._generate_url()
        subject = "Active your account"
        mail_body = render_to_string('mails/active_account.html', {'active_url': active_url})
        email = EmailMessage(subject, mail_body, to=[self._user.email])
        if email.send():
            #TODO: add log successful email
            pass
        else:
            #TODO: add log failed email
            pass
            