from django.db import models

# Create your models here.


class category(models.Model):
    category_english = models.CharField(max_length=255)
    category_hindi = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.category_english
    
class author(models.Model):
    category_data=models.ForeignKey(category,on_delete=models.CASCADE,blank=True,null=True)  
    author_english=models.CharField(max_length=50,blank=True,null=True)      
    author_hindi=models.CharField(max_length=50,blank=True,null=True) 

    def __str__(self) -> str:
        return self.author_english     
   

    def __str__(self):
        return self.author_english    