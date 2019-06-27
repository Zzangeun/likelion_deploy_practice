from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('detail/<int:review_id>/', views.detail, name = 'detail'),
    path('detail/new/', views.review_new, name = 'new'),
    path('detail/<int:review_id>/edit/', views.review_edit, name = 'edit'),
    path('detail/<int:review_id>/delete/', views.review_delete, name = 'delete'),
    path('detail/<int:review_id>/comment/', views.add_comment, name = 'add_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name = 'delete_comment'),
]
