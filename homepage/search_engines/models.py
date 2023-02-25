from django.db import models


class SearchEngine(models.Model):
    FORM_METHODS = (('get', 'GET'), ('post', 'POST'))
    name = models.CharField(max_length=100, unique=True)
    url = models.URLField(max_length=500, unique=True)
    form_action = models.CharField(max_length=200)
    form_method = models.CharField(max_length=4, choices=FORM_METHODS, default='get')
    name_attribute = models.CharField(max_length=100)
    icon = models.URLField(max_length=500, blank=True, null=True)
    is_default = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Search Engines'

    def __str__(self):
        return self.name
