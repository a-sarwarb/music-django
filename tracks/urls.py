from django.urls import path
from .views import (
    SongListView,
    SearchResultsView,
    PopMusicView,
    JazzMusicView,
    RapMusicView,
    RemixMusicView,
    MusicCreateView,
    MusicDetailView,
    AddLike,
    AddDislike
 )

urlpatterns = [
    path('list/', SongListView.as_view(), name='songs_list'),
    path('search/', SearchResultsView.as_view(), name='search_result'),
    path('pop/', PopMusicView.as_view(), name='pop_music'),
    path('classic/', JazzMusicView.as_view(), name='jazz'),
    path('rap/', RapMusicView.as_view(), name='rap'),
    path('remix/', RemixMusicView.as_view(), name='remix'),
    path('newmusic/', MusicCreateView.as_view(), name='my_music'),
    path('<int:pk>/', MusicDetailView.as_view(), name='song_detail'),
    path('like/<int:pk>', AddLike.as_view(), name='like_music'),
    path('dislike/<int:pk>', AddDislike.as_view(), name='dislike_music'),
]