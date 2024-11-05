
from rest_framework import serializers
from .models import*

#------------- category ----------------

class category_serializers(serializers.Serializer):
    
    id = serializers.IntegerField(required=False)
    category_english=serializers.CharField(max_length=50,required=True)
    category_hindi=serializers.CharField(max_length=50,required=True)
    

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
    

#-------------Author_serializers ----------------
    

    
class author_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    category_data = serializers.SlugRelatedField(slug_field='id', queryset=category.objects.all(), required=False)
    author_english = serializers.CharField(max_length=100, required=True)
    author_hindi=serializers.CharField(max_length=50,required=True)
    
    class Meta:
        model = author
        fields = '__all__'
        exclude = ('id',) 
    
    
    def create(self, validated_data):
        return author.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.category_data=validated_data.get('category_data',instance.category_data)
        instance.author_english=validated_data.get('author_english',instance.author_english)
        instance.author_hindi=validated_data.get('author_hindi',instance.author_hindi)
        
        instance.save()
        return instance 

    def to_representation(self, instance):
        representation = super().to_representation(instance)   
        if instance.category_data is not None:
            representation["category_data"] = category_serializers(instance.category_data).data
        else:
            representation["category_data"] = None 
        return representation 
        