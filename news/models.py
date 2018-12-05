import datetime as dt
from django.db import models

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank = True)

    def __str__(self):
        return self.first_name
        try:
            editor = Editor.objects.get(email = 'example@gmail.com')
            print('Editor found')
        except DoesNotExist:
            print('Editor was not found') 
    def save_editor(self):
        self.save()

    def delete_editor(self):
        editor = Editor.objects.get(pk=self.id)
        editor.delete()
    
    class Meta:
        ordering = ['first_name']
               
class tags(models.Model):
    name = models.CharField(max_length =30)

    def ___str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/')

    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news

    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return news

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news
