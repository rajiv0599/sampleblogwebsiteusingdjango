from django.contrib import admin

# Register your models here.
from .models import blog,blogcomments

class blogcommentsAdmin(admin.ModelAdmin):
    search_fields=['comment']

class blogAdmin(admin.ModelAdmin):
    search_fields=['content']


#admin.site.register((blog,blogcomments))
admin.site.register(blog,blogAdmin)
admin.site.register(blogcomments,blogcommentsAdmin)




