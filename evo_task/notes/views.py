
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import  render, redirect
from django.contrib.auth import authenticate, login
from .models import Note
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import NoteSerializer
from django.views.generic import View
from django.urls import reverse_lazy
# from .forms import UserForm


class NoteList(APIView):

    def get(self, request):
        note = Note.objects.all()
        serializer = NoteSerializer(note, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class IndexView(generic.ListView):
    template_name = 'notes/index.html'
    #context_object_name = 'all_albums'

    def get_queryset(self):
        return Note.objects.all()


class DetailView(generic.DetailView):
    model = Note
    template_name = 'notes/detail.html'


class NoteCreate(CreateView):
    model = Note
    fields = ['note_title', 'note_body', 'note_logo']


class NoteUpdate(UpdateView):
    model = Note
    fields = ['note_title', 'note_body', 'note_logo']


class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy('notes:index')

# class UserFormView(View):
#
#     form_class = UserForm
#     template_name = 'music/registration_form.html'
#
#     # display blank form
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template_name, {'form':form})
#
#     # process form data
#     def post(self, request):
#         form = self.form_class(request.POST)
#
#         if form.is_valid():
#
#             user = form.save(commit = False)
#
#             #cleaned (normalized) data
#
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user.set_password(password)
#             user.save()
#
#             #returns User objects if credentials are correct
#
#             user = authenticate(username = username, password = password)
#
#             if user is not None:
#
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('music:index')
#
#         return render(request, self.template_name, {'form' : form})