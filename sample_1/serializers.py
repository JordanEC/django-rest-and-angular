from django.contrib.auth.models import User
from rest_framework import serializers, permissions
from .models import *

"""
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
"""


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id','name','dni','email','phone','books',)#'__all__'


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(read_only=True,many=True)

    class Meta:
        model = Book
        fields = ('id','name', 'description','isbn','year','authors')#'__all__'
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def create(self, validated_data):
        book = super(BookSerializer, self).create(validated_data)
        authors = self.initial_data['authors']
        for author_dict in authors:
            author = Author.objects.get(name=author_dict['name'])
            book.authors.add(author)
        book.save()
        return book

    def update(self, instance, validated_data):
        authors = self.initial_data['authors'] #updated authors list
        for a in instance.authors.all():    #original authors
            delete = True
            for au in authors:
                if a.id == au['id']:        #delete if is not in the list
                    delete = False
            if delete:
                instance.authors.remove(a)

        return super(BookSerializer, self).update(instance, validated_data)

    def save(self, **kwargs):
        return super(BookSerializer, self).save(**kwargs)


