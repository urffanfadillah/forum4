from django.contrib import admin
# import settings
from django.conf import settings 
from django.urls import path, include # import include
# import static
from django.conf.urls.static import static

from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path froala_editor
    path('froala_editor/', include('froala_editor.urls')),
    # path login
    path('login/', LoginView.as_view(), name='login'),
    # path logout
    path('logout/', LogoutView.as_view(), name='logout'),
    # path home
    path('', views.index, name='home'),
    # path include post
    path('post/', include('post.urls', namespace='post')),
]
# buat setting media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


