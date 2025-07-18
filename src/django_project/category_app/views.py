from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK

class CategoryViewSet(viewsets.ViewSet):
    def list(self, request: Request)-> Response:
        return Response(
            status= HTTP_200_OK,
            data = [
                {
                    "id":"8227aa2b-6098-43d5-82e8-debd9536785b",
                    "name":"Movie",
                    "description":"Movie descritption",
                    "is_active": True
                },
                {
                    "id":"4c01e326-25af-44ee-9d0c-ea6a6b454e3b",
                    "name":"Documentary",
                    "description":"Documentary descritption",
                    "is_active": True
                 },
            ]
        ) 