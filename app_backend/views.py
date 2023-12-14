from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
import json, time, datetime, threading
from queue import Queue
import dirtyjson

def _test_stream():
    for i in range(10):
        yield f"{i}. this is a test\n"
        time.sleep(1)

@api_view(['GET'])
def test_endpoint(request):
    return StreamingHttpResponse(_test_stream())

@api_view(['GET'])
def sync_test(request):
    return JsonResponse({"response": "ok"}) 