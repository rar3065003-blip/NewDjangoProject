from django.db import models

class Blog(models.Model):

    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    is_published = models.BooleanField(default=True)
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блоговая запись'
        verbose_name_plural = 'Блоговые записи'
