import httpx


def get_bookmark_categories(bookmarks):
    categories = []
    for bookmark in bookmarks:
        categories.append(bookmark.sub_category.category)
    return set(categories)

def get_bookmark_sub_categories(bookmarks):
    sub_categories = []
    for bookmark in bookmarks:
        sub_categories.append(bookmark.sub_category)
    return set(sub_categories)

def get_shortcuts(bookmarks):
    shortcuts = []
    for bookmark in bookmarks:
        if bookmark.is_shortcut:
            shortcuts.append({
                'name': bookmark.name,
                'url': bookmark.url,
                'icon': bookmark.icon
            })
    return shortcuts

def get_weather_data(user, data_type):
    if not user.open_weather_key:
        return
    url = f'http://api.openweathermap.org/data/2.5/{data_type}?q={user.city}&appid={user.open_weather_key}&units=metric'
    response = httpx.get(url)
    if response.status_code != 200:
        return
    return response.json()

def get_current_weather_data(data):
    if not data:
        return
    return {
        'temp': data['main']['temp'],
        'temp_min': data['main']['temp_min'],
        'temp_max': data['main']['temp_max'],
        'feels_like': data['main']['feels_like'],
        'description': data['weather'][0]['description']
    }