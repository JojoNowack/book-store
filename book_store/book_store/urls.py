# book_store -> url

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # letting the string empty forces django to look at an empty path at 
    # account.urls. Since there is an path with emtpy strings as well, 
    # the first page displays "Login Seite"
    path('', include('account.urls')),
    # path('account/', include('account.urls'))
]
