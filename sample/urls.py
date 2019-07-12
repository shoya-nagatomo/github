from django.urls import path
from . import views

app_name = 'sample'

urlpatterns = [
    # トップ画面
    path('', views.IndexView.as_view(), name='index'),

    # 詳細画面
    path('sample/<int:pk>/', views.DetailView.as_view(), name='detail'),

    # Ajax処理
    path("sample/<int:pk>/exec/", views.exec_ajax, name='exec'),
]