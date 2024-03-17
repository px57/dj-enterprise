from django.contrib import admin
from enterprise.models import EnterpriseRoleListModel, EnterpriseModel, EmployeeRoleModel

class EmployeeRoleModelInline(admin.TabularInline):
    model = EmployeeRoleModel
    extra = 1
    fields = [
    
    ]
    readonly_fields = [
    ]

@admin.register(EnterpriseRoleListModel)
class EnterpriseRoleListModelAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]

@admin.register(EnterpriseModel)
class EnterpriseModelAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'employee_count',
    ]

@admin.register(EmployeeRoleModel)
class EmployeeRoleModelAdmin(admin.ModelAdmin):
    list_display = [
        'profile',
        'enterprise',
        'role',
    ]