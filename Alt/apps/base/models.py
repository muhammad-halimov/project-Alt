from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=256, null=True)
    surname = models.CharField(max_length=256, null=True)
    email = models.EmailField(unique=True, null=True)
    login = models.CharField(max_length=256, null=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='avatars', default="avatar.svg")
    codeforce = models.CharField(max_length=256, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    DisplayFields = ['username', 'surname', 'login', 'email', 'avatar', 'created', 'updated', 'id']
    SearchableFields = ['id', 'username', 'surname', 'login', 'email', 'avatar', 'created', 'updated']
    FilterFields = ['created', 'updated']

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ['id', '-updated']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username or self.email


class Organization(models.Model):
    name = models.CharField(max_length=256, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    DisplayFields = [
        'name', 'created', 'updated', 'id'
    ]
    SearchableFields = [
        'id', 'name', 'created', 'updated',
    ]
    FilterFields = ['created', 'updated']

    class Meta:
        ordering = ['id', '-updated']
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'

    def __str__(self):
        return self.name


class Tasks(models.Model):
    name = models.CharField(max_length=256, null=True)
    time_limit = models.CharField(max_length=256, null=True, blank=True)
    memory_limit = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    entry = models.CharField(max_length=256, null=True, blank=True)
    output = models.CharField(max_length=256, null=True, blank=True)
    example_entry = models.CharField(max_length=256, null=True, blank=True)
    example_output = models.CharField(max_length=256, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    DisplayFields = [
        'name', 'time_limit', 'memory_limit', 'description', 'entry', 'output',
        'example_entry', 'example_output', 'created', 'updated', 'id'
    ]
    SearchableFields = [
        'id', 'name', 'description', 'created', 'updated',
    ]
    FilterFields = ['created', 'updated']

    class Meta:
        ordering = ['id', '-updated']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.name


class Competition(models.Model):
    name = models.CharField(max_length=256, null=True)
    tasks = models.ManyToManyField(Tasks, related_name='tasks', blank=True)
    description = models.TextField(null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    link = models.TextField(null=True, blank=True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    DisplayFields = [
        'name', 'description', 'organization', 'start_time', 'end_time', 'created', 'updated', 'id'
    ]
    SearchableFields = [
        'id', 'name', 'description', 'organization', 'start_time', 'end_time', 'created', 'updated',
    ]
    FilterFields = ['created', 'updated']

    class Meta:
        ordering = ['-start_time']
        verbose_name = 'Competition'
        verbose_name_plural = 'Competitions'

    def __str__(self):
        return self.name


class History(models.Model):
    text = models.TextField(null=True)
    competition = models.ForeignKey(Competition, on_delete=models.SET_NULL, null=True, blank=True)
    task = models.ForeignKey(Tasks, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    DisplayFields = [
        'text', 'task', 'competition', 'user', 'created', 'updated', 'id',
    ]
    SearchableFields = [
        'id', 'text', 'competition',  'task', 'user', 'created', 'updated',
    ]
    FilterFields = ['created', 'updated']

    class Meta:
        ordering = ['-updated']
        verbose_name = 'History'
        verbose_name_plural = 'History'

    def __str__(self):
        return self.text[:30]
