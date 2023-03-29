from requests import Response
from rest_framework import serializers
from .models import Blog, Category, Comment, Like, PostView
from django.contrib.auth import get_user_model

User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name','id',)

class CommentSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = "__all__"

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"



class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    likes = serializers.SerializerMethodField()
    post_views = serializers.SerializerMethodField()
    author = serializers.StringRelatedField()
    comment_count=serializers.SerializerMethodField()
    category_name=serializers.SerializerMethodField()
    likes_n=serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'image', 'category', 'publish_date', 'author', 'status', 'slug', 'comments','category_name','likes','post_views',"comment_count","likes_n")
    
    def create(self, validated_data):
        author = User.objects.get(username=self.context['request'].user)
        validated_data['author'] = author
        return Blog.objects.create(**validated_data)
    
    def get_likes(self, obj):
        return Like.objects.filter(post=obj).count()

    def get_post_views(self, obj):
        return PostView.objects.filter(post=obj).count()
    
    def get_comment_count(self, obj):
        return Comment.objects.filter(post=obj).count()

    def get_category_name(self, obj):
        return Category.objects.get(id=obj.category.id).name
    
    def get_likes_n(self, obj):
        return Like.objects.filter(post=obj).values()