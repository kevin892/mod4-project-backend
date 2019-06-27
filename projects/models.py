from django.db import models

class User(models.Model):
    username = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.username


class Project(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="projects")
    title = models.CharField(max_length=100)
    json_url = models.CharField(max_length=250)
    app_url = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
