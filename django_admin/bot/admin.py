from django.contrib import admin

from .models import About, Admission, Passing_scores, Num_places, Directions, Questions

admin.site.register(Admission)
admin.site.register(About)
admin.site.register(Passing_scores)
admin.site.register(Num_places)
admin.site.register(Directions)
admin.site.register(Questions)