from django.contrib import admin

# Register your models here.
from .models import Feed,Discussion,Vote,Discussion2
class FeedAdmin(admin.ModelAdmin):
    fields=['title','url','number_of_votes','created_by']

admin.site.register(Feed,FeedAdmin)
admin.site.register(Vote)
admin.site.register(Discussion)
admin.site.register(Discussion2)