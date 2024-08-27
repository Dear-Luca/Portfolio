from django.contrib import admin
from .models import Tag, Project, ProjectImage, ProjectVideo

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectVideoInline(admin.TabularInline):
    model = ProjectVideo

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title","link",)
    inlines = [ProjectImageInline, ProjectVideoInline]
    search_fields = ("title","description",)
    list_filter = ("tags",)

class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
admin.site.register(ProjectVideo)
