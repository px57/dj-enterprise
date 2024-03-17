from django.db import models
from kernel.models.base_metadata_model import BaseMetadataModel
# from profiles.models import Profile

class EnterpriseRoleListModel(BaseMetadataModel):
    """
    Enterprise role list model
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Enterprise role list'
        verbose_name_plural = 'Enterprise role lists'
        db_table = 'enterprise_role_list'
        ordering = ['name']

class EnterpriseModel(BaseMetadataModel):
    """
    Enterprise model
    """

    name = models.CharField(max_length=255)
    employee_count = models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Enterprise'
        verbose_name_plural = 'Enterprises'
        db_table = 'enterprise'
        ordering = ['name']

class EmployeeRoleModel(BaseMetadataModel):
    """
    Employee role model
    """
    profile = models.ForeignKey(
        'profiles.Profile',
        on_delete=models.CASCADE,
                
    )

    enterprise = models.ForeignKey(
        EnterpriseModel, 
        on_delete=models.CASCADE
    )

    role = models.ForeignKey(
        EnterpriseRoleListModel, 
        on_delete=models.CASCADE
    )