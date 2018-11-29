"""pvrl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#for redirecting path
from django.views.generic import RedirectView

#For static webpage(During our Development phase)
from django.conf import settings
from django.conf.urls.static import static
from login.views import index, user_login
from upload.views import uploads_page, file_upload 
from failed_login.views import index as f_index
from upload_success.views import uploads_page as s_uploads_page 

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    #Creating new path for all localhost access
    path('pvrl', index),

    path('pvrl/f-login', f_index),

    path('pvrl/login', user_login),

    path('pvrl/uploads', uploads_page),

    path('pvrl/upload-file', file_upload),

    path('pvrl/s-uploads', s_uploads_page),
    
    path('', RedirectView.as_view(url='pvrl', permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 