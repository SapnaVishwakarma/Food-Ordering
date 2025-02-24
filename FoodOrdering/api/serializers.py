from rest_framework import serializers
from api.models import Product

#create serializers here
class ProductSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields="__all__"