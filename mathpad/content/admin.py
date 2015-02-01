from django.contrib import admin
from models import Problem, Solution

class ProblemAdmin(admin.ModelAdmin):
	pass

class SoultionAdmin(admin.ModelAdmin):
	pass

admin.site.register(Problem, ProblemAdmin)
admin.site.register(Solution, SoultionAdmin)