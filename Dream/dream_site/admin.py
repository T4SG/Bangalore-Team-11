from django.contrib import admin
from .models import Mentor, Mentee, Team, Admin, Meeting, Goal
# Register your models here.

admin.site.register(Mentor)
admin.site.register(Mentee)
admin.site.register(Team)
admin.site.register(Meeting)
admin.site.register(Goal)
admin.site.register(Admin)
