from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

def userprofile(request, username):
    user = get_object_or_404(User, username=username)

    number_of_votes = 0

    for feed in user.feeds.all():
        number_of_votes = number_of_votes + (feed.number_of_votes - 1)
    
    return render(request, 'userprofile/userprofile.html', {'user': user, 'number_of_votes': number_of_votes})

def votes(request, username):
    user = get_object_or_404(User, username=username)
    votes = user.votes.all()

    feeds = []

    for vote in votes:
        feeds.append(vote.feed)
    
    return render(request, 'userprofile/votes.html', {'user': user, 'feeds': feeds})

def submissions(request, username):
    user = get_object_or_404(User, username=username)

    feeds = user.feeds.all()

    return render(request, 'userprofile/submissions.html', {'user': user, 'feeds': feeds})