from django.contrib import admin

from .models import *


class DirectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'time_create']
    
    
admin.site.register(Admission)
admin.site.register(About)
admin.site.register(Passing_scores)
admin.site.register(Num_places)
admin.site.register(Directions)
admin.site.register(Questions, DirectionAdmin)
admin.site.register(Welcome_message)