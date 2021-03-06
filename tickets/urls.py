from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from tickets.views import MyTicketListView, MyTicketDetailView, TicketCreateView


urlpatterns = [
    url(r'^my/$', login_required(MyTicketListView.as_view()), name='list'),
    url(r'^my/(?P<pk>\d+)/$', login_required(MyTicketDetailView.as_view()), name='detail'),
    url(r'^create/$', login_required(TicketCreateView.as_view()), name='create'),
]
