from django.contrib import admin
from .models import Coursework, Project, Skill, WorkExperience, Education

class CourseworkAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'grade_received', 'order')
    ordering = ('order',)
    list_editable = ('order',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    ordering = ('order',)
    list_editable = ('order',)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    ordering = ('order',)
    list_editable = ('order',)

class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'order')
    ordering = ('order',)
    list_editable = ('order',)
    
# Ensure each model is only registered once
admin.site.register(Coursework, CourseworkAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(WorkExperience, WorkExperienceAdmin)
admin.site.register(Education)

# admin.py
#from django.contrib import admin
#from .models import Project, Coursework, WorkExperience  # Make sure to import the new model

#admin.site.register(WorkExperience)  # Register the new model
