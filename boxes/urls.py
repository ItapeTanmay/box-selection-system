from django.urls import path
from .views import recommend_box_api, order_ui_view

urlpatterns = [
    path('api/recommend-box/', recommend_box_api, name='recommend_box_api'),
    path('select-box/', order_ui_view, name='order_ui_view'),
]