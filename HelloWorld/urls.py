from django.conf.urls import url
from django.contrib import admin
from . import view
from . import testdb

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', view.hello),
    url(r'^testadd', testdb.testadd),
    url(r'^testsearch', testdb.testsearch),
    url(r'^testupdate', testdb.testupdate),
    url(r'^testdelete', testdb.testdelete),

]