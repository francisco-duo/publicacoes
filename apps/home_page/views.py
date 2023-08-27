from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# from allauth.account.models import EmailAddress


@login_required
def index(request, user_id):
    user = User.objects.get(id=user_id)

    return render(request, 'app/pages/index.html', {
        'user': user
    })
