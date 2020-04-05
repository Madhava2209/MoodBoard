from django.contrib import admin
from MoodLog.models import *

# Register your models here.
admin.site.register(Mood)
admin.site.register(Action)
admin.site.register(MoodLog)