from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "phone", "project", "message"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control border-0 py-3",
                "placeholder": "Your Name",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control border-0 py-3",
                "placeholder": "Your Email",
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control border-0 py-3",
                "placeholder": "Phone Number (optional)",
            }),
            "project": forms.TextInput(attrs={
                "class": "form-control border-0 py-3",
                "placeholder": "What do you need help with?",
            }),
            "message": forms.Textarea(attrs={
                "class": "w-100 form-control border-0 py-3",
                "rows": 6,
                "placeholder": "Message",
            }),
        }