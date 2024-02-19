from rest_framework import serializers
from blog.models import Post,Comment,Like
from django.contrib.auth import get_user_model


class miniUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('last_name','first_name','email')

class Postserializer(serializers.ModelSerializer):
    author = miniUserSerializer(many=False)
    fist_comment = serializers.SerializerMethodField()

    def get_fist_comment(self,obj):
        comment = Comment.objects.filter(post_id=obj.id).first()
        if comment :
            comment_serializer = CommentSerializer(comment,many=False)
            return comment_serializer.data if comment_serializer.data else []
        return []



    class Meta:
        model = Post
        fields = '__all__'  

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('body')

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'

class UpdatedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','description')

class ChangeStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('status')

class LikedPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
