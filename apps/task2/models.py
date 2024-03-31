from django.db import models

# Create your models here.


class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    requirements = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'
        db_table = 'vacancy'

    def __str__(self):
        return self.title
