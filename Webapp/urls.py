from django.urls import path, include
from django.contrib.auth import views
from django.contrib import admin
from apps.Feed.views import frontpage, search, submit, newest, vote, feed
from apps.Forum.views import register,forgot
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('s/<int:feed_id>/vote/', vote, name='vote'),
    path('s/<int:feed_id>/', feed, name='feed'),
    path('newest/', newest, name='newest'),
    path('search/', search, name='search'),
    path('submit/', submit, name='submit'),
    path('register/', register, name='register'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('forgot/',forgot,name="fogot"),
    path('u/', include('apps.Userprofile.urls')),
]

urlpatterns+=staticfiles_urlpatterns()