from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Blog


# Create your views here.

class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'date_of_creation',)
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(sign_of_publication=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'date_of_creation',)

    def get_success_url(self):
        return reverse('blog:view', args=[self.object.pk])

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


def toggle_activity(request, pk):
    blog_data = get_object_or_404(Blog, pk=pk)
    if blog_data.sign_of_publication:
        blog_data.sign_of_publication = False
    else:
        blog_data.sign_of_publication = True

    blog_data.save()

    return redirect(reverse('blog:list'))


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
