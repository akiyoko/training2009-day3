from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # TODO: 「/」にアクセスした場合に「/todo/」にリダイレクトする
    # path('', RedirectView.as_view(url='/todo/')),
    path('todo/', include('todo.urls')),
]
