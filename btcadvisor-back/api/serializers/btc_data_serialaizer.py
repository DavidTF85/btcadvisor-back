from rest_framework import serializers
from foundation.models import LLIStudentData

class btcDataSerializer(serializers.Serializer):


    date = serializers.DateField()
    low = serializers.IntegerField()
    high = serializers.IntegerField()
    open = serializers.IntegerField()
    close = serializers.IntegerField()
    volumefrom = serializers.IntegerField()
    volumeto = serializers.IntegerField()
