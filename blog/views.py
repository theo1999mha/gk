from collections import OrderedDict
from rest_framework.response import Response
from django.http import HttpResponse,Http404
from rest_framework.decorators import api_view
from blog.models import Post ,Comment
from . import serializers as SR
from rest_framework.pagination import  PageNumberPagination
from django.db.models import Count

def home(request):
    return HttpResponse ('this is our home page')

def Ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@api_view(['GET'])
def getposts(request):
    paginator = PageNumberPagination() 
    paginator.page_size = 20

    posts = Post.objects.filter(status=1).prefetch_related('author')
    
    result = paginator.paginate_queryset(posts,request)

    serializer = SR.Postserializer(result , many=True,context={'request': request})
    return Response(OrderedDict([
            ('count', paginator.page.paginator.count),
            ('next', paginator.get_next_link()),
            ('previous', paginator.get_previous_link()),
            ('results', serializer.data)
        ]))


@api_view(['POST'])
def createPost(request):

    serializer = SR.Postserializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors)
    serializer.save()
    return Response('ok')


@api_view(['POST'])
def createAuthor(request):
    serializer = SR.UserSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors)
    serializer.save()
    return Response('ok')

@api_view(['POST'])
def like_post(request):
    request.data._mutable = True

    if request.user:
        request.data['user_id'] = request.user.pk
    request.data['ip'] = Ip(request)
    
    
    serializer = SR.LikeSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors)

    post = Post.objects.filter(pk=request.data['post_id']).first()
    post.likes_count += 1

    post.save()

    serializer.save()
    return Response('ok')


@api_view(['get'])
def extractpost(request ,id):
    post = Post.objects.filter(id=id).first()
    if not post:
        raise Http404()
    serializer = SR.Postserializer(post , many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getcomments(request ,id):
    post = Post.objects.filter(id=id).first()
    comments = post.comment_set.all()
    serializer = SR.CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def updatepost(request ,id):
    post = Post.objects.get(id=id)
    serializer = SR.UpdatedPostSerializer(post,data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors)    
    serializer.save() 
    return Response(serializer.data)

@api_view(['DELETE'])
def deletepost(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return Response('your post has successfully deleted')

@api_view(['PUT'])
def change_status(request, pk):
    post = Post.objects.filter(id=pk).first()
    if not post:
        raise Http404()
    
    status = request.data['status']
    if not status:
        raise Http404()

    choess = ('0','1')
    if not status in choess:
        return Response('bad request',status=400 )


    post.status = status
    post.save()
    return Response('your status is save')

@api_view(['GET'])
def liked_posts (request):
    liked = Post.objects.annotate(liked_posts = Count('like__post_id')).filter().first()
    return HttpResponse(liked)





    
