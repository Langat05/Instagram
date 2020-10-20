from django.db import models

# Create your models here.

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='images/')
    bio = models.CharField(max_length=100,blank=True)
    user = models.ForeignKey(User,blank=True, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return self.bio

    #Save profile
    def profile_save(self):
        self.save()

     #delete profile
    def delete_profile(self):
        self.delete()

class Image(models.Model):
    time_created= models.DateTimeField(default=datetime.now, blank=True)
    image=models.ImageField(upload_to='images/')
    message = models.CharField(max_length=80, blank=True)
    name = models.CharField(max_length=80)
    caption = models.TextField(blank=True)
    profile = models.ForeignKey(User, blank=True,on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    #Save image
    def save_image(self):
        self.save()

    #Delete image
    def delete_image(self):
        self.delete()        