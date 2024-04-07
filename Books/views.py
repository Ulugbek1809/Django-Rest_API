# from django.shortcuts import render
# from rest_framework import generics
from .models import books
from .serilaziator import APIList
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


class all(ModelViewSet):
    queryset = books.objects.all()
    serializer_class = APIList


class booksviev(APIView):
    def get(self, request):
        book = books.objects.all()
        ser = APIList(book, many=True).data
        context = {
            "status": True,
            "Books": ser
        }
        return Response(context)


class bookdetail(APIView):
    def get(self, request, pk):
        try:
            book = books.objects.get(id=pk)
            context = {
                "status": True,
                "Books": APIList(book).data
            }
            return Response(context)
        except:
            return Response({"status": False, "message": "bunday kitob mavjud emas !"},
                            status=status.HTTP_404_NOT_FOUND)


class bookdelete(APIView):
    def delete(self, request, pk):
        try:
            book = books.objects.get(id=pk)
            book.delete()
            context = {
                "status": True,
                "message": "Kitob o'chirildi."
            }
            return Response(context, status=status.HTTP_200_OK)
        except:
            context = {
                "status": False,
                "message": "Kitob topilmadi."
            }
            return Response(context, status=status.HTTP_404_NOT_FOUND)


class bookupdata(APIView):
    def post(self, request, pk):
        book = get_object_or_404(books.objects.all(), id=pk)
        data = request.data
        ser = APIList(instance=book, data=data, partial=True)
        if ser.is_valid(raise_exception=True):
            book_saved = ser.save()
            return Response({
                "status": True,
                "message": f"{book_saved} yangilandi."
            })


class bookcreate(APIView):
    def post(self, request):
        data = request.data
        ser = APIList(data=data)
        if ser.is_valid():
            ser.save()
            return Response({
                "status": True,
                "message": f"kitob bazaga saqlandi."
            })

# class APIViews(generics.ListAPIView):
#     queryset = books.objects.all()
#     serializer_class = APIList
#
#
# class APIretryupdatedeletel(generics.RetrieveUpdateDestroyAPIView):
#     queryset = books.objects.all()
#     serializer_class = APIList
#
#
# class APICreate(generics.CreateAPIView):
#     queryset = books.objects.all()
#     serializer_class = APIList
# # Create your views here.
