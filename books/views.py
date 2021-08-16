from django.db.models import Q
from django.contrib.auth.mixins import (
	LoginRequiredMixin,
	PermissionRequiredMixin
)
from django.views.generic import ListView, DetailView

from .models import Book


# class BookListView(LoginRequiredMixin, ListView):
# 	model = Book
# 	context_object_name = 'book_list'
# 	template_name = 'books/book_list.html'
# 	login_url = 'account_login'

# Access without login
class BookListView(ListView):
	model = Book
	context_object_name = 'book_list'
	template_name = 'books/book_list.html'


# class BookDetailView(
# 	LoginRequiredMixin, 
# 	PermissionRequiredMixin,
# 	DetailView):
# 	model = Book
# 	context_object_name = 'book'
# 	template_name = 'books/book_detail.html'
# 	login_url = 'account_login'
# 	permission_required = 'books.special_status'

# Access without login
class BookDetailView(DetailView):
	model = Book
	context_object_name = 'book'
	template_name = 'books/book_detail.html'


class SearchResultsListView(ListView):
	model = Book
	context_object_name = 'book_list'
	template_name = 'books/search_results.html'
	# queryset = Book.objects.filter(title__icontains='beginners')

	def get_queryset(self):
		query = self.request.GET.get('q')
		return Book.objects.filter(
			Q(title__icontains=query) | Q(title__icontains=query)
		)