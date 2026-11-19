
from django.contrib import admin

from apps.courses.models import Progress
from apps.courses.models.category import Category
from apps.courses.models.course import Course, CourseCategory
from apps.courses.models.enrollment import Enrollment
from apps.courses.models.module import Module
from apps.courses.models.review import Review

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('name',)}
    list_display = ('name', 'slug')
    search_fields = ('name',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(CourseCategory)
class CourseGategory(admin.ModelAdmin):
    list_display = ['course', 'category']
    list_filter = ['category']
    search_fields = ['course__title'] #con doble guion bajo accedemos a atributos del curso    

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['title', 'course']
    list_filter = ['title', 'course__title']

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'enrolled_at')
    list_filter = ('course', 'enrolled_at')
    search_fields = ('user__username', 'course__title')

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'progress', 'status', 'updated_at')
    list_filter = ('status',)
    search_fields = ('user__username', 'course__title')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('user__username', 'course__title', 'comment')