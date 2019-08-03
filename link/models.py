from django.db import models
from django.utils.translation import gettext_lazy as _

class Link(models.Model):
    label = models.CharField(_('label'), max_length=100)
    name = models.CharField(_('name'), max_length=50)
    image = models.ImageField(_('image'),
            upload_to='uploads/link/%Y%m/%d/',
            blank=True, null=True)
    path = models.CharField(_('path'), max_length=200, blank=True, null=True)
    sort = models.PositiveSmallIntegerField(_('sort'), default=0)
    is_active = models.BooleanField(_('is active'), default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['label', 'sort']
        verbose_name = _('link')
        verbose_name_plural = _('link')
