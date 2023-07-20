from django.contrib import admin

from .models import *


class PerevalAdmin(admin.ModelAdmin):
    list_display = ('id', 'beauty_title', 'title', 'other_titles', 'add_time', 'user', 'coords', 'level', 'connect', 'status')

class CoordsAdmin(admin.ModelAdmin):
    list_display = ('id', 'latitude', 'longitude', 'height')


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('title_1', 'image_1', 'title_2', 'image_2', 'title_3', 'image_3')


class LevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'winter', 'summer', 'autumn', 'spring')

class UsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'fam', 'name', 'otc', 'phone')


admin.site.register(PerevalAdded, PerevalAdmin)
admin.site.register(Coords, CoordsAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Users, UsersAdmin)