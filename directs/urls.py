from django.urls import path
from directs import views
from directs.views import SendMessage, inbox
urlpatterns = [
    path('inbox/', inbox, name="mesage"),
    path('directs/<username>', views.Directs, name="directs"),
    path('send/', SendMessage, name="send-message"),
    path('new/', views.UserSearch, name="user-search"),
    path('new/<username>', views.NewMessage, name="new-message"),


]