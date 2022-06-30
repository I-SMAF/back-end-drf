from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('v1/', include('api.v1.urls'), name='v1')
        # other versions
    ]), name='api'),

]
