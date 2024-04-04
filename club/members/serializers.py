from rest_framework import serializers

from library.models import Book
from members.models import MemberCard


class MemberCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberCard
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
