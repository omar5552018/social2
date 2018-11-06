from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from friend.models import Friend
from django.contrib.auth.decorators import login_required


@login_required
def home (request):
    user = request.user
    user_friend_model = Friend.objects.get(user=user)
    friends = user_friend_model.friends.all()


    args = dict(friends=friends)
    return render(request, 'homePage/homePage.html', args)
