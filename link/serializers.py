from rest_framework import serializers

from .models import *


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('id', 'name', 'image', 'path')
