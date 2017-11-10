from django.views.generic import View, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Album
from .forms import UserForm
from .serializers import AlbumSerializer

class IndexView(ListView):
	template_name='music/index.html'
	context_object_name = 'all_albums'

	def get_queryset(self):
		return Album.objects.all()


class DetailView(DetailView):
	model = Album
	template_name = 'music/detail.html'


class AlbumCreate(CreateView):
	model = Album
	fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
	model = Album
	fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
	model = Album
	success_url = reverse_lazy('music:index')

class like(View):

		
class UserFormView(View):
	form_class = UserForm
	template_name = 'music/registration_form.html'

	# display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form':form})

	# process form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)

			# cleaning data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()
			
			user = authenticate(username=username, password=password)
			
			if user is not None:
				if user.is_active:
					 login(request,user)
					 return redirect('music:index')

		return render(request, self.template_name, {'form':form})

# List All albums or create a new one
# alnums/
class AlbumList(APIView):
	def get(self, request):
		albums = Album.objects.all()
		serializer = AlbumSerializer(albums, many=True)
		return Response(serializer.data)

	def post(self):
		pass