from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Image, Profile,Comment,Follow,Likes



# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    current_user = request.user
    all_images = Image.objects.all()
    comments = Comment.objects.all()
    likes = Likes.objects.all
    profile = Profile.objects.all()
    return render(request,'index.html',locals())

def search(request):
    profiles = User.objects.all()
    if 'username' in request.GET and request.GET['username']:
        search_term = request.GET.get('username')
        results = User.objects.filter(username__icontains=search_term)
        return render(request,'search.html',locals())
    return redirect(home)  

@login_required(login_url='/login')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile =form.save(commit=False)
            profile.user = current_user
            profile.save()
    else:
        form=ProfileForm()

    return render(request, 'profile/new_user.html', locals())

@login_required(login_url='/login')
def explore(request):
    images = Image.objects.all()
    all_profiles = Profile.objects.all()
    return render(request, 'explore.html',{'images': images,'all_profiles' : all_profiles })

@login_required(login_url='accounts/login/')
def add_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.profile = current_user
            add.save()
            return redirect('home')
    else:
        form = ImageForm()
    return render(request,'image.html',locals())

@login_required(login_url='/accounts/login/')
def display_profile(request, id):
    seekuser=User.objects.filter(id=id).first()
    profile = seekuser.profile
    images = Image.get_profile_images(id)

    users = User.objects.get(id=id)
    follower = len(Follow.objects.followers(users))
    following = len(Follow.objects.following(users))
    people=User.objects.all()
    pip_following=Follow.objects.following(request.user)

    return render(request,'profile/profile.html',locals())