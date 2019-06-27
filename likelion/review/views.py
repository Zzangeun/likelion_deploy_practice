from django.shortcuts import render, get_object_or_404, redirect
from .models import Review, Comment
from django.utils import timezone
from .forms import ReviewForm, CommentForm
# Create your views here.

def home(request):
    reviews = Review.objects
    return render(request, 'review/home.html', {'reviews':reviews})

def detail(request, review_id):
    review_detail = get_object_or_404(Review, pk = review_id)
    form = CommentForm()
    return render(request, 'review/detail.html', {'review':review_detail, 'form':form,})

def review_new(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return redirect('detail', review_id=review.pk)
    else:
        form = ReviewForm()
    return render(request, 'review/new.html', {'form':form})

def review_edit(request, review_id):
    review = get_object_or_404(Review, pk = review_id)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return redirect('detail', review_id=review.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'review/edit.html', {'form':form})

def review_delete(request, review_id):
    review = get_object_or_404(Review, pk = review_id)
    review.delete()
    return redirect('home')

def add_comment(request, review_id):
    review = get_object_or_404(Review, pk = review_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.review = review
            comment.save()
    return redirect('detail', review_id=review.pk)

def delete_comment(request, review_id):
    comment = get_object_or_404(Comment, pk = comment_id)
    review = comment.review
    comment.delete()
    return redirect('detail', review_id=review.id)