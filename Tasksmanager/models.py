from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user_auth = models.OneToOneField(User, primary_key=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="Name")
    login = models.CharField(max_length=25, verbose_name="Username")
    password = models.CharField(max_length=100, verbose_name="Password")
    phone = models.CharField(max_length=20, verbose_name="Phone Number", null=True, default=None, blank=True)
    born_date = models.DateField(verbose_name="Born Date", null=True, default=None, blank=True)
    last_connection = models.DateTimeField(verbose_name="Date Of Last Connection", null=True, default=None, blank=True)
    email = models.EmailField(verbose_name="Email")
    years_seniority = models.IntegerField(verbose_name="Seniority", default=0)
    date_created = models.DateTimeField(verbose_name="Date Of birthday", auto_now_add=True)


    def __str__(self):
        return self.user_auth.username


class Project(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title")
    description = models.CharField(max_length=1000, verbose_name="Description")
    client_name = models.CharField(max_length=1000, verbose_name="Client Name")
    def __str__(self):
        return self.title

# this class defines a staff/user who is a supervisor , he or she inherits all attributes from the userprofile model
class Supervisor(UserProfile):
    specialization = models.CharField(max_length=50, verbose_name="Specialization")


# this class defines a staff/user who is not a supervisor , he also inherits some attributes from the userprofile model
class Developer(UserProfile):
    supervisor = models.ForeignKey(Supervisor, verbose_name="Supervisor")

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title")
    description = models.CharField(max_length=1000, verbose_name="Description")
    time_elasped = models.IntegerField(verbose_name="Elapsed Time", default=None, null=True, blank=True)
    importance = models.IntegerField(verbose_name="Importance")
    project = models.ForeignKey(Project, verbose_name="Project", null=True, default=None, blank=True)
    developers = models.ManyToManyField(Developer,verbose_name="Second Developer", related_name="dev1")


    def __str__(self):
        return self.title + '' + str(self.project)

    class Meta:
        verbose_name = "task"
        verbose_name_plural = "tasks"
    

class DeveloperWorkTask(models.Model):
    developer = models.ForeignKey(Developer, verbose_name="Developer")
    task = models.ForeignKey(Task, verbose_name="Task")
    time_elasped_dev = models.IntegerField(verbose_name="Time Elasped", null=True, default=None, blank=True)
