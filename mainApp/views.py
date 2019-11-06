from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.urls import reverse
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView,TemplateView
from mainApp.models import Faculty,Album,Photo,StudentAchiev,Review
from django.urls import reverse_lazy
from mainApp.models import Faculty as f

class HomePage(TemplateView):
    """
    Because our needs are so simple, all we have to do is
    assign one value; template_name. The home.html file will be created
    in the next lesson.
    """
    template_name = 'mainApp/homepage.html'
    # def get_context_data(self, **kwargs):
    #     context = super(AboutView, self).get_context_data(**kwargs)


class addFaculty(CreateView):
    #template_name ='faculty/addFaculty.html'
    model = Faculty
    fields = ['name','email','qual','pic','desc','category']
    
    
    template_name='Faculty/addFaculty.html'
    def get_context_data(self, **kwargs):
        
        ctx = super(addFaculty, self).get_context_data(**kwargs)
        ctx['object_list'] =f.objects.all()
        return ctx


    def delete(request,id,*args, **kwargs):
        if request.user.is_authenticated:
            print("deletewas called")
            f.objects.filter(id=id).delete()
            template = loader.get_template('Faculty/addFaculty.html')
            context={}
            context['object_list'] =f.objects.all() 
            return redirect(reverse('addFaculty'))
        else :
            return redirect(reverse('login'))

    def update(request,id):
        Faculty=get_object_or_404(Faculty,pk=id)

        return redirect(reverse('addFaculty'))



class listFaculty(ListView):
    model = Faculty
    object_list=f.objects.all()
    template_name="Faculty/faculty_list.html"
    def get_queryset(self):
        qs = self.model.objects.all().filter(category=1).order_by('name')
        # print(str(qs.query))   # SQL check is perfect for debugging
        return qs
    def get(self, request, *args, **kwagrs):
        self.object_list=self.get_queryset()
        context=self.get_context_data()
        #context['media_url']=settings.MEDIA_URL+"Faculty_pic/"
        #return render(request,context)
        return self.render_to_response(context)
   
class listStaff(ListView):
    model = Faculty
    # object_list=f.objects.all()
    template_name="Faculty/staff_list.html"
    def get_queryset(self):
        qs = self.model.objects.all().filter(category=2).order_by('name')
        # print(str(qs.query))   # SQL check is perfect for debugging
        return qs
    def get(self, request, *args, **kwagrs):
        self.object_list=self.get_queryset()
        context=self.get_context_data()
        #context['media_url']=settings.MEDIA_URL+"Faculty_pic/"
        #return render(request,context)
        return self.render_to_response(context)

class updateFaculty(UpdateView):
    model=Faculty
    fields=['name','desc','pic','category']
    template_name="Faculty/faculty_update.html"
    def get_object(self, queryset=None):
        obj = f.objects.get(id=self.kwargs['id'])
        return obj

class deleteFaculty(DeleteView):
    model=Faculty
   # success_url=reverse('facultyList')
    def get_object(self, queryset=None):
        obj = f.objects.get(id=self.kwargs['id'])
        return obj











class listAlbum(ListView):
    model =Album
    fields=['name','desc']
    template_name='photogallery/list_album.html'
    # paginate_by = 3

    def get(self, request, *args, **kwagrs):
        self.object_list=self.get_queryset()
        context=self.get_context_data()
        #context['media_url']=settings.MEDIA_URL+"Faculty_pic/"
        #return render(request,context)
        return self.render_to_response(context)



class updateAlbum(UpdateView):
    model =Album
    fields=['name','desc']
    template_name='photogallery/update_album.html'
    def get_object(self, queryset=None):
        obj = Album.objects.get(id=self.kwargs['id'])
        return obj

class deleteAlbum(DeleteView):
    model=Album
   # success_url=reverse('facultyList')
    template_name='photogallery/delete_album.html'
    def get_object(self, queryset=None):
        obj = Album.objects.get(id=self.kwargs['id'])
        return obj
    def get_success_url(self, **kwargs):
        
        success_url=reverse_lazy("listAlbum")
        return success_url

class addAlbum(CreateView):
    model=Album
    fields=['name','desc','thumbnail']
    template_name='photogallery/add_album.html'

#considering photo list as a detail of album
class listPhoto(ListView):
    model=Photo
    fields=['name','pic']
    template_name='photogallery/photo_list.html'
    def get_context_data(self, **kwargs):
        context = super(listPhoto, self).get_context_data(**kwargs)
        context['albumid']=self.kwargs['pk']
        context['albumname']=Album.objects.get(pk=self.kwargs['pk']).name
        context['albumdesc']=Album.objects.get(pk=self.kwargs['pk']).desc
        return context

    def get_queryset(self):
        return Photo.objects.filter(albumid=self.kwargs['pk'])
    
    

class addPhoto(CreateView):
    model=Photo
    fields=['name','pic','albumid']
    template_name='photogallery/add_photo.html'
    def get_initial(self):
        albumid = get_object_or_404(Album, id=self.kwargs.get('pk'))
        return {
            'albumid':albumid,
            }
        
    

class deletePhoto(DeleteView):
    model=Photo
    template_name='photogallery/delete_photo.html'
    
    def get_object(self, queryset=None):
        obj = Photo.objects.get(id=self.kwargs['picid'])
        success_url=reverse_lazy("listPhoto",kwargs={'pk':obj.albumid.id})
        return obj

    def get_success_url(self, **kwargs):
        obj = Photo.objects.get(id=self.kwargs['picid'])
        success_url=reverse_lazy("listPhoto",kwargs={'pk':obj.albumid.id})
        return success_url


class listStuAchiev(TemplateView):
    #model=StudentAchiev
    template_name='studentachiev/list_stu_ach.html'
    # engineers=objects = StudentAchiev.objects.filter(category= 2)
    def get_context_data(self, **kwargs):
        context = super(listStuAchiev, self).get_context_data(**kwargs)
        context['engineers']= StudentAchiev.objects.filter(category=2)
        return context

class addStuAchive(CreateView):
    model=StudentAchiev
    fields=['name','institute','category','pic','year']    
    template_name='studentachiev/addachiev.html'


class admissionInfo(TemplateView):
    template_name='admission_info.html'


class labs(TemplateView):
    template_name='acadamic_labs.html'


# class Faculty(TemplateView):
#     template_name='faculty.html'



class listReview(ListView):
    model=Review
    template_name='review/list_review.html'

class about(TemplateView):
    template_name='about.html'

class mission(TemplateView):
    template_name='mission.html'


class principal(TemplateView):
    template_name='principal.html'


class playground(TemplateView):
    template_name='playground.html'
class mess(TemplateView):
    template_name='mess.html'
class yoga(TemplateView):
    template_name='yoga.html'
class smartclass(TemplateView):
    template_name='smartclass.html'
class hostel(TemplateView):
    template_name='hostel.html'
class opengym(TemplateView):
    template_name='opengym.html'

class index(TemplateView):
    template_name='index.html'
class contact_us(TemplateView):
    template_name='contact_us.html'