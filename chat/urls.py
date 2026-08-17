from django.urls import path
from .views import home, new_message, user_threads, new_message_initial, view_thread

app_name = "chat"

urlpatterns = [
    path("home", home, name="home"),
    path("<int:thread_id>/", view_thread, name="view_thread"),
    path("new_message/<int:thread_id>/", new_message, name="new_message"),
    path("new_message_initial/", new_message_initial, name="new_message_initial"),
    path("user_threads", user_threads, name="user_threads"),
]