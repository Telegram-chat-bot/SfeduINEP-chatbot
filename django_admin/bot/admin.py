from django.contrib import admin
from .models import *

admin.site.register(Welcome_message)
admin.site.register(Help_content)


class InfoInline(admin.StackedInline):
    extra = 0
    model = InfoPage


class InnerKeyboardInline(admin.StackedInline):
    extra = 0
    model = InnerKeyboard


class PageAdmin(admin.ModelAdmin):
    inlines = [InfoInline, InnerKeyboardInline]
    list_display = ["btn_title", "row"]
    list_editable = ["row"]


class NumPlacesInline(admin.StackedInline):
    extra = 0
    model = Num_places


class PassScoreInline(admin.StackedInline):
    extra = 0
    model = Passing_scores


class DirectionsAdmin(admin.ModelAdmin):
    inlines = [NumPlacesInline, PassScoreInline]


admin.site.register(Page, PageAdmin)
admin.site.register(Directions, DirectionsAdmin)
