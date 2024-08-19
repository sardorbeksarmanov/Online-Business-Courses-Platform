from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from django.db.models import Q
from .serializers import (
    ServiceSerializer, ClientSerializer, AdvisersSerializer,
    FeaturesSerializer, FAQsSerializer, CommentsSerializer
)
from .models import Serves, Clients, Comment, Features, FAQs, Advise

class ServiseViewSet(ModelViewSet):
    queryset = Serves.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [AllowAny]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        return super().retrieve(request, *args, **kwargs)

    @action(detail=True, methods=['get'])
    def get_reviews(self, request, pk=None):
        serve = self.get_object()
        return Response({'reviews': serve.reviews})

    @action(detail=True, methods=['post'])
    def add_review(self, request, pk=None):
        serve = self.get_object()
        review = request.data.get('review')
        if review:
            serve.reviews += f"\n{review}"
            serve.save()
        return Response({'status': 'review added'})

    def get_queryset(self):
        query = super().get_queryset()
        search_data = self.request.query_params.get('search')
        if search_data:
            query = query.filter(Q(title__icontains=search_data) | Q(description__icontains=search_data))
        return query

    @action(detail=True, methods=['put'])
    def update_service(self, request, pk=None):
        serve = self.get_object()
        serializer = self.get_serializer(serve, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['delete'])
    def delete_service(self, request, pk=None):
        serve = self.get_object()
        serve.delete()
        return Response({'status': 'service deleted'})

    @action(detail=False, methods=['post'])
    def create_service(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class ClientViewSet(ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer

    def get_queryset(self):
        query = super().get_queryset()
        search_data = self.request.query_params.get('search')
        if search_data:
            query = query.filter(Q(first_name__icontains=search_data) | Q(last_name__icontains=search_data) | Q(email__icontains=search_data))
        return query

    @action(detail=True, methods=['get'])
    def get_email(self, request, pk=None):
        client = self.get_object()
        return Response({'email': client.email})

    @action(detail=True, methods=['get'])
    def get_phone(self, request, pk=None):
        client = self.get_object()
        return Response({'phone_number': client.phone_number})

    @action(detail=True, methods=['get'])
    def get_username(self, request, pk=None):
        client = self.get_object()
        return Response({'username': client.username})

    @action(detail=True, methods=['put'])
    def update_client(self, request, pk=None):
        client = self.get_object()
        serializer = self.get_serializer(client, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['delete'])
    def delete_client(self, request, pk=None):
        client = self.get_object()
        client.delete()
        return Response({'status': 'client deleted'})

    @action(detail=False, methods=['post'])
    def create_client(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class AdvisersViewSet(ModelViewSet):
    queryset = Advise.objects.all()
    serializer_class = AdvisersSerializer

    def get_queryset(self):
        query = super().get_queryset()
        search_data = self.request.query_params.get('search')
        if search_data:
            query = query.filter(Q(first_name__icontains=search_data) | Q(last_name__icontains=search_data) | Q(level__icontains=search_data))
        return query

    @action(detail=True, methods=['get'])
    def get_level(self, request, pk=None):
        adviser = self.get_object()
        return Response({'level': adviser.level})

    @action(detail=True, methods=['get'])
    def get_email(self, request, pk=None):
        adviser = self.get_object()
        return Response({'email': adviser.email})

    @action(detail=True, methods=['get'])
    def get_telegram(self, request, pk=None):
        adviser = self.get_object()
        return Response({'telegram_link': adviser.telegram_link})

    @action(detail=True, methods=['put'])
    def update_adviser(self, request, pk=None):
        adviser = self.get_object()
        serializer = self.get_serializer(adviser, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['delete'])
    def delete_adviser(self, request, pk=None):
        adviser = self.get_object()
        adviser.delete()
        return Response({'status': 'adviser deleted'})

    @action(detail=False, methods=['post'])
    def create_adviser(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class FeaturesViewSet(ModelViewSet):
    queryset = Features.objects.all()
    serializer_class = FeaturesSerializer

    def get_queryset(self):
        query = super().get_queryset()
        search_data = self.request.query_params.get('search')
        if search_data:
            query = query.filter(Q(title__icontains=search_data) | Q(description__icontains=search_data))
        return query

    @action(detail=True, methods=['get'])
    def get_title(self, request, pk=None):
        feature = self.get_object()
        return Response({'title': feature.title})

    @action(detail=True, methods=['get'])
    def get_description(self, request, pk=None):
        feature = self.get_object()
        return Response({'description': feature.description})

    @action(detail=True, methods=['get'])
    def get_image_url(self, request, pk=None):
        feature = self.get_object()
        return Response({'image_url': feature.image.url})

    @action(detail=True, methods=['put'])
    def update_feature(self, request, pk=None):
        feature = self.get_object()
        serializer = self.get_serializer(feature, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['delete'])
    def delete_feature(self, request, pk=None):
        feature = self.get_object()
        feature.delete()
        return Response({'status': 'feature deleted'})

    @action(detail=False, methods=['post'])
    def create_feature(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class FAQsViewSet(ModelViewSet):
    queryset = FAQs.objects.all()
    serializer_class = FAQsSerializer

    def get_queryset(self):
        query = super().get_queryset()
        search_data = self.request.query_params.get('search')
        if search_data:
            query = query.filter(Q(questions__icontains=search_data) | Q(answers__icontains=search_data))
        return query

    @action(detail=True, methods=['get'])
    def get_question(self, request, pk=None):
        faq = self.get_object()
        return Response({'question': faq.questions})

    @action(detail=True, methods=['get'])
    def get_answer(self, request, pk=None):
        faq = self.get_object()
        return Response({'answer': faq.answers})

    @action(detail=True, methods=['get'])
    def get_summary(self, request, pk=None):
        faq = self.get_object()
        return Response({'question': faq.questions, 'answer': faq.answers})

    @action(detail=True, methods=['put'])
    def update_faq(self, request, pk=None):
        faq = self.get_object()
        serializer = self.get_serializer(faq, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['delete'])
    def delete_faq(self, request, pk=None):
        faq = self.get_object()
        faq.delete()
        return Response({'status': 'FAQ deleted'})

    @action(detail=False, methods=['post'])
    def create_faq(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class CommentsViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer

    def get_queryset(self):
        query = super().get_queryset()
        search_data = self.request.query_params.get('search')
        if search_data:
            query = query.filter(Q(comment__icontains=search_data) | Q(rating__icontains=search_data))
        return query

    @action(detail=True, methods=['get'])
    def get_rating(self, request, pk=None):
        comment = self.get_object()
        return Response({'rating': comment.rating})

    @action(detail=True, methods=['get'])
    def get_comment(self, request, pk=None):
        comment = self.get_object()
        return Response({'comment': comment.comment})

    @action(detail=True, methods=['get'])
    def get_created_at(self, request, pk=None):
        comment = self.get_object()
        return Response({'created_at': comment.created_at})

    @action(detail=True, methods=['put'])
    def update_comment(self, request, pk=None):
        comment = self.get_object()
        serializer = self.get_serializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['delete'])
    def delete_comment(self, request, pk=None):
        comment = self.get_object()
        comment.delete()
        return Response({'status': 'comment deleted'})

    @action(detail=False, methods=['post'])
    def create_comment(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
