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
   

    