from django.shortcuts import render

# Create your views here.
from django.views import View

# Create your views here.
class HelloWorldView(View):
    def get(self, request):
        return render(request=request, template_name='hello_world.html')

class HelloView(View):
    def get(self, request, name='world'):
        context = {'name': name}
        return render(
            request=request, template_name='hello_name.html', context=context,
        )

class GoodbyeView(View):
    def get(self, request, name='Django'):
        context = {'name': name}
        return render(
            request=request, template_name='goodbye.html', context=context,
        )
