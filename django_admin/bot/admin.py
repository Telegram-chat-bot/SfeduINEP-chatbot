from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import *

class Admin_sort(AdminSite):
    def get_app_list(self, request):
        app_dict = self._build_app_dict(request)
        return sorted(app_dict.values(), key=lambda x: x['name'].lower())
    
admin.site = Admin_sort()

admin.site.register(Admission)
admin.site.register(About)
admin.site.register(Passing_scores)
admin.site.register(Num_places)
admin.site.register(Directions)
admin.site.register(Questions)
admin.site.register(Welcome_message)
admin.site.register(ChatID)