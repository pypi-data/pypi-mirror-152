from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class Config(AppConfig):
    name = "examples.cloudinary.collections"
    label = "cloudinary_collections"
    verbose_name = _("Collections")
