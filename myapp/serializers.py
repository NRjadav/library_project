
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
class BooksSerializer1(serializers.ModelSerializer):
    
    class Meta:
        model = Books
        fields = '__all__'
        # exclude = ('id',)     

class WishlistSerializer1(serializers.ModelSerializer):
    # book_data = BooksSerializer1(many=True)  # Serialize the related books
    
    
    class Meta:
        model = wishlist
        fields = ['id', 'book_data']

    def to_representation(self, instance):
        # Get the default representation
        representation = super().to_representation(instance)
        
        # Add user data and book data
        # representation["user_data"] = user_data_notification(instance.user_data).data
        # representation["book_data"] = BooksSerializer1(instance.book_data, many=True).data
        
        # Iterate through the book data
        # for book in representation["book_data"]:
        #     # Print book ID (just for debugging purposes)
        #     print(book["id"])
            
        #     # Filter the add_book table to find entries based on user_id and book_id
        #     uid = add_book.objects.filter(
        #         user_data__user_id=representation["user_data"]["user_id"],
        #         book_data=book["id"]  # Compare with the book ID
        #     )
            
        #     # Print the filtered add_book entries (for debugging)
        #     print(uid)
            
        #     # Optionally, you could add the result of the query into the representation if needed
        #     # For example, you could include a flag indicating whether the book has been added to the list:
        #     book["purchase"] = uid.exists()  # Adds a new field `is_in_add_book`
        
        return representation    

class PurchaseSerializer1(serializers.ModelSerializer):
      
    
    
    class Meta:
        model = add_book
        fields = "__all__"
    def to_representation(self, instance):
        # Get the default representation
        representation = super().to_representation(instance)
        
        # Add user data and book data
        representation["user_data"] = user_data_notification(instance.user_data).data 
        representation["book_data"] = BooksSerializer(instance.book_data).data 
        return representation    

class BookSerializer11(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

    def to_representation(self, instance):
        # Get the default representation
        representation = super().to_representation(instance)

        # Fetch the user's purchase data (this is just an example; adjust as necessary)
        # Assuming `purchase_data` is passed along with the serialized data, 
        # you should have access to this information in the context.
        purchase_data = self.context.get('purchase_data', [])

        # Iterate through wishlist_data to check if the book exists in purchase_data
        for book in representation.get("wishlist_data", []):
            # Set purchase to True if the book is in purchase_data
            if any(purchase['book_data']['id'] == book['id'] for purchase in purchase_data):
                book["purchase"] = True
            else:
                book["purchase"] = False

        # Return the modified representation
        return representation        

class login_user_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    user_id=serializers.CharField(max_length=100,required=False)   
    device_token=serializers.CharField(max_length=255,required=False)
    name=serializers.CharField(max_length=100,required=False)
    mobile_no = serializers.IntegerField(required=False)
    email=serializers.CharField(max_length=100,required=False)
    image=serializers.ImageField(required=False)
    password=serializers.CharField(max_length=100,required=False)
    languages=serializers.CharField(max_length=20,required=False)
    theme=serializers.CharField(max_length=20,required=False)
    wishlist_data = serializers.SerializerMethodField()
    purchase_data = serializers.SerializerMethodField()
    class Meta:
        model = login_user
        fields = '__all__'
        exclude = ('id',) 
    
    def get_wishlist_data(self, obj):
        # Get the wishlist related to the login_user instance
        wishlist_instance = wishlist.objects.filter(user_data=obj).first()
        if wishlist_instance:
            # Serialize the book data from the wishlist
            return BookSerializer11(wishlist_instance.book_data.all(), many=True).data
        return []

    def get_purchase_data(self, obj):
       
        purchase_instances = add_book.objects.filter(user_data=obj)
        print(purchase_instances, "data")

        # Check if there are any purchases
        if purchase_instances.exists():
            # Serialize the books from all purchase instances
            books = [purchase.book_data for purchase in purchase_instances]
            return BookSerializer11(books, many=True).data  # Serialize multiple books
        return []
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
        # instance.device_token=validated_data.get('device_token',instance.device_token)
       
        instance.save()
        return instance  
    def to_representation(self, instance):
    # Get the default representation
        representation = super().to_representation(instance)

        # Fetch the user's purchase data (this is just an example; adjust as necessary)
        purchase_data = representation.get('purchase_data', [])

        # Iterate through wishlist_data to check if the book exists in purchase_data
        for book in representation.get("wishlist_data", []):
            # Set purchase to True if the book is in purchase_data
            # Iterate over purchase_data to find a match
            book["purchase"] = any(purchase['id'] == book['id'] for purchase in purchase_data)

        # Return the modified representation
        return representation

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
            


# ================== Ad ==============

# import mimetypes
class ad_serializers(serializers.ModelSerializer):
    class Meta:
        model = ad
        fields = ['id', 'file', 'type']
    
    def create(self, validated_data):
        # Handle file upload in the create method
        # file = validated_data.get('file')
        # validated_data['type'] = self.get_file_type(file)
        return ad.objects.create(**validated_data)
        # return ad_instance

    def update(self, instance, validated_data):
        # Handle file upload in the update method
        instance.file = validated_data.get('file', instance.file)
        instance.type = validated_data.get('type', instance.type)
        instance.save()
        return instance
    
    # def get_file_type(self, file):
    #     # Get the MIME type of the file
    #     mime_type, _ = mimetypes.guess_type(file.name)
    #     return mime_type if mime_type else 'unknown'


# ========================== notification =========================

class user_data_notification(serializers.ModelSerializer):
    class Meta:
        model = login_user
        fields = ['id','user_id','name','image']

import json
import pytz
class NotificationSerializer(serializers.ModelSerializer):
    user_data= serializers.SlugRelatedField(slug_field='user_id', queryset=login_user.objects.all(), required=True,many=True)
    timestamp = serializers.SerializerMethodField()
    
    class Meta:
        model = notification
        fields = ['id', 'user_data', 'message', 'title', 'read', 'timestamp']
        read_only_fields = ['timestamp']
    def get_timestamp(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
        local_dt = obj.timestamp.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')  
    def create(self, validated_data):
        user_data_1 = validated_data.pop('user_data', [])
      
        noti=notification.objects.create(**validated_data)
        noti.user_data.set(user_data_1)
        noti.save()
        return noti
    def update(self, instance, validated_data):
        user_data_1 = validated_data.pop('user_data', [])
       
        if user_data_1:
            instance.user_data.set(user_data_1)
        instance.message=validated_data.get('message',instance.message)
        instance.title=validated_data.get('title',instance.title)
        instance.read=validated_data.get('read',instance.read)
        instance.save()
        return instance    
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["user_data"] = user_data_notification(instance.user_data,many=True).data 
        return representation 


class HylighterSerializer(serializers.ModelSerializer):
    user_data= serializers.SlugRelatedField(slug_field='user_id', queryset=login_user.objects.all(), required=True)
    book_data= serializers.SlugRelatedField(slug_field='book_name_english', queryset=Books.objects.all(), required=True)
    color=serializers.CharField(max_length=100,required=False)
    words = serializers.ListField(
        child=serializers.CharField(max_length=255, allow_blank=True),
        required=False
    )
    timestamp = serializers.SerializerMethodField()
    
    class Meta:
        model = hylighter
        fields = "__all__"
        read_only_fields = ['timestamp']
    def get_timestamp(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
        local_dt = obj.timestamp.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')  
    def create(self, validated_data):
        return hylighter.objects.create(**validated_data)
       
    def update(self, instance, validated_data):
        
        instance.user_data=validated_data.get('user_data',instance.user_data)
        instance.book_data=validated_data.get('book_data',instance.book_data)
        instance.color=validated_data.get('color',instance.color)
        instance.words=validated_data.get('words',instance.words)
        instance.save()
        return instance    
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["user_data"] = user_data_notification(instance.user_data).data 
        return representation 


# =========================== Add Cart Book ================    

class Book_cart_serializers(serializers.ModelSerializer):
    book_keyword_english = serializers.ListField(
        child=serializers.CharField(max_length=255, allow_blank=True),
        required=False
    )
    book_keyword_hindi = serializers.ListField(
        child=serializers.CharField(max_length=255, allow_blank=True),
        required=False
    )
    class Meta:
        
        model = Books
        fields = "__all__"


class Add_Book_Serializer(serializers.ModelSerializer):
    user_data= serializers.SlugRelatedField(slug_field='user_id', queryset=login_user.objects.all(), required=True)
    book_data= serializers.SlugRelatedField(slug_field='book_name_english', queryset=Books.objects.all(), required=True)
    qty=serializers.IntegerField(required=False)
    total=serializers.IntegerField(required=False)
    
    
    class Meta:
        model = add_book
        fields = "__all__"
        
    def create(self, validated_data):
        return add_book.objects.create(**validated_data)
       
    def update(self, instance, validated_data):
        
        instance.user_data=validated_data.get('user_data',instance.user_data)
        instance.book_data=validated_data.get('book_data',instance.book_data)
        instance.qty=validated_data.get('qty',instance.qty)
        instance.total=validated_data.get('total',instance.total)
        instance.save()
        return instance    
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["user_data"] = user_data_notification(instance.user_data).data 
        representation["book_data"] = Book_cart_serializers(instance.book_data).data 
        
        return representation 


# =========================== Add Wishlist Book ================    


class Add_Wishlist_Book_Serializer(serializers.ModelSerializer):
    user_data= serializers.SlugRelatedField(slug_field='user_id', queryset=login_user.objects.all(), required=True)
    book_data= serializers.SlugRelatedField(slug_field='id', queryset=Books.objects.all(), required=True ,many=True)
    
    
    
    class Meta:
        model = wishlist
        fields = "__all__"
        
    def create(self, validated_data):
        
        book_data = validated_data.pop('book_data', [])
        book = wishlist.objects.create(**validated_data)
        book.book_data.set(book_data)
        return book
       
    def update(self, instance, validated_data):
        
        instance.user_data=validated_data.get('user_data',instance.user_data)
        book_data = validated_data.pop('book_data', [])
       
        if book_data:
            instance.book_data.set(book_data)
      
        instance.save()   
        return instance    
    
    def to_representation(self, instance):
        # Get the default representation
        representation = super().to_representation(instance)
        
        # Add user data and book data
        representation["user_data"] = user_data_notification(instance.user_data).data
        representation["book_data"] = BooksSerializer(instance.book_data, many=True).data
        
        # Iterate through the book data
        for book in representation["book_data"]:
            # Print book ID (just for debugging purposes)
            print(book["id"])
            
            # Filter the add_book table to find entries based on user_id and book_id
            uid = add_book.objects.filter(
                user_data__user_id=representation["user_data"]["user_id"],
                book_data=book["id"]  # Compare with the book ID
            )
            
            # Print the filtered add_book entries (for debugging)
            print(uid)
            
            # Optionally, you could add the result of the query into the representation if needed
            # For example, you could include a flag indicating whether the book has been added to the list:
            book["purchase"] = uid.exists()  # Adds a new field `is_in_add_book`
        
        return representation


