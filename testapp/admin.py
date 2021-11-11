from django.contrib import admin
from .models import NewModel, TestModel,Album, Track
# Register your models here.


admin.site.register(NewModel)
admin.site.register(TestModel)
admin.site.register(Album)
admin.site.register(Track)