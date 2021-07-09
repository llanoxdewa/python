from django.shortcuts import render
from django.views.generic import TemplateView,RedirectView
from .models import Post


class WithContext(TemplateView):

    template_name = 'context.html'

    def get_context_data(self, **kwargs):
        print(self.request.GET)
        context = super().get_context_data(**kwargs)
        context['title'] = 'page with input and context'
        context['post_single_object'] = Post.objects.get(author=context['inputURL'])
        return context

class HomeView(RedirectView):
    pattern_name = 'cbv:index'



class RedirectPostModel(RedirectView):
    pattern_name = 'cbv:redirect_to_post_model'
    # permanent =
    def get_redirect_url(self,*args,**kwargs):
        # if kwargs['inputURL'] == 'llano':
        #     kwargs['inputURL'] = 'dragon'
        return super().get_redirect_url(*args,**kwargs)

