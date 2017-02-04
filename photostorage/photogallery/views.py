from django.shortcuts import render, redirect
from django.utils import timezone
#from django.http import HttpResponse
#from django.template.loader import get_template
#from django.template import Context
#from django.shortcuts import render_to_response
from .models import *
from .forms import AddForm, AddComment

# Create your views here.

def gallery_home(request):
  image_list = picture.objects.order_by('-pic_date')
  return render(request, 'picture_list.html', {'pictures': image_list})

def pic_detail(request, pk):
  pic = picture.objects.get(pk=pk)
  comm = comment.objects.filter(comment_pic=pk)
  if request.POST:
    form_comment = AddComment(request.POST)
    if form_comment.is_valid():
      comm = form_comment.save(commit=False)
      comm.comment_pic = pic
      comm.comment_date = timezone.now()
      human = True
      comm.save()
      return redirect('pic_detail', pk=pic.pk)
  else:
    form_comment = AddComment(auto_id=False)
  return render(request, 'pic_detail.html', {'pic': pic, 'comments': comm, 'form_comment': form_comment})

def pic_upload(request):
  if request.POST:
    form_upload = AddForm(request.POST, request.FILES)
    if form_upload.is_valid():
      picture = form_upload.save(commit=False)
      picture.pic_date = timezone.now()
      human = True
      picture.save()
      return redirect('pic_detail', pk=picture.pk)
  else:
    form_upload = AddForm()
  return render(request, 'pic_upload.html', {'form_upload': form_upload}) 