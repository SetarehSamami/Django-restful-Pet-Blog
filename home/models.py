from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    animal_type = models.CharField(max_length=15)
    
    def __str__(self):
        return self.animal_type

class Post(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=20)
    description=models.TextField()
    race=models.CharField(max_length=15, blank=True)  
    image=models.ImageField(upload_to='petimage/')
    animal_age=models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=('title',)  
    
    def __str__(self):
        return self.title
        
class Comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    text=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user}_{self.title[:20]}'
        
class Answer(models.Model):
    comment=models.ForeignKey(Comment, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.TextField()
    
    def __str__(self):
        return f'{self.user}'