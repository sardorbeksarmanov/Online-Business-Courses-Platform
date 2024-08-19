from django.db import models
from django_filters import rest_framework as filters

class Serves(models.Model):
    title = models.CharField(max_length=255)
    image = models.URLField(null=True)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        indexes = [
            models.Index(fields=['slug']),
        ]


class ServesFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    price = filters.NumberFilter()
    slug = filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Serves
        fields = ['title', 'price', 'slug']


class Clients(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=255, unique=True, default='default_username')
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    image = models.URLField(null=True)
    defination = models.CharField(max_length=255, default='Default value')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['last_name', 'first_name']

class ClientsFilter(filters.FilterSet):
    first_name = filters.CharFilter(lookup_expr='icontains')
    last_name = filters.CharFilter(lookup_expr='icontains')
    email = filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Clients
        fields = ['first_name', 'last_name', 'email']


class Comment(models.Model):
    clients = models.ForeignKey(Clients, on_delete=models.CASCADE)
    serves = models.ForeignKey('Serves', on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.clients} on {self.serves}"

    class Meta:
        ordering = ['-created_at']

class CommentFilter(filters.FilterSet):
    comment = filters.CharFilter(lookup_expr='icontains')
    rating = filters.NumberFilter()
    created_at = filters.DateTimeFilter()

    class Meta:
        model = Comment
        fields = ['comment', 'rating', 'created_at']


class Advise(models.Model):
    slug = models.SlugField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    image = models.URLField(null=True)
    level = models.CharField(max_length=50)
    telegram_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['last_name', 'first_name']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['email']),
        ]

class AdviseFilter(filters.FilterSet):
    first_name = filters.CharFilter(lookup_expr='icontains')
    last_name = filters.CharFilter(lookup_expr='icontains')
    level = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Advise
        fields = ['first_name', 'last_name', 'level']


class FAQs(models.Model):
    questions = models.TextField()
    answers = models.TextField()

    def __str__(self):
        return self.questions

    class Meta:
        ordering = ['questions']

class FAQsFilter(filters.FilterSet):
    questions = filters.CharFilter(lookup_expr='icontains')
    answers = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = FAQs
        fields = ['questions', 'answers']


class Features(models.Model):
    title = models.ForeignKey(Serves, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title.serves.title

    class Meta:
        ordering = ['title']

class FeaturesFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    description = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Features
        fields = ['title', 'description']
