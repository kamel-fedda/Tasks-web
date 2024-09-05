from dataclasses import field
from rest_framework import serializers
from Data.models import *


class TasksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__' 