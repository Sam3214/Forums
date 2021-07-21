from django.db import models
from django.contrib.auth.models import User

class Feed(models.Model):
    title=models.CharField(max_length=255)
    url=models.URLField()
    number_of_votes=models.IntegerField(default=1)
    created_by=models.ForeignKey(User,related_name='feeds',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['created_at']
    def __str__(self):
        return '%s' % self.title

class Discussion(models.Model):
    feed=models.ForeignKey(Feed,on_delete=models.CASCADE,related_name='discussions')
    body=models.TextField()
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='discussions')
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-created_at']

class Discussion2(models.Model):
    feed=models.ForeignKey(Feed,on_delete=models.CASCADE,related_name='discussions2')
    body=models.TextField()
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='discussions2')
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-created_at']

class Vote(models.Model):
    feed=models.ForeignKey(Feed,on_delete=models.CASCADE,related_name='votes')      
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='votes')
    def save(self,*args,**kwargs):
        self.feed.number_of_votes+=1
        self.feed.save()
        super(Vote,self).save(*args,**kwargs)