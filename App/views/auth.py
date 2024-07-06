from django.shortcuts import render, HttpResponse, redirect
from App.forms import signUpForm, loginForm
from django.views import View
from django.contrib.auth import logout, login
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
# Create your views here.

# class signupView(View):
    # def get(self, request):   #request parameter should be the first parameter of your methods in class-based views, not self
    #     form = signUpForm()
    #     print('Response from Class Based')
    #     return render(request, 'signup.html', context={'form': form})


    # def post(self, request):
    #     if request.method == "POST":
    #         form = signUpForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('login') 
    #         else:
    #             return render(request, 'signup.html', context={'form': form})

class signupView(FormView):
    template_name = "signup.html"
    form_class = signUpForm
    success_url = '/login'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
# class loginView(View):
#     def get(self, request):
#         form = loginForm()
#         context = {'form':form}
#         return render(request, 'login.html', context=context)

#     def post(self, request):
#         form = loginForm(request = request, data = request.POST)
#         context = {'form':form}
#         if(form.is_valid()):
#             return redirect('/')
#         return render(request, 'login.html', context=context)
    
class loginView(FormView):
    template_name = "login.html"
    form_class = loginForm
    success_url = '/'

    def form_valid(self, form):
        login(self.request, form.cleaned_data)
        next_page = self.request.GET.get('next')
        if next_page:
            return redirect(next_page)
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

def logout_view(request):
    logout(request)
    return redirect('/')