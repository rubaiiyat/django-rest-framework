from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import Blogs, Comments, Employee

router=DefaultRouter()
router.register('employee',Employee)
router.register('blogs',Blogs)
router.register('comments',Comments)

urlpatterns = [
    path('',include(router.urls)),
]


