from django.db import models
from .module import Module
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

class ItemBase(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_name' , on_delete=models.CASCADE) # el nombre es dinamico y varia dependiendo de la clase que lo hereda
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # las hijas son las que van a crear la tabla, la tabla del padre no se crea

    def __str__(self):
        return self.title

class Text(ItemBase):
    content = models.TextField()

class File(ItemBase):
    file = models.FileField( upload_to='files')

class Image(ItemBase):
    file = models.FileField(upload_to='images')

class Video(ItemBase):
    url = models.URLField()



class Content(models.Model):
    modules = models.ForeignKey(Module, related_name="contents", on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={
        'model__in': ('text', 'video', 'image', 'file' )
    })
    #trae la referencia de los modelos registrados en django
    object_id = models.IntegerField()#guardar el object ID 
    # Asi aseguramos que podamos tener diferentes tipos de datos
    item = GenericForeignKey('content_type', 'object_id') #EJ: una imagen(content type) con el ID 3 (object_id)

