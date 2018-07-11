from django.contrib import admin

from pm.models import (Project, ProjectCategory, ProjectPhoto, Slideshow)


class ProjectPhotoInline(admin.StackedInline):
    model = ProjectPhoto
    extra = 0
    readonly_fields = ('image_tag',)


class ProjectAdmin(admin.ModelAdmin):
    model = Project

    inlines = [ProjectPhotoInline,]

    fields = ['name', 'description', 'engineer', 'owner', 'location', 'cost', 'status', 'categories',]


class ProjectPhotoAdmin(admin.ModelAdmin):
    model = ProjectPhoto

    fields = ( 'project', 'title', 'photo', 'image_tag', )
    readonly_fields = ('image_tag',)

class SlideshowAdmin(admin.ModelAdmin):
    model = Slideshow


class ProjectCategoryAdmin(admin.ModelAdmin):
    model = ProjectCategory


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectPhoto, ProjectPhotoAdmin)
admin.site.register(ProjectCategory, ProjectCategoryAdmin)
admin.site.register(Slideshow, SlideshowAdmin)
