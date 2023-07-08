from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Urlinfo
from .url_support import generate_unique_id, generate_short_url


# Create your views here.
class UrlOps(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def post(self, request):
        long_url = request.data.get("longUrl")
        if long_url is None:
            return Response({"error": "Missing longUrl in requests parameter"}, status=status.HTTP_400_BAD_REQUEST)

        url = Urlinfo.objects.filter(longUrl=long_url).first()

        if url:
            response_data = {"message": "Short URL already present!",
                             "shortUrl": url.short_url}
            return Response(response_data, status=status.HTTP_200_OK)

        unique_id = generate_unique_id()
        short_url = generate_short_url(unique_id)

        url_info = Urlinfo(uuid=unique_id, shortUrl=short_url, longUrl=long_url)

        url_info.save()

        response_data = {
            "message": "URL Successfully generated"
        }

        return Response(response_data, status=status.HTTP_201_CREATED)

