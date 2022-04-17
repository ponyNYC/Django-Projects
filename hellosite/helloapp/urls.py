from django.urls import path
from helloapp.views import HelloWorldView, HelloView, GoodbyeView

urlpatterns = [
    # helloapp/
    path('', HelloWorldView.as_view(), name='hello_world'),
    path('<name>', HelloView.as_view(), name='hello_name'),
    path('goodbye/<name>', GoodbyeView.as_view(), name='goodbye'),
    
]