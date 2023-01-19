from django.urls import path

from appfiles.views import FileListView, model_form_upload, FileDetailView, FilesUpdateView, FilesDeleteView, about

urlpatterns = [
    path('list/', FileListView.as_view(), name='list'),
    path('detail/<int:pk>/', FileDetailView.as_view(), name='detail'),
    path('list/<int:pk>/update/', FilesUpdateView.as_view(), name='update'),
    path('list/<int:pk>/delete/', FilesDeleteView.as_view(), name='delete'),
    path('create/', model_form_upload, name='create'),
     path('about/', about, name='about'),

]