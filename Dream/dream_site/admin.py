from django.contrib import admin
from .models import Mentor, Mentee, Team, Admin
# Register your models here.

admin.site.register(Mentor)
admin.site.register(Mentee)
admin.site.register(Team)
admin.site.register(Admin)
