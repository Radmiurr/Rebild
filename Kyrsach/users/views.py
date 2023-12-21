from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import NewUserForm, LoginUserForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("myapp:index")
    form = NewUserForm()
    context = {"form": form}
    return render(request, "users/register.html", context)

@login_required
def profile(request):
    if request.method == "POST":
        contact_number = request.POST.get("number")
        image = request.FILES["upload"]
        user = request.user
        profile = Profile(user=user, contact_number=contact_number, image=image)
        profile.save()
    return render(request, "users/profile.html")


def seller_profile(request, id):
    seller = User.objects.get(id=id)

    context = {
        'seller': seller
    }

    return render(request, 'users/sellerprofile.html', context)

# class LoginUser(LoginView):
#     form_class = LoginUserForm
#     template_name = 'women/login.html'

#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Авторизация")
#         return dict(list(context.items()) + list(c_def.items()))

#     def get_success_url(self):
#         return reverse_lazy('home')
# Create your views here.
