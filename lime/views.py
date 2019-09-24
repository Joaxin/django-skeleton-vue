from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
 
from .models import Bookmark, Category

# Create your views here.
# @require_http_methods(["GET"])
# def add_link(request):
#     response = {}
#     try:
#         link = Bookmark(
#             author=request.user, 
#             title=request.GET.get('title'),
#             url=request.GET.get('url',"https://www.baidu.com"),
#             ico=request.GET.get('ico',"https://github.com/fluidicon.png"),
#             description=request.GET.get('description',""), 
#             category=Category(request.GET.get('name')),
#             # is_pubic=request.GET.get('is_public'), 
#             # tags=request.GET.get('tags',"1,2,3"),
#             )
#         link.save()
#         response['msg'] = 'success'
#         response['error_num'] = 0
#     except  Exception as e:
#         response['msg'] = str(e)
#         response['error_num'] = 1
#     return JsonResponse(response)
 
 
# @require_http_methods(["GET"])
# def show_links(request):
#     response = {}
#     try:
#         links = Bookmark.objects.filter(author=request.user)
#         response['list'] = json.loads(serializers.serialize("json", links))
#         response['msg'] = 'success'
#         response['error_num'] = 0
#     except  Exception as e:
#         response['msg'] = str(e)
#         response['error_num'] = 1

