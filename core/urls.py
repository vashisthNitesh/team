from django.urls import path

from .views import TeamListView, TeamMemberDetailView

app_name = 'core'

urlpatterns = [
    path('', TeamListView.as_view(), name='member-list'),
    path('<slug:slug>/', TeamMemberDetailView.as_view(), name='detail'),
]
