from django.db import models

# Create your models here.
class Feature(models.Model):

    
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)

    """
    #_id = 0
    
    def __init__(self, name: str, description: str, isEnabled: bool = True):
        
        Feature._id += 1
        self.id = Feature._id
        self.name = name
        self.description = description
        self.isEnabled = isEnabled
        
        self.name = models.CharField(max_length=100)
        self.description = models.CharField(max_length=500)

    
    def switchFeatureState(self, isEnabled: bool):
        self.isEnabled = isEnabled
    
    def updateFeatureDetails(self, name: str, description: str):
        self.name = name
        self.description = description

    
    def __del__(self):
        Feature._id -= 1
    """