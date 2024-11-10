from django.views.generic.edit import CreateView
from users.models import User
from users.forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER


class UserCreateView(CreateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = f"Добро пожаловать, {user_email}!"
        message = "Спасибо, что зарегистрировались на сайте нашего магазина 'Чашечка горячего'!"
        from_email = EMAIL_HOST_USER
        recipient_list = [user_email]
        send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)

