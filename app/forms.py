from django.forms import ModelForm
from app.models import *

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'username', 'password', 'phone_number', 'email']

class CatForm(ModelForm):
    class Meta:
        model = Cat
        fields = ['id', 'name', 'gender', 'breed', 'age', 'availability', 'price', 'description']