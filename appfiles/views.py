from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from appfiles.forms import FilesForm
from appfiles.models import Files
from appfiles.tasks import send_email, checked_files
from users.models import User

class FileListView(LoginRequiredMixin, ListView):
    # queryset = Files.objects.filter(author = self.request.user)
    # model = Files
    login_url = '/login/'
    template_name = 'appfiles/home.html'
    context_object_name = 'files'

    def get_queryset(self):
        return Files.objects.filter(author=self.request.user)


class FileDetailView(LoginRequiredMixin, DetailView):
    model = Files
    login_url = '/login/'
    template_name = 'appfiles/detail.html'
    context_object_name = 'object'


class FilesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Files
    login_url = '/login/'
    success_url = "/list/"
    template_name = 'users/update.html'
    fields = ['title', 'file']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.checked = False
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class FilesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Files
    login_url = '/login/'
    success_url = reverse_lazy('list')
    template_name = 'appfiles/delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


@login_required
def model_form_upload(request):
    if request.method == 'POST':
        file = Files(author = request.user)
        form = FilesForm(request.POST, request.FILES, instance=file)
        if form.is_valid():

            form.save()

            return redirect('list')
    else:
        form = FilesForm()
    return render(request, 'appfiles/model_form_upload.html', {
        'form': form
    })

def about(request):
    # checked_files.delay()
    # checked_files()
    return render(request, 'appfiles/about.html', {'title': 'Python-разработчик (ISA)'})