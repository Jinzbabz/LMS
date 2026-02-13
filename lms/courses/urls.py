from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('upload/', views.upload_notes, name='upload_notes'),
    path('my-notes/', views.note_list, name='note_list'),
]