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

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_notime(self):
        return self.pub_date.strftime('%b %e %Y')
