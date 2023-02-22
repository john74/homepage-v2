from django.shortcuts import render, redirect

from bookmarks.models import Bookmark
from users.models import User

from .utils import get_categorized_bookmarks, get_shortcuts, get_bookmark_sub_categories, get_bookmark_categories


def home(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('authentication/login/')

    bookmarks = Bookmark.objects.all()
    bookmark_categories = get_bookmark_categories(bookmarks)
    bookmark_sub_categories = get_bookmark_sub_categories(bookmarks)
    shortcuts = get_shortcuts(bookmarks)
    context = {
        'bookmark_categories': bookmark_categories,
        'bookmark_sub_categories': bookmark_sub_categories,
        'bookmarks': bookmarks,
        'shortcuts': shortcuts
    }
    return render(request, 'home.html', context)
