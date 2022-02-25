from . import views
from django.urls import path


urlpatterns = [
    path('list/', views.BookView.as_view({"get": "list", "post": "create"})),
]
