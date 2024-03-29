from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('notes/', views.notes, name="notes"),
    path('delete_note/<int:pk>', views.delete_note, name="delete-note"),
    path('notes_detail/<int:pk>', views.NotesDetailView.as_view(), name="notes-detail"),
    path('dsa/', views.dsa, name="dsa"),
    path('update_dsa/<int:pk>', views.update_dsa, name = "update-dsa"),
    path('delete_dsa/<int:pk>', views.delete_dsa, name="delete-dsa"),
    path('youtube/', views.youtube, name="youtube"),
    path('todo/', views.todo, name="todo"),
    path('update_todo/<int:pk>', views.update_todo, name = "update-todo"),
    path('delete_todo/<int:pk>', views.delete_todo, name = "delete-todo"),
    path('books/', views.books, name="books"),
    path('dictionary/', views.dictionary, name="dictionary"),
    path('wiki/', views.wiki, name="wiki"),
    path('conversion/', views.conversion, name="conversion"),
    path('profile/', views.profile, name="profile"),
]
