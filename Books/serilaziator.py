from rest_framework.serializers import ModelSerializer
from .models import books


class APIList(ModelSerializer):
    class Meta:
        model = books
        fields = ["id", "title", "content", "subtitle", "author", "isbn", "price"]
    
    # def validata(self,data):
    #     title=data.get("title",None)
    #     author=data.get("author",None)
        
    #     if not title.isalpha():
    #         raise ValidationError(
    #             {
    #                 "status":True,
    #                 "message":"Kitob sarlavhasi satr bo'lishi kerak"
    #             }
    #         )