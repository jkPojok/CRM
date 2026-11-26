from django.contrib import admin
from django.urls import path
from crm.views import DoctorRetrieveUpdateView
from crm.views import DoctorListCreateView
from crm.views import PatientListCreateView
from crm.views import PatientRetrieveUpdateView
from crm.views import AppointmentListCreateView
from crm.views import AppointmentRetrieveUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/doctors', DoctorListCreateView.as_view()),
    path('api/v1/doctors/<int:pk>', DoctorRetrieveUpdateView.as_view()),
    path('api/v1/patients', PatientListCreateView.as_view()),
    path('api/v1/patients/<int:pk>', PatientRetrieveUpdateView.as_view()),
    path('api/v1/appointments', AppointmentListCreateView.as_view()),
    path('api/v1/appointments/<int:pk>', AppointmentRetrieveUpdateView.as_view()),
]
