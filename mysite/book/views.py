from django.shortcuts import render
from django.views import generic
from . import models


# Create your views here.
def index(request):
    num_books = models.Book.objects.all().count()
    num_instances = models.BookInstance.objects.all().count()
    num_instances_available = models.BookInstance.objects.filter(status__exact = 'a').count()
    num_author = models.Author.objects.count()
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_author': num_author
    }
    return render (request, 'book/index.html', context)

class BookListView(generic.ListView):
    model = models.Book
    context_object_name = 'my_book_list'
    # queryset = models.Book.objects.filter(summary__icontains = 'powerful')

    def  get_queryset(self):
        return models.Book.objects.filter(title__icontains = 'django')[:3]

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['my_book_list'] = models.Book.objects.all()[:1]
        return context

class AuthorListView(generic.ListView):
    model = models.Author
    queryset = models.Author.objects.filter(last_name__icontains = 'Hong')[:2]


class BookDetailView(generic.DetailView):
    medel = models.Book

    def  get_queryset(self):
        return models.Book.objects.all()


# def book_detail_view(request, pk):
#     try:
#         book_id = models.Book.objects.get(pk = pk)
#     except Book.DoesNotExist:
#         raise Http404("Book does not exist. ")
#
#     return render(request, 'book/book_detail.html',context = {'book': book})
