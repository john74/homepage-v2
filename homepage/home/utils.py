from bookmarks.models import BookmarkCategory, BookmarkSubCategory


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

def group_sub_categories(categories, bookmarks):
    sub_categories = []
    # for category in categories:
    #     for bookmark in bookmarks:
    for bookmark in bookmarks:
        sub_categories.append(bookmark.sub_category)
    return set(sub_categories)

def get_categorized_bookmarks(bookmarks):
    categories = get_bookmark_categories(bookmarks)
    sub_categories = group_sub_categories(categories, bookmarks)
    print(sub_categories)
    for category in sub_categories:
        pass

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