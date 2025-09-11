from django.shortcuts import render,redirect

from django.http import HttpResponseForbidden

from django.views.generic import View

from myapp.forms import AdminRegistrationForm,LoginForm,UploadForm,AnnouncementForm

from myapp.models import User,Dashboard,Announcements

from django.contrib.auth import authenticate,login,logout

from django.utils.dateparse import parse_date

from django.contrib.auth.decorators import login_required,user_passes_test



def is_admin_user(user):
    
    return user.is_authenticated and user.username == 'admin'

@login_required
@user_passes_test(is_admin_user)
def admin_dashboard_view(request):
    return render(request, 'admin_dashboard.html')

# # Ensure the fixed admin exists
# def ensure_admin_exists():
    
#     if not User.objects.filter(username='admin').exists():
        
#         User.objects.create_user(username='admin', password='admin123')


class AdminRegisterView(View):

    def get(self,request):

        form = AdminRegistrationForm

        return render(request,'Signup.html',{'form':form})
    
    def post(self,request):

        form =AdminRegistrationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')

            password = form.cleaned_data.get('password')

            User.objects.create_user(username=username,password=password)


        return render(request,'Signup.html',{'form':form})

        return redirect('login')
    
class LoginView(View):

    def get(self,request):

        # ensure_admin_exists()

        form = LoginForm

        return render(request,'Login.html',{'form':form})
    
    def post(self,request):

        form = LoginForm(request.POST)

        if form.is_valid():

            username = 'admin'

            password = form.cleaned_data.get('password')

            
            user_obj = authenticate(request,username=username,password=password)

            if user_obj is not None and user_obj.username == 'admin':

                login(request,user_obj)

                return redirect('admin_dashboard')
            
            else:
                return render(request, 'login.html', {
                    'form': form,
                    'login_failed': True
                })

        return render(request, 'login.html', {'form': form})
    
            
class LogoutView(View):

    def get(self,request):

        logout(request)

        return redirect('login')
    
class AdduploadView(View):

    def get(self,request):

        if not is_admin_user(request.user):
            
            return HttpResponseForbidden("You are not authorized.")

        form = UploadForm

        return render(request,'Adduploads.html',{'form':form})
    
    def post(self,request):

        if not is_admin_user(request.user):
            
            return HttpResponseForbidden("You are not authorized.")

        form = UploadForm(request.POST,request.FILES)

        if form.is_valid():

            Dashboard.objects.create(User_id=request.user,**form.cleaned_data)

            return redirect('create')

        return render(request,'Adduploads.html',{'form':form})
    
class UploadReadView(View):

    def get(self,request):

        items = Dashboard.objects.all()

        return render(request,'uploads.html',{'items':items})
    
class UpdateView(View):

    def get(self,request,**kwargs):

    #  if not is_admin_user(request.user):

        id = kwargs.get('pk')

        item = Dashboard.objects.get(id=id)

        form = UploadForm(instance=item)

        return render(request,'update.html',{'form':form})
    
    def post(self,request,**kwargs):

    #  if not is_admin_user(request.user):

        id = kwargs.get('pk')


        item = Dashboard.objects.get(id=id)

        form = UploadForm(request.POST,request.FILES, instance=item)

        if form.is_valid():

            form.save()

        form = UploadForm

        return render(request,'update.html',{'form':form})
    
class DeleteView(View):

    def get(self,request,**kwargs):

    #  if not is_admin_user(request.user):

        id = kwargs.get('pk')

        Dashboard.objects.get(id=id).delete()

        return redirect('uploadlist')
    
class DetailView(View):

    def get(self,request,**kwargs):

        id = kwargs.get('id')

        item = Dashboard.objects.get(id=id)

        return render(request,'detail.html',{'item':item})
    
# class SearchView(View):

#     def get(self,request,**kwargs):

#         date = request.GET.get('date')

#         item = []

#         if date :

#             parse_dt = parse_date(date)
            
#             if parse_dt:

#                 item = Dashboard.objects.filter(Uploaded_date = parse_dt)

        

#         return render(request,'search.html',{'item':item,'query':date})

class Home(View):

    def get(self,request):

        return render(request,'base.html')


class Intro(View):

    def get(self,request):

        return render(request,'home.html')
    
class AnnouncementView(View):

    def get(self,request):

        # if not is_admin_user(request.user):

             
            

        form = AnnouncementForm

        return render(request,'Announcement.html',{'form':form})
    
    def post(self,request):
        
        # if not is_admin_user(request.user):
            
        #     return HttpResponseForbidden("You are not authorized.")
        
        form = AnnouncementForm(request.POST)

        if form.is_valid():

            title = form.cleaned_data.get('title')

            message = form.cleaned_data.get('message')

            Announcements.objects.create(title=title,message=message)

            return redirect('announcement')

        return render(request,'Announcement.html',{'form':form})
    
class AnnounceReadView(View):

    def get(self,request):

        items = Announcements.objects.all().order_by('uploaded_date')

        return render(request,'announceuploads.html',{'items':items})

class AnounceUpdateView(View):

    def get(self,request,**kwargs):

    #  if not is_admin_user(request.user):

    #     return HttpResponseForbidden("You are not authorized.")

     id = kwargs.get('pk')

     item = Announcements.objects.get(id=id)

     form = AnnouncementForm(instance=item)

     return render(request,'Anupdate.html',{'form':form})
    
    def post(self,request,**kwargs):

    #  if not is_admin_user(request.user):

    #     return HttpResponseForbidden("You are not authorized.")

     id = kwargs.get('pk')
     
     item = Announcements.objects.get(id=id)

     form = AnnouncementForm(request.POST,request.FILES, instance=item)

     if form.is_valid():

            form.save()

        # form = AnnouncementForm

     return render(request,'announceuploads.html',{'form':form})
    
class AnDeleteView(View):

    def get(self,request,**kwargs):

    #  if not is_admin_user(request.user):

    #     return HttpResponseForbidden("You are not authorized.")

     id = kwargs.get('pk')

     Announcements.objects.get(id=id).delete()

     return redirect('read')
    

            