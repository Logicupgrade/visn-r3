from unicodedata import name
from django.urls import include,path
from . import views
# from .views import CustomLoginView

urlpatterns = [
    # path('login/', CustomLoginView.as_view(), name='login'),
    path('', views.dashboardView, name='dashboard'),
    path('project_view/<int:project_id>/', views.projectView, name='project_view'),
    # path('chat/', include('chat.urls', namespace='chat')),
]