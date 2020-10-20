from django.shortcuts import render, redirect

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    current_user = request.user
    all_images = Image.objects.all()
    comments = Comment.objects.all()
    likes = Likes.objects.all
    profile = Profile.objects.all()
    return render(request,'index.html',locals())