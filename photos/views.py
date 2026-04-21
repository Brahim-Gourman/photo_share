from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Photo, Like, Comment

@login_required
def feed(request):
    photos = Photo.objects.all().order_by('-created_at')
    liked_photos = Like.objects.filter(user=request.user).values_list('photo_id', flat=True)
    return render(request, 'photos/feed.html', {
        'photos': photos,
        'liked_photos': liked_photos
    })

@login_required
def upload_photo(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        caption = request.POST.get('caption')
        Photo.objects.create(user=request.user, image=image, caption=caption)
        return redirect('feed')
    return render(request, 'photos/upload.html')

@login_required
def like_photo(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    like, created = Like.objects.get_or_create(user=request.user, photo=photo)
    if not created:
        like.delete()
    return redirect('feed')

@login_required
def add_comment(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Comment.objects.create(user=request.user, photo=photo, text=text)
    return redirect('feed')

@login_required
def delete_photo(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id, user=request.user)
    photo.delete()
    return redirect('feed')