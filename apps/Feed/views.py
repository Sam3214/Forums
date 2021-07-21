import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import FeedForm, DiscussionForm,DiscussionForm2
from .models import Feed, Vote, Discussion,Discussion2

def frontpage(request):
    feeds = Feed.objects.all()[0:200]
    return render(request, 'feed/frontpage.html', {'feeds': feeds})

def search(request):
    query = request.GET.get('query', '')
    if len(query) > 0:
        feeds = Feed.objects.filter(title__icontains=query)
    else:
        feeds = []
    return render(request, 'feed/search.html', {'feeds': feeds, 'query': query})

def feed(request, feed_id):
    feed = get_object_or_404(Feed, pk=feed_id)
    if request.method == 'POST':
        fform =DiscussionForm(request.POST)
        aform =DiscussionForm2(request.POST)
        if fform.is_valid() and 'fform' in request.POST:
            discussion = fform.save(commit=False)
            discussion.feed = feed
            discussion.created_by = request.user
            discussion.save()
        elif aform.is_valid() and 'aform' in request.POST:    
            discussion2 = aform.save(commit=False)
            discussion2.feed = feed
            discussion2.created_by = request.user
            discussion2.save()
            return redirect('feed', feed_id=feed_id)
    else:
        fform = DiscussionForm()   
        aform =DiscussionForm2()
    return render(request, 'feed/detail.html', {'feed': feed, 'fform': fform,'aform':aform})

def newest(request):
    date_from = datetime.datetime.now() - datetime.timedelta(days=1)
    feeds = feeds = Feed.objects.all().order_by('-number_of_votes')[0:30]
    return render(request, 'feed/newest.html', {'feeds': feeds})

@login_required
def vote(request, feed_id):
    feed = get_object_or_404(Feed, pk=feed_id)
    next_page = request.GET.get('next_page', '')
    if feed.created_by != request.user and not Vote.objects.filter(created_by=request.user, feed=feed):
        vote = Vote.objects.create(feed=feed, created_by=request.user)
    if next_page == 'feed':
        return redirect('feed', feed_id=feed_id)
    else:
        return redirect('frontpage')

@login_required
def submit(request):
    if request.method == 'POST':
        form = FeedForm(request.POST)
        if form.is_valid():
            feed = form.save(commit=False)
            feed.created_by = request.user
            feed.save()
            return redirect('frontpage')
    else:
        form = FeedForm()
    return render(request, 'feed/submit.html', {'form': form})