from rest_framework import serializers
from .models import Call


class CallCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('caller', 'receiver', 'recording', 'status')
        model = Call
