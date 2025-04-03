from django.contrib import admin
from .models import account
# Register your models here.
class accountAdmin(admin.ModelAdmin):
    list_display = ['student_name','fees_type','amount','date']

    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(account,accountAdmin)