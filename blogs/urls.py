from django.urls import include, path
# from .views import  TodoGetUpdateDelete, TodoListCreate, home
# from .views import  home
from rest_framework import routers

from .views import BlogView, CategoryView, comment_list, like
# from .views import BlogView, CategoryView, CommentView, like

router = routers.DefaultRouter()
#default router da apiroot var prefix yazmadan çalıştırırsak apirootu veriyor
router.register('blogs', BlogView)
router.register('categories', CategoryView)
# router.register('comments', CommentView)



urlpatterns = [
    path("", include(router.urls)),
    path("likes/<int:pk>/", like, name="like"),
    path("comments/<int:pk>/", comment_list, name="comment_list"),
]
