from django.shortcuts import render, redirect
from core.repository.postgres import filter_users, create_user
from core.forms.user_form import UserForm

def user_list(request):
    query = request.GET.get('q')
    users = filter_users(query)

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            create_user(form.cleaned_data)
            return redirect('user_list')
    else:
        form = UserForm()

    return render(request, "users.html", {"users": users, "form": form, "query": query})
