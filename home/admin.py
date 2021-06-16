from django.contrib import admin


from . models import Setting, ContactMessage, Brand, Testimonial
# Register your models here.

class SettingAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'company','status','icon','logo','menu_icon','cart_icon')


class BrandAdmin(admin.ModelAdmin):
    list_display= ['id','title','brands']


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'comment', 'testimos']
     

class ContactMessageAdmin(admin.ModelAdmin):
    list_display=('name','email', 'subject','message','status', 'note')
    readonly_fields = ('name', 'subject','email', 'message')
    list_filter= ['status']
    list_display_links = ('status','name','note')
    search_fields = ('name','email', 'subject','message','status', 'note')
    list_per_page = 25

    
admin.site.register(Setting, SettingAdmin) 
admin.site.register(Brand, BrandAdmin)  
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
    
   
