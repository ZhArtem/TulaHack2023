from .models import *


menu = [
    {'title': "О проекте", 'url_name': 'about'},
    {'title': "Добавить публикацию", 'url_name': 'post_create'},
    {'title': "Обратная связь", 'url_name': 'contact'},
]


class DataMixin:
    paginate_by = 5

    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu
        return context