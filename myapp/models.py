from django.db import models
from googletrans import Translator
from django_mysql.models import ListTextField
# Create your models here.

# ======================== Category =========================

class category(models.Model):
    category_english = models.CharField(max_length=255)
    category_hindi = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.category_english
    
    # def save(self, *args, **kwargs):
    #     if not self.category_hindi:
    #         translator = Translator()
    #         translation = translator.translate(self.category_english, src='en', dest='hi')
    #         self.category_hindi = translation.text
    #     super().save(*args, **kwargs)

# ======================== Author =========================


class author(models.Model):
    category_data=models.ForeignKey(category,on_delete=models.CASCADE,blank=True,null=True)  
    author_english=models.CharField(max_length=50,blank=True,null=True)      
    author_hindi=models.CharField(max_length=50,blank=True,null=True) 

    def __str__(self) -> str:
        return self.author_english     

# ======================== User =========================


class user(models.Model):
    user_id=models.CharField(max_length=100,blank=True,null=True)  
    languages=models.CharField(max_length=100,blank=True,null=True) 
    def __str__(self) -> str:
        return self.user_id 

# ======================== Login User =========================


class login_user(models.Model): 
    user_id=models.CharField(max_length=100,blank=True,null=True)
    name=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(max_length=100,blank=True,null=True)
    mobile_no=models.IntegerField(blank=True,null=True)
    image=models.ImageField(upload_to="image",blank=True,null=True) 
    password=models.CharField(max_length=100,blank=True,null=True)
    languages=models.CharField(max_length=100,blank=True,null=True)
    theme=models.CharField(max_length=100,blank=True,null=True)
    def __str__(self) -> str:
        return self.user_id 
    


# ============== Admin Login ===================
    
class admin_login(models.Model):
    email=models.EmailField(max_length=255,blank=True,null=True)
    password=models.CharField(max_length=255,blank=True,null=True)
    
    def __str__(self):
        return self.email     

# ================= Book =======================
    
class Books(models.Model):
    book_name_english=models.CharField(max_length=255,blank=True,null=True)
    book_name_hindi=models.CharField(max_length=255,blank=True,null=True)
    book_front_image=models.ImageField(upload_to='image', null=True, blank=True)
    book_languages=models.CharField(max_length=255,blank=True,null=True)
    author_data=models.ManyToManyField(author,blank=True,null=True)
    category_data=models.ManyToManyField(category,blank=True,null=True)
    book_details_english=models.TextField(blank=True,null=True)
    book_details_hindi=models.TextField(blank=True,null=True)
    book_price_discount=models.IntegerField()
    book_price=models.FloatField()
    book_keyword_english=ListTextField(base_field=models.CharField(max_length=255,blank=True,null=True),size=100,blank=True,null=True)
    book_keyword_hindi=ListTextField(base_field=models.CharField(max_length=255,blank=True,null=True),size=100,blank=True,null=True)
    
    
    def __str__(self):
        return self.book_name_hindi    