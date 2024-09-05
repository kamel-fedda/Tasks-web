from .models import *
from django.forms import ModelForm



class AddTask(ModelForm):

    class Meta:
        model = Tasks
        fields = ['title','description','user'] 