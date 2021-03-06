from django.shortcuts import render, get_object_or_404
from .models import Tweet
from django.views.generic import DetailView, ListView, CreateView
from .forms import TweetModelForm
# Create your views here.



# Update

# Delete

# Create

class TweetCreateView(CreateView):
    # queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    # fields = ['user', 'content']
    success_url = "/tweet/create/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TweetCreateView, self).form_valid(form)


# Retrieve

class TweetDetailView(DetailView):
    # template_name = "tweets/detail_view.html"
    queryset = Tweet.objects.all()
    #
    # def get_object(self):
    #     print(self.kwargs)
    #     pk = self.kwargs.get("pk")
    #     obj = get_object_or_404(Tweet, pk=pk)
    #     print(pk)
    #     return Tweet.objects.get(id=pk)



class TweetListView(ListView):
    # template_name = "tweets/list_view.html"
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView,self).get_context_data(*args, **kwargs)
        print(context)
        return(context)

#
# def tweet_create_view(request):
#     form= TweetModelForm(request.POST or None)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.user =request.user
#         instance.save()
#     context ={
#         "form":form
#     }
#     return render(request, 'tweets/create_view.html', context)

#
#
# def tweet_detail_view(request, pk=None):  #pk =id
#     # obj = Tweet.objects.get(pk=pk)
#     obj = get_object_or_404(Tweet, pk=pk)
#     print(obj)
#     context ={
#         "object": obj
#     }
#     return render(request, "tweets/detail_view.html", context)
# #
#
# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     print(queryset)
#     for obj in queryset:
#         print(obj.content)
#     context ={
#         "object_list": queryset
#     }
#     return render(request, "tweets/list_view.html", context)