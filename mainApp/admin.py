from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Faculty,StudentAchiev,Review,Album,Photo
# Register your models here.
admin.register(Faculty)(admin.ModelAdmin)

admin.register(StudentAchiev)(admin.ModelAdmin)

admin.register(Review)(admin.ModelAdmin)
admin.register(Album)(admin.ModelAdmin)
admin.register(Photo)(admin.ModelAdmin)