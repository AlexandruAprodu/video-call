
from django.urls import path
from agora.views import Agora
from video import views as video_views


urlpatterns = [
    path('agor/', Agora.as_view(app_id='f5648bb23083402cbd9c2faa5692593a', channel='Suzeta')),
    path('', video_views.agora, name='agora'),
    path('agora/', video_views.agora, name='agora'),
]
