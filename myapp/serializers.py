
from rest_framework import serializers
from .models import*
from googletrans import Translator
#------------- category ----------------

class category_serializers(serializers.Serializer):
    
    category_id = serializers.IntegerField(source='id',required=False)
    category_english=serializers.CharField(max_length=50,required=False)
    category_hindi=serializers.CharField(max_length=50,required=False)
    

    class Meta:
        models=category
        fields ='__all__'
        exclude = ('id',) 

    # def create(self, validated_data):
    #     if 'category_hindi' not in validated_data or not validated_data['category_hindi']:
    #         translator = Translator()
    #         translation = translator.translate(validated_data['category_english'], src='en', dest='hi')
    #         validated_data['category_hindi'] = translation.text
        
    #     return category.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.category_english = validated_data.get('category_english', instance.category_english)
        
    #     if 'category_hindi' in validated_data:
    #         instance.category_hindi = validated_data['category_hindi']
            
    #     else:
    #         translator = Translator()
    #         translation = translator.translate(instance.category_english, src='en', dest='hi')
    #         instance.category_hindi = translation.text
        
    #     instance.save()
    #     return instance
  
    def create(self, validated_data):
        return category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category_english=validated_data.get('category_english',instance.category_english)
        
        instance.category_hindi=validated_data.get('category_hindi',instance.category_hindi)
        
        

        instance.save()
        return instance        
    

#-------------Author_serializers ----------------
    

    
class author_serializers(serializers.Serializer):
    author_id = serializers.IntegerField(source='id',required=False)
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
        

#-------------User_serializers ----------------

class user_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    user_id=serializers.CharField(max_length=100,required=False)
    languages=serializers.CharField(max_length=20,required=False,allow_null=True)   

    class Meta:
        model = user
        fields = '__all__'
        exclude = ('id',) 
    
    
    def create(self, validated_data):
        return user.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.user_id=validated_data.get('user_id',instance.user_id)
        instance.languages=validated_data.get('languages',instance.languages)
       
        instance.save()
        return instance   
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation.get('languages') is None:
            representation['languages'] = ""
        return representation  

#-------------Login_User_serializers ----------------

class login_user_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    user_id=serializers.CharField(max_length=100,required=False)   
    name=serializers.CharField(max_length=100,required=False)
    mobile_no = serializers.IntegerField(required=False)
    email=serializers.CharField(max_length=100,required=False)
    image=serializers.ImageField(required=False)
    password=serializers.CharField(max_length=100,required=False)
    languages=serializers.CharField(max_length=20,required=False)
    theme=serializers.CharField(max_length=20,required=False)
    class Meta:
        model = login_user
        fields = '__all__'
        exclude = ('id',) 
    
    
    def create(self, validated_data):
        return login_user.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.user_id=validated_data.get('user_id',instance.user_id)
        instance.name=validated_data.get('name',instance.name)
        instance.mobile_no=validated_data.get('mobile_no',instance.mobile_no)
        instance.email=validated_data.get('email',instance.email)
        instance.image=validated_data.get('image',instance.image)
        instance.password=validated_data.get('password',instance.password)
        instance.languages=validated_data.get('languages',instance.languages)
        instance.theme=validated_data.get('theme',instance.theme)
       
        instance.save()
        return instance   
    