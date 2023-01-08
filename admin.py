from django.contrib import admin
from .models import Image

# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_dispaly=['id','photo','date']
#admin.site.register(Image,ImageAdmin)
