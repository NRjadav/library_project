
from rest_framework import serializers
from .models import*
from googletrans import Translator


# ===================== Category ===================

class category_serializers(serializers.Serializer):
    
    category_id = serializers.IntegerField(source='id',required=False)
    category_english=serializers.CharField(max_length=50,required=False)
    category_hindi=serializers.CharField(max_length=50,required=False)
    timestamp = serializers.SerializerMethodField()
    number=serializers.IntegerField(required=False)

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
    def get_timestamp(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
        local_dt = obj.timestamp.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')
    def create(self, validated_data):
        return category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category_english=validated_data.get('category_english',instance.category_english)
        
        instance.category_hindi=validated_data.get('category_hindi',instance.category_hindi)
        instance.number=validated_data.get('number',instance.number)
        
        

        instance.save()
        return instance        
    

#  ===================== Author ===================
    

    
class author_serializers(serializers.Serializer):
    author_id = serializers.IntegerField(source='id',required=False)
    category_data = serializers.SlugRelatedField(slug_field='id', queryset=category.objects.all(), required=False)
    author_english = serializers.CharField(max_length=100, required=True)
    author_hindi=serializers.CharField(max_length=50,required=True)
    timestamp = serializers.SerializerMethodField()
    
    class Meta:
        model = author
        fields = '__all__'
        exclude = ('id',) 
    
    def get_timestamp(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
        local_dt = obj.timestamp.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')
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
        
#  ===================== Languages ===================
    

    
class Languages_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    languages=serializers.CharField(max_length=50,required=True)
    
    class Meta:
        model = Language
        fields = '__all__'
        exclude = ('id',) 
    
    
    def create(self, validated_data):
        return Language.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.languages=validated_data.get('languages',instance.languages)

        instance.save()
        return instance 


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
        fields = ['id','book_name_english']

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
from datetime import timedelta
from django.utils import timezone
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
    timestamp = serializers.SerializerMethodField()
    password_time=serializers.DateTimeField(required=False,format="%Y-%m-%d %H:%M:%S.%f", read_only=True)
    is_expired = serializers.SerializerMethodField()
    premium=serializers.BooleanField(default=False)
    class Meta:
        model = login_user
        fields = '__all__'
        exclude = ('id',) 
    def get_is_expired(self, obj):
        if obj.password_time:
            expiration_duration = timedelta(minutes=1)  # Set the expiration duration to 1 minute
            current_time = timezone.now()

            # Ensure password_time is aware
            if timezone.is_naive(obj.password_time):
                password_time_aware = timezone.make_aware(obj.password_time, timezone.get_default_timezone())
            else:
                password_time_aware = obj.password_time

            expiration_time = password_time_aware + expiration_duration

            # Compare current_time with expiration_time and reverse the logic
            return not (current_time > expiration_time)
        return False
    def get_timestamp(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  
        local_dt = obj.timestamp.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')
    def get_wishlist_data(self, obj):
        # Get the wishlist related to the login_user instance
        purchase_instances = wishlist.objects.filter(user_data=obj)
        print(purchase_instances, "data")

        # Check if there are any purchases
        if purchase_instances.exists():
            # Serialize the books from all purchase instances
            books = [purchase.book_data for purchase in purchase_instances]
            return BookSerializer11(books, many=True).data  # Serialize multiple books
        return []

    def get_purchase_data(self, obj):
       
        purchase_instances = add_book.objects.filter(user_data=obj)
        print(purchase_instances, "data")

        # Check if there are any purchases
        if purchase_instances.exists():
          
            books = [purchase.book_data for purchase in purchase_instances]
            return BookSerializer11(books, many=True).data  
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
        instance.premium=validated_data.get('premium',instance.premium)
        # instance.device_token=validated_data.get('device_token',instance.device_token)
       
        instance.save()
        return instance  
    def to_representation(self, instance):
   
        representation = super().to_representation(instance)

        
        purchase_data = representation.get('purchase_data', [])

        for book in representation.get("wishlist_data", []):
            book["purchase"] = any(purchase['id'] == book['id'] for purchase in purchase_data)

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

# =============== Use Book Serializer   =================
class language___Serializer(serializers.ModelSerializer):
   
    class Meta:
        model = Language
        fields ='__all__'


# =============== Book =================

class BooksSerializer(serializers.ModelSerializer):
    author_data = serializers.PrimaryKeyRelatedField(many=True, queryset=author.objects.all(), required=False)
    category_data = serializers.PrimaryKeyRelatedField(many=True, queryset=category.objects.all(), required=False)
    language_data = serializers.PrimaryKeyRelatedField(many=True, queryset=Language.objects.all(), required=False)
    book_keywords = serializers.ListField(
        child=serializers.CharField(max_length=255, allow_blank=True),
        required=False
    )
    
    book_front_image=serializers.ImageField(required=False)
    book_file=serializers.FileField(required=False)
    timestamp = serializers.SerializerMethodField()

    class Meta:
        model = Books
        fields = '__all__'
        # exclude = ('id',)  # If you wish to exclude `id`, otherwise remove this line.
    def get_timestamp(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
        local_dt = obj.timestamp.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')
    def create(self, validated_data):
        author_data = validated_data.pop('author_data', [])
        category_data = validated_data.pop('category_data', [])
        language_data = validated_data.pop('language_data', [])
        book = Books.objects.create(**validated_data)
        book.author_data.set(author_data)
        book.category_data.set(category_data)
        book.language_data.set(language_data)
        return book

  
        
    def update(self, instance, validated_data):
        instance.book_name_english = validated_data.get('book_name_english', instance.book_name_english)
        instance.book_name_hindi = validated_data.get('book_name_hindi', instance.book_name_hindi)
        instance.book_front_image = validated_data.get('book_front_image', instance.book_front_image)
        instance.book_file = validated_data.get('book_file', instance.book_file)
        instance.book_details_english = validated_data.get('book_details_english', instance.book_details_english)
        instance.book_details_hindi = validated_data.get('book_details_hindi', instance.book_details_hindi)
        instance.book_price_discount = validated_data.get('book_price_discount', instance.book_price_discount)
        instance.book_price = validated_data.get('book_price', instance.book_price)
        instance.book_free_demo = validated_data.get('book_free_demo', instance.book_free_demo)
        instance.book_keywords = validated_data.get('book_keywords', instance.book_keywords)
        

        if 'author_data' in validated_data:
            instance.author_data.set(validated_data.get('author_data'))
        if 'category_data' in validated_data:
            instance.category_data.set(validated_data.get('category_data'))
        if 'language_data' in validated_data:
            instance.language_data.set(validated_data.get('language_data'))    

        instance.save()
        return instance
    
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Serialize each related category in the `category_data` ManyToMany field
        
        if not instance.book_front_image:
            representation['book_front_image'] = instance.book_name_english
        # if representation.get('book_keywords') is None:
        #     representation['book_keywords'] = []    
    
        
        representation['category_data'] = category___Serializer(instance.category_data.all(), many=True).data if instance.category_data.exists() else None
        
        representation['author_data'] = author___Serializer(instance.author_data.all(), many=True).data if instance.author_data.exists() else None
        
        representation['language_data'] = language___Serializer(instance.language_data.all(), many=True).data if instance.language_data.exists() else []
        
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

# ========================== Hylighter ========================
    
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
    book_data= serializers.SlugRelatedField(slug_field='id', queryset=Books.objects.all(), required=True )
    
    
    
    class Meta:
        model = wishlist
        fields = "__all__"
        
    def create(self, validated_data):
        
        return wishlist.objects.create(**validated_data)
       
         
       
    def update(self, instance, validated_data):
        
        instance.user_data=validated_data.get('user_data',instance.user_data)
        instance.book_data=validated_data.get('book_data',instance.book_data)
      
        instance.save()   
        return instance    
    
    def to_representation(self, instance):
        # Get the default representation
        representation = super().to_representation(instance)

        # Add user data and book data
        representation["user_data"] = user_data_notification(instance.user_data).data
        representation["book_data"] = BooksSerializer(instance.book_data).data
        
        # If book_data is a list, iterate over it
        if isinstance(representation["book_data"], list):
            for book in representation["book_data"]:
                # Filter the add_book table to find entries based on user_id and book_id
                uid = add_book.objects.filter(
                    user_data__user_id=representation["user_data"]["user_id"],
                    book_data=book["id"]
                )
                
                # Add purchase field to each book representation
                book["purchase"] = uid.exists()
        else:
            # If book_data is a single object, handle it directly
            book = representation["book_data"]
            uid = add_book.objects.filter(
                user_data__user_id=representation["user_data"]["user_id"],
                book_data=book["id"]
            )
            book["purchase"] = uid.exists()
        
        return representation




# =========================== Hylighter ================

import json
from datetime import datetime
import pytz  # Ensure pytz is imported for timezone handling

class WordsField(serializers.Field):
    def to_representation(self, value):
        # Convert JSON string to Python list of dictionaries
        try:
            words_list = json.loads(value)
        except (TypeError, ValueError):
            words_list = []

        # Ensure the ordering of fields with `id` appearing before `book_page`
        for word in words_list:
            ordered_word = {}
            if 'id' in word:
                ordered_word['id'] = word.pop('id')  # Add `id` first
            if 'book_page' in word:
                ordered_word['book_page'] = word.pop('book_page')  # Add `book_page` next
            ordered_word.update(word)  # Add the remaining fields
            word.clear()
            word.update(ordered_word)

        return words_list

    def to_internal_value(self, data):
        # Allowed keys for each word entry
        allowed_keys = {'book_page', 'color', 'word', 'timestamp'}

        if isinstance(data, list):
            # Retrieve existing data
            existing_data = self.parent.instance.words if self.parent.instance and self.parent.instance.words else "[]"
            try:
                existing_data_list = json.loads(existing_data)
            except (TypeError, ValueError):
                existing_data_list = []

            # Determine the current maximum id (replacing index)
            max_id = max((entry.get('id', 0) for entry in existing_data_list), default=0)

            updated_data = existing_data_list
            for word in data:
                if not isinstance(word, dict):
                    raise serializers.ValidationError("Each item in the list must be a dictionary.")
                if not allowed_keys.issuperset(word.keys()):
                    raise serializers.ValidationError(f"Only these fields are allowed: {allowed_keys}")

                # Auto-generate 'id' as a unique ID
                max_id += 1
                word['id'] = max_id

                # Add timestamp if not present
                if 'timestamp' not in word:
                    local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired timezone
                    word['timestamp'] = datetime.now(local_tz).strftime('%Y-%m-%d %H:%M:%S')

                updated_data.append(word)

            try:
                value = json.dumps(updated_data)
            except (TypeError, ValueError):
                raise serializers.ValidationError("Invalid format for words.")
        else:
            raise serializers.ValidationError("Expected a list of dictionaries.")
        return value


class HylighterSerializer1(serializers.ModelSerializer):
    user_data= serializers.SlugRelatedField(slug_field='user_id', queryset=login_user.objects.all(), required=True)
    book_data= serializers.SlugRelatedField(slug_field='id', queryset=Books.objects.all(), required=True)
    words = WordsField()
    
    class Meta:
        model = hylighter1
        fields = "__all__"
       
    
    def create(self, validated_data):
        return hylighter1.objects.create(**validated_data)
       
    def update(self, instance, validated_data):
        
        instance.user_data=validated_data.get('user_data',instance.user_data)
        instance.book_data=validated_data.get('book_data',instance.book_data)
        instance.words=validated_data.get('words',instance.words)
        instance.save()
        return instance    
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["user_data"] = user_data_notification(instance.user_data).data 
        representation["book_data"] = BooksSerializer(instance.book_data).data
        return representation 