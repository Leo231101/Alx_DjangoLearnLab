# Author model stores the author's name
class Author(models.Model):
    name = models.CharField(max_length=255)
    # other fields...

# Book model stores book information with a foreign key to the Author model
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    # other fields...

    from api.models import Author, Book
author = Author.objects.create(name="George Orwell")
book = Book.objects.create(title="1984", publication_year=1949, author=author)

