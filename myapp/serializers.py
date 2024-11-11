
from rest_framework import serializers
from .models import*
from googletrans import Translator


# ===================== Category ===================

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
    

#  ===================== Author ===================
    

    
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
        

# ===================== User ===================

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

# ===================== Login User ===================

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

# ===================== Admin Login ===================
    
class admin_login_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    email=serializers.CharField(max_length=50,required=True)
    password=serializers.CharField(max_length=50,required=True)

    class Meta:
        models=admin_login
        fields ='__all__'
        exclude = ('id',)


    def create(self, validated_data):
        return admin_login.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email=validated_data.get('email',instance.email)
        instance.password=validated_data.get('password',instance.password)

        instance.save()
        return instance
    



#  =============== Use Book Serializer   =================
class category___Serializer(serializers.ModelSerializer):
   
    
    class Meta:
        model = category
        fields ='__all__'

# =============== Use Book Serializer   =================
class author___Serializer(serializers.ModelSerializer):
   
    class Meta:
        model = author
        fields ='__all__'

# =============== Book =================

class BooksSerializer(serializers.ModelSerializer):
    author_data = serializers.PrimaryKeyRelatedField(many=True, queryset=author.objects.all(), required=False)
    category_data = serializers.PrimaryKeyRelatedField(many=True, queryset=category.objects.all(), required=False)
    book_keyword_english = serializers.ListField(
        child=serializers.CharField(max_length=255, allow_blank=True),
        required=False
    )
    book_keyword_hindi = serializers.ListField(
        child=serializers.CharField(max_length=255, allow_blank=True),
        required=False
    )
    book_front_image=serializers.ImageField(required=False)
    class Meta:
        model = Books
        fields = '__all__'
        # exclude = ('id',)  # If you wish to exclude `id`, otherwise remove this line.
    
    def create(self, validated_data):
        author_data = validated_data.pop('author_data', [])
        category_data = validated_data.pop('category_data', [])
        book = Books.objects.create(**validated_data)
        book.author_data.set(author_data)
        book.category_data.set(category_data)
        return book

  
        
    def update(self, instance, validated_data):
        instance.book_name_english = validated_data.get('book_name_english', instance.book_name_english)
        instance.book_name_hindi = validated_data.get('book_name_hindi', instance.book_name_hindi)
        instance.book_front_image = validated_data.get('book_front_image', instance.book_front_image)
        instance.book_languages = validated_data.get('book_languages', instance.book_languages)
        instance.book_details_english = validated_data.get('book_details_english', instance.book_details_english)
        instance.book_details_hindi = validated_data.get('book_details_hindi', instance.book_details_hindi)
        instance.book_price_discount = validated_data.get('book_price_discount', instance.book_price_discount)
        instance.book_price = validated_data.get('book_price', instance.book_price)
        instance.book_keyword_english = validated_data.get('book_keyword_english', instance.book_keyword_english)
        instance.book_keyword_hindi = validated_data.get('book_keyword_hindi', instance.book_keyword_hindi)
        

        if 'author_data' in validated_data:
            instance.author_data.set(validated_data.get('author_data'))
        if 'category_data' in validated_data:
            instance.category_data.set(validated_data.get('category_data'))

        instance.save()
        return instance
    
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Serialize each related category in the `category_data` ManyToMany field
        
        if not instance.book_front_image:
            representation['book_front_image'] = instance.book_name_english
    
        
        representation['category_data'] = category___Serializer(instance.category_data.all(), many=True).data if instance.category_data.exists() else None
        
        representation['author_data'] = author___Serializer(instance.author_data.all(), many=True).data if instance.author_data.exists() else None
        
        return representation
            


