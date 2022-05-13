from django.contrib import admin

from .models import *

admin.site.register(Admission)
admin.site.register(About)
admin.site.register(Passing_scores)
admin.site.register(Num_places)
admin.site.register(Directions)
admin.site.register(Questions)
admin.site.register(Welcome_message)
admin.site.register(Help_content)
admin.site.register(OpenDay)

#
# class InfoInline(admin.TabularInline):
#     extra = 1
#     model = InfoPage
#
#
# class PageModel(admin.ModelAdmin):
#     inlines = [InfoInline]
#     list_display = ["page_title", "row"]
#
#
# admin.site.register(Page, PageModel)
