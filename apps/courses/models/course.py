from django.db import models
from django.conf import settings
from .category import Category

class Course(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="owned_courses")
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    overview = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through='CourseCategory',related_name="courses")

    class Meta:
        ordering = ["-created_at"] # forma descendente a su fecha de creación

    def __str__(self):
        return self.title

#tabla intermedia: solo conecta cuando la relacion es muchos a muchos
#cada fila solo es un elnace entre course y category
class CourseCategory(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # un curso no deberia ser asignado dos veces en la misma categoria. Si esta permitido varias categorias de cursos pero sin duplicados
    class Meta: 
        unique_together = ('course', 'category') 


    def __str__(self):
        return f'{self.course} - {self.category}'
    