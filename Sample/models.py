from random import choice, choices
from django.db import models


# This table stores all the information about a process
class processInfo(models.Model): 

    processID = models.AutoField(primary_key = True) 
    processName = models.CharField(max_length=60)
    processDescription = models.TextField()
    processType = models.CharField(choices= (("Integration","Integration" ), ("Application", "Application"), ("Dashboard", "Dashboard")), max_length=20)

    def __str__(self):
        return self.processName


# This table stores all the information about the data elements (configuration parameters) for the processes
class processElements(models.Model): 
    processElementID = models.AutoField(primary_key = True)
    processID = models.ForeignKey(processInfo, on_delete=models.CASCADE)
    elementName = models.CharField(max_length=60)
    elementValue = models.CharField(max_length=20)

    def __str__(self):
        return str(self.elementName)

# This table stores data about the groups 
class groupInfo(models.Model):
    groupID = models.AutoField(primary_key=True)
    groupName = models.CharField(max_length=30)

    
    def __str__(self):
        return str(self.groupName)

class processAccessInfo(models.Model):
    processID = models.ForeignKey(processInfo, on_delete=models.CASCADE)
    groupID = models.ForeignKey(groupInfo, on_delete=models.CASCADE) 

    def __str__(self):
        return str(self.processID)


class processUpdateLog(models.Model):
    ID = models.AutoField(primary_key=True)
    processID = models.ForeignKey(processInfo, on_delete=models.CASCADE)
    userID = models.CharField(max_length=30)
    groupID = models.ForeignKey(groupInfo, on_delete=models.CASCADE)
    processElementID = models.ForeignKey(processElements, on_delete=models.CASCADE)
    valueBefore = models.CharField(max_length=30)
    valueAfter = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.ID)



    
class scheduledUpdatesInfo(models.Model):
    ID = models.AutoField(primary_key=True)
    processID = models.ForeignKey(processInfo, on_delete=models.CASCADE)
    userID = models.CharField(max_length=30)
    groupID = models.ForeignKey(groupInfo, on_delete=models.CASCADE)
    processElementID = models.ForeignKey(processElements, on_delete=models.CASCADE)
    valueBefore = models.CharField(max_length=30)
    valueAfter = models.CharField(max_length=30)
    dateScheduled = models.DateField()

    def __str__(self):
        return str(self.ID)



