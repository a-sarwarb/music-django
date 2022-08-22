from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Song
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

# Create your views here.
# def LikeMusic(request, pk):
#     post = get_object_or_404(Song, id=request.POST.get('post_id'))
#     liked = False
#     if post.likes.filter(id=request.user.id).exists():
#         post.likes.remove(request.user)
#         liked = False
#     else:
#         post.likes.add(request.user)
#         liked = True
#
#     return HttpResponseRedirect(reverse('song_detail', args=[str(pk)]))
#
# def DislikeMusic(request, pk):
#     post = get_object_or_404(Song, id=request.POST.get('post_id'))
#     disliked = False
#     if post.dislikes.filter(id=request.user.id).exists():
#         post.dislikes.remove(request.user)
#         disliked = False
#     else:
#         post.dislikes.add(request.user)
#         disliked = True
#     return HttpResponseRedirect(reverse('song_detail', args=[str(pk)]))

class AddLike(LoginRequiredMixin, View):

    def post(self, request, pk, *args, **kwargs):
        post = Song.objects.get(pk=pk)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break


        if is_dislike:
            post.dislikes.remove(request.user)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            post.likes.add(request.user)

        if is_like:
            post.likes.remove(request.user)

        return HttpResponseRedirect(reverse('song_detail', args=[str(pk)]))



class AddDislike(LoginRequiredMixin, View):

    def post(self, request, pk, *args, **kwargs):
        post = Song.objects.get(pk=pk)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            post.likes.remove(request.user)



        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            post.dislikes.add(request.user)

        if is_dislike:
            post.dislikes.remove(request.user)

        return HttpResponseRedirect(reverse('song_detail', args=[str(pk)]))


class SongListView(ListView):
    model = Song
    template_name = 'songs_list.html'

class SearchResultsView(ListView):
    model = Song
    template_name = 'search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Song.objects.filter(
            Q(name__icontains=query) | Q(singer__icontains=query)
        )
        if len(object_list) < 0:
            return None
        else:
            return object_list


class PopMusicView(ListView):
    model = Song
    template_name = 'pop_music.html'

class RemixMusicView(ListView):
    model = Song
    template_name = 'remix.html'

class JazzMusicView(ListView):
    model = Song
    template_name = 'jazz.html'

class RapMusicView(ListView):
    model = Song
    template_name = 'rap.html'

class MusicCreateView(CreateView):
    model = Song
    fields = ['songs', 'category', 'name', 'singer']
    template_name = 'my_music.html'

class MusicDetailView(DetailView):
    model = Song
    template_name = 'song_detail.html'

    def get_context_data(self, *args, **kwargs):

        context = super(MusicDetailView, self).get_context_data()
        stuff = get_object_or_404(Song, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        total_dislikes = stuff.total_dislikes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        disliked = False
        if stuff.dislikes.filter(id=self.request.user.id).exists():
            disliked = True

        context["total_likes"] = total_likes
        context["total_dislikes"] = total_dislikes
        context['liked'] = liked
        context['disliked'] = disliked
        return context














