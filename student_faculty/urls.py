"""URLs for Student and Faculty pages."""
from django.urls import path
# from login.views import LoginViewSet

urlpatterns = [
    path('student', ),
    path('student/apply', ),
    path('student/update_details', ),
    path('faculty', ),
    path('faculty/add_course', ),
    path('faculty/update_details', ),
]
