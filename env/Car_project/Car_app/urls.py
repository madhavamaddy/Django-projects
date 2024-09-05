from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('fruits',views.fruits,name="fruits_page"),
    path('movies',views.videos,name="movies_page")
]
