from django.contrib import admin
from managedb.models import  Department, Position, StatusLeave, Policy, Policytype

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'dep_name']
admin.site.register(Department, DepartmentAdmin)

class PositionAdmin(admin.ModelAdmin):
    list_display = ['id', 'pos_name']
admin.site.register(Position, PositionAdmin)

class PolicytypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'policy_name']
admin.site.register(Policytype, PolicytypeAdmin)

class StatusLeaveAdmin(admin.ModelAdmin):
    list_display = ['id', 'sta_name']
admin.site.register(StatusLeave, StatusLeaveAdmin)

class PolicyAdmin(admin.ModelAdmin):
    list_display = ['policy_name', 'dep_name', 'pos_name', 'numofleave']
admin.site.register(Policy, PolicyAdmin)
