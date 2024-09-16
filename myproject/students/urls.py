from django.urls import path
from . import views
urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('create/',views.student_create, name='studnet_list'),
    path('update/<int:id>/', views.student_update, name='student_update'),
    path('delete/<int:id>/', views.student_delete, name='student_delete'),
    #path('contact/',views.contact),
    #path('profile/',views.profile)
    #path('std/', include('students.urls'))

]