from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class ExamCategory(models.Model):
    REGION_CHOICES = [
        ('INTERNATIONAL', 'International'),
        ('TURKEY', 'Turkey'),
    ]
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    region = models.CharField(max_length=20, choices=REGION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Exam Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class ExamResource(models.Model):
    DIFFICULTY_CHOICES = [
        ('EASY', 'Easy'),
        ('MEDIUM', 'Medium'),
        ('HARD', 'Hard'),
    ]
    EXAM_TYPE_CHOICES = [
        ('FULL_TEST', 'Full Test'),
        ('SECTION', 'Section'),
        ('MINI_QUIZ', 'Mini Quiz'),
    ]

    title = models.CharField(max_length=255)
    category = models.ForeignKey(ExamCategory, on_delete=models.CASCADE, related_name='resources')
    source_name = models.CharField(max_length=100)
    url = models.URLField()
    description = models.TextField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    exam_type = models.CharField(max_length=20, choices=EXAM_TYPE_CHOICES)
    subject = models.CharField(max_length=100)
    is_free = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    target_exam = models.ForeignKey(ExamCategory, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} profile'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()


class SavedResource(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_resources')
    resource = models.ForeignKey(ExamResource, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'resource')
        ordering = ['-saved_at']

    def __str__(self):
        return f'{self.user.username} - {self.resource.title}'


class SearchLog(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    query = models.TextField()
    results_count = models.IntegerField(default=0)
    searched_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-searched_at']

    def __str__(self):
        return f'"{self.query}" ({self.results_count} results)'
