from .views import home, add_emp, update_emp, delete_emp
from django.urls import path, include

urlpatterns = [
    path("home/", home, name='home'),
    path("add-emp/", add_emp, name='add_emp'),
    path("update-emp/<int:emp_id>", update_emp, name='update_emp'),
    path("delete-emp/<int:emp_id>",delete_emp, name='delete_emp'),
]
