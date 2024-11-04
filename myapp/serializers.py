
from rest_framework import serializers
from .models import*

#------------- category ----------------

class category_serializers(serializers.Serializer):
    
    id = serializers.IntegerField(required=False)
    category_english=serializers.CharField(max_length=50,required=True)
    category_hindi=serializers.CharField(max_length=50,required=True)
    """श्रीमद्भगवद्गीता"""

    class Meta:
        models=category
        fields ='__all__'
        exclude = ('id',) 

    def create(self, validated_data):
        return category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category_english=validated_data.get('category_english',instance.category_english)
        
        instance.category_hindi=validated_data.get('category_hindi',instance.category_hindi)
        
        

        instance.save()
        return instance        
    