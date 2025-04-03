from django.contrib import admin

from .models import books


# books : ['user','book_name','author']




class booksAdmin(admin.ModelAdmin):
    list_display = ['student_name','book_name','author','issue_date','return_date']

    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(books,booksAdmin)
# Register your models here.