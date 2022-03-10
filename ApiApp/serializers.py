from rest_framework import serializers
from .models import Movies

class MoviesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Movies
        fields = ('id','name','img','summary')
