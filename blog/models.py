from django.db import models

#Create a blog model
#title
#pub_date
#body
#image

#Add the blog app to the settings

#Create a migration

#Migrate

#Add to admin

class Blog(models.Model):
    title=models.CharField(max_length=255)
    pub_date=models.DateTimeField()
    body=models.TextField(max_length=500)
    image=models.ImageField(upload_to='images/')
