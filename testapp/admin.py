from django.contrib import admin
from testapp.models import Ecommerce,Confirmation

# Register your models here.
class EcommerceAdmin(admin.ModelAdmin):
    list_display=['name','price','discounted_price','category','description','image']


class ConfirmationAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','phone_no','address','email','city','state','pincode','landmark']


admin.site.register(Ecommerce,EcommerceAdmin)
admin.site.register(Confirmation,ConfirmationAdmin)
