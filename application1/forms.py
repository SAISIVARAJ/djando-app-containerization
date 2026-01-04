from application1.models import Users 
from django.forms import ModelForm 
class Users_Form(ModelForm):
    class Meta:
        model=Users 
        fields="__all__"

