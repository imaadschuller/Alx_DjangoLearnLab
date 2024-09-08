from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["title", "publication_year", "author"]

        #Custom Validation for the publication_year field

        def validate_publication_year(self, value):
            current_year = datetime.now().year
            if value > current_year:
                raise serializers.ValidationError("Publication year cannot be in the future.")
            return value

class AuthorSerializer(serializers.ModelSerializer):
    #AuthorSerializer includes author's name and a nested BookSerializer to serialize the related books dynamically
    books = BookSerializer(many= True, read_only=True)

    class Meta:
        model = Author
        fields = ["name", "books"]
