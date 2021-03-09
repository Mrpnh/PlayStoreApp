from rest_framework import serializers
from playstore.models import AppAdmin


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        # specifies the model
        model=AppAdmin
        # specifies the fields
        fields=['id','name','appID','downloadLink','category','points']