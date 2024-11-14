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
    device_token=models.CharField(max_length=50,blank=True,null=True)
    name=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(max_length=100,blank=True,null=True)
    mobile_no=models.IntegerField(blank=True,null=True)
    image=models.ImageField(upload_to="image",blank=True,null=True) 
    password=models.CharField(max_length=100,blank=True,null=True)
    languages=models.CharField(max_length=100,blank=True,null=True)
    theme=models.CharField(max_length=100,blank=True,null=True)
    def __str__(self) -> str:
        return self.name 
    


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
    purchase = models.BooleanField(default=False)
    
    def __str__(self):
        return self.book_name_hindi    


# ======================= Ad ========================



class ad(models.Model):
    file=models.FileField(upload_to="video")
    type = models.CharField(max_length=500,blank=True, null=True)           

# ======================= Notification ==================
    

class notification(models.Model):
    user_data = models.ManyToManyField(login_user, blank=True, null=True)
    message=models.TextField()
    title = models.CharField(max_length=255)
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)



# =========================== Hylighter ================
    
class hylighter(models.Model):    
    user_data = models.ForeignKey(login_user,on_delete=models.CASCADE)  
    book_data = models.ForeignKey(Books,on_delete=models.CASCADE)  
    color = models.CharField(max_length=255)
    words=ListTextField(base_field=models.CharField(max_length=1000),size=1000,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now=True)

# =========================== Add Cart Book ================    
    
class add_book(models.Model):
    user_data = models.ForeignKey(login_user,on_delete=models.CASCADE)  
    book_data = models.ForeignKey(Books,on_delete=models.CASCADE)
    qty=models.IntegerField()
    total=models.IntegerField()

# =========================== Add Wishlist Book ================    


class wishlist(models.Model):
    user_data = models.ForeignKey(login_user,on_delete=models.CASCADE)  
    book_data = models.ManyToManyField(Books)
    

