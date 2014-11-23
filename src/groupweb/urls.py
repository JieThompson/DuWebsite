from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'contents.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^people/', 'contents.views.people', name='people'),
    url(r'^publication/', 'contents.views.publication', name='publication'),
    url(r'^research/', 'contents.views.research', name='research'),
    url(r'^excition/', 'contents.views.exciton', name='exciton'),
    url(r'^fqhe/', 'contents.views.fqhe', name='fqhe'),
    url(r'^magneto-transport/', 'contents.views.magnetotransport', name='magnetotransport'),
    url(r'^many-particle/', 'contents.views.manyparticle', name='manyparticle'),
    url(r'^microwave/', 'contents.views.microwave', name='microwave'),
    url(r'^nano-electronics/', 'contents.views.nanoelectronics', name='nanoelectronics'),
    url(r'^qshe/', 'contents.views.qshe', name='qshe'),
    url(r'^quantum-well/', 'contents.views.quantumwell', name='quantumwell'),
    url(r'^shpm/', 'contents.views.shpm', name='shpm'),
    
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)