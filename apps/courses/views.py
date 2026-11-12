from django.shortcuts import render

# Create your views here.
def course_list(request):
    courses = [
        {
            'id': 1, 
            'level': 'Principiante', 
            'rating': 4.8,
            'course_title': 'Python: fundamentos hasta los detalles', 
            'instructor': 'Alison Walsh', 
            'course_image': 'images/curso_1.jpg', 
            'instructor_image': 'https://randomuser.me/api/portraits/women/68.jpg'
        },
        {
            'id': 2, 
            'level': 'Experto', 
            'rating': 3.8,
            'course_title': 'Hello world', 
            'instructor': 'Alison Torres', 
            'course_image': 'images/curso_1.jpg', 
            'instructor_image': 'https://randomuser.me/api/portraits/women/69.jpg'
        }
    ]
    return render(request, "courses/courses.html", {
        "courses": courses
    })

def course_detail(request):
    course = {
        'course_title': 'Django Aplicaciones',
        'course_link': 'course_lessons',
        'course_image': 'images/curso_1.jpg',
        'info_course': {
            'lessons': 79,
            'duration': 8,
            'instructor': 'Ricardo Cuéllar'
        },
        'course_content': [
            {
                'id': 1,
                'name': 'Introducción al curso',
                'lessons': [
                    {
                        'name': '¿Qué aprenderás en el curso?',
                        'type': 'video'
                    },
                    {
                        'name': 'Hello World',
                        'type': 'file'
                    }
                ]
            }
        ]
    }

    return render(request, "courses/course_detail.html", {
        "course": course
    })

def course_lessons(request):
    lesson = {
        'course_title': 'Django: Crea aplicaciones web robustas con Python',
        'course_progress': 30,
        'course_content': [
            {
                'id': 1,
                'name': 'Introducción al curso',
                'total_lessons': 6,
                'complete_lessons': 3,
                'lessons': [
                    {
                        'name': '¿Qué aprenderás en el curso?',
                        'type': 'video'
                    },
                    {
                        'name': 'Hello World',
                        'type': 'file'
                    }
                ]
            }
        ]
    }
    return render(request, "courses/course_lessons.html", {
        "lesson": lesson
    })