from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from sentence_transformers import SentenceTransformer
from transformers import MT5ForConditionalGeneration, MT5Tokenizer

from core import main

class Chat(APIView):
    state = "GREETING"
    FINAL_STATE = "END2"
    buttons = []
    previous_questions_embeddings = []
   
    def post(self, request):
        message = json.loads(request.body.decode('utf-8'))["message"]
        if message == "restart":
            Chat.state = "GREETING"
        res, Chat.state, Chat.buttons, Chat.previous_questions_embeddings = main.information_retrieval_module(Chat.state, message, Chat.previous_questions_embeddings)
        if Chat.state != Chat.FINAL_STATE:
            return Response({"status": "success", "response": res, "buttons": Chat.buttons},
                            status=status.HTTP_200_OK)
        return Response({"status": "end", "response":  "امیدوارم تونسته باشم کمکت کنم.", "buttons": Chat.buttons}, status=status.HTTP_200_OK)
