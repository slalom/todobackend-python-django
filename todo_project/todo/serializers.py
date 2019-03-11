#todo/serializers.py

from rest_framework import serializers
from .models import todo

class todoSerializer(serializers.ModelSerializer):
	class Meta:
		model = todo
		fields = ("title", "completed")
