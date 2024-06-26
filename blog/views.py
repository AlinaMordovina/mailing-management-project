from django.shortcuts import render
from django.views.generic import DetailView

from blog.models import Blog


def blog(request):
    context = {
        "object_list": Blog.objects.filter(date_is_published__isnull=False),
        "title": " Блог",
    }
    return render(request, "blog/blog_list.html", context)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object
