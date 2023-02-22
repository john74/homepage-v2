from django.db import models

from users.models import User


class BookmarkCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Bookmark Categories'

    def __str__(self):
        return self.name


class BookmarkSubCategory(models.Model):
    category = models.ForeignKey(BookmarkCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Bookmark Subcategories'

    def __str__(self):
        return f'{self.category} - {self.name}'


class Bookmark(models.Model):
    sub_category = models.ForeignKey(BookmarkSubCategory, blank=True, null=True, on_delete=models.CASCADE, default='Other')
    name = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=700, unique=True)
    icon = models.URLField(max_length=500, blank=True, null=True)
    is_shortcut = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Bookmarks'

    def __str__(self):
        return f'{self.sub_category} - {self.name}'