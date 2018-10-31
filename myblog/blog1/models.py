from django.db import models

# Create your models here.
class article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

class comment(models.Model):
    article = models.ForeignKey(article,related_name = 'article_comment',on_delete=models.CASCADE)
    detail = models.TextField()
