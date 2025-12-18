from django.apps import AppConfig
from cloudinary.models import CloudinaryField

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
