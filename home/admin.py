from django.contrib import admin
from home import models

# Register your models here.
admin.site.register(models.IndexPage)
admin.site.register(models.ProjectPage)
admin.site.register(models.AboutPage)
admin.site.register(models.Podcast)
