from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from sentence_transformers import SentenceTransformer
from transformers import MT5ForConditionalGeneration, MT5Tokenizer

from core import main

class ViewController(APIView):
    FINAL_STATE = "END2"
    buttons = []
   
    def post(self, request):
        message = json.loads(request.body.decode('utf-8'))["message"]
        page, res, ViewController.buttons = main.information_retrieval_module(message)
        return Response({"status": "success", "page": page, "response": res, "buttons": ViewController.buttons},
                        status=status.HTTP_200_OK)