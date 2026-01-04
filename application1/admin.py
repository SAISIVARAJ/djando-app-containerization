from django.contrib import admin 
from application1.models import Users 
class Users_Admin(admin.ModelAdmin):
    list_display=['First_Name','Last_Name','Username','P1','P2','Email_Address','Mobile_Number']
admin.site.register(Users,Users_Admin)

