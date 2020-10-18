from django.contrib import admin
from .models import Status, Personnel_information, request_position, Criterion, User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass

class StatusAdmin(admin.ModelAdmin):
    pass

class Personnel_informationAdmin(admin.ModelAdmin):
    pass

class request_positionAdmin(admin.ModelAdmin):
    pass

class CriterionAdmin(admin.ModelAdmin):
    pass

admin.site.register(User,UserAdmin)
admin.site.register(Status,StatusAdmin)
admin.site.register(Personnel_information,Personnel_informationAdmin)
admin.site.register(request_position,request_positionAdmin)
admin.site.register(Criterion,CriterionAdmin)

