from django.contrib import admin

from assignments.models import About, SocialLink

# Register your models here.
class aboutadmin(admin.ModelAdmin):
    def has_add_permission(self,request):
        count=About.objects.all().count()
        if count==0:
            return True
        return False

admin.site.register(About,aboutadmin)
admin.site.register(SocialLink)