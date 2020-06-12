from django.shortcuts import render
from .models import Job

# Create your views here.


def job_list(request):
    job_list = Job.objects.all()

    context = {'jobs': page_obj}  # template name
    return render(request, 'job/job_list.html', context)


def job_detail(request, id):
    pass
# job_detail = Job.objects.get(slug=slug)

# if request.method=='POST':
#     form = ApplyForm(request.POST , request.FILES)
#     if form.is_valid():
#         myform = form.save(commit=False)
#         myform.job = job_detail
#         myform.save()
#         print('DOne')

# else:
#     form = ApplyForm()

# context = {'job' : job_detail , 'form1':form}
# return render(request,'job/job_detail.html',context)
