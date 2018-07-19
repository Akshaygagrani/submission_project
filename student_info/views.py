from django.shortcuts import render, get_object_or_404, redirect
from .models import info
from .forms import add_student
# Create your views here.
def welcome(request):
    return render(request, 'student_info/info.html', {})

def details(request):
    detail = info.objects.all()
    return render(request, 'student_info/detail.html', {'detail':detail}) # dictionary links the keyword detail to detail i.e our database

def deep(request, pk):
    deep_info = info.objects.get(pk=pk)
    return render(request, 'student_info/deep_detail.html', {'deep_info':deep_info})

def add(request):
    if request.method == 'POST':
        add_form = add_student(request.POST)
        if add_form.is_valid:
            deep_info = add_form.save()
            deep_info.save()
            return redirect('details')
            return redirect('post_detail', pk=post.pk)
    else:
        add_form = add_student()
    return render(request, 'student_info/add_me.html', {'add_form':add_form})
