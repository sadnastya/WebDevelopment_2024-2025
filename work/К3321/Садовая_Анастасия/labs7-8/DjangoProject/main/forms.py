from django.forms import ModelForm
from django.forms import Textarea
from .models import Feedback


class ContactForm(ModelForm):

    class Meta:
        model = Feedback
        fields = ['first_name', 'last_name', 'email', 'message']
        widgets = {
            'message': Textarea(
                attrs={
                    'placeholder': 'Напишите тут ваше сообщение'
                }
            )
        }