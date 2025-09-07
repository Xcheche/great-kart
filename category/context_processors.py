from category.models import Category





def menu_links(request):
    """Context processor to add menu links (categories) to all templates.
    It retrieves all Category objects and makes them available in the template context  as dict 
    This link variable can then be used anywhere in the templates to display category links.
    Dont forget in settings.py to add the context processor to TEMPLATES option
    'OPTIONS': {
        'context_processors': [
    """
    links = Category.objects.all()
    return dict(links=links)