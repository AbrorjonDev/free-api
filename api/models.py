from django.db import models

# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    faculty = models.CharField(max_length=100, null=True)
    group = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ('id',)


    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
        

    def __str__(self):
        return self.full_name