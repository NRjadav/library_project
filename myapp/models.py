from django.db import models
from googletrans import Translator
# Create your models here.


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
    
class author(models.Model):
    category_data=models.ForeignKey(category,on_delete=models.CASCADE,blank=True,null=True)  
    author_english=models.CharField(max_length=50,blank=True,null=True)      
    author_hindi=models.CharField(max_length=50,blank=True,null=True) 

    def __str__(self) -> str:
        return self.author_english     
   
class user(models.Model):
    user_id=models.CharField(max_length=100,blank=True,null=True)  
    languages=models.CharField(max_length=100,blank=True,null=True) 
    def __str__(self) -> str:
        return self.user_id 


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