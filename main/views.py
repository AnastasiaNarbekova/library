from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from main.models import Book, Order
from main.serializers import BookSerializer, OrderSerializer


@api_view(['GET'])
def books_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class CreateBookView(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'Книга успешно создана'}, status=status.HTTP_201_CREATED)


class BookDetailsView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer