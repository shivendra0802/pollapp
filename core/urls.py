from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from poll import views as poll_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', include('testapp.urls')),
    path('', poll_views.home, name='home'),
        # path('', poll_views.home, name='home'),
    path('create/', poll_views.create, name='create'),
    path('vote/<poll_id>/', poll_views.vote, name='vote'),
    path('results/<poll_id>/', poll_views.results, name='results'),
]
