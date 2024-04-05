from django.contrib.auth.models import User
from rest_framework import serializers

from library.models import Book
from members.models import MemberCard


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'username'


class MemberCardSerializer(serializers.ModelSerializer):
    likes = UserSerializer(many=True, read_only=True)

    class Meta:
        model = MemberCard
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):
    likes = MemberCardSerializer(many=True, read_only=True)
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def get_like_count(self, obj):
        return len(obj.likes.all())
