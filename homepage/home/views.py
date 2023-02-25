from django.shortcuts import render, redirect

from bookmarks.models import Bookmark
from users.models import User

from .utils import get_weather_data, get_shortcuts, get_bookmark_sub_categories, get_bookmark_categories, get_current_weather_data


def home(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('authentication/login/')

    bookmarks = Bookmark.objects.all()
    bookmark_categories = get_bookmark_categories(bookmarks)
    bookmark_sub_categories = get_bookmark_sub_categories(bookmarks)
    shortcuts = get_shortcuts(bookmarks)

    current_weather_json = get_weather_data(user, 'weather')
    current_weather_data = get_current_weather_data(current_weather_json)

    context = {
        'bookmark_categories': bookmark_categories,
        'bookmark_sub_categories': bookmark_sub_categories,
        'bookmarks': bookmarks,
        'shortcuts': shortcuts,
        'current_weather_data': current_weather_data
    }
    return render(request, 'home.html', context)
