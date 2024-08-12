from rest_framework.serializers import ModelSerializer,ImageField
from .models import qbank

class Itemserializer(ModelSerializer):

    class Meta:

        model=qbank
        fields=['answer','qtype','image']