# chat/views.py
from django.shortcuts import render
from django.http import JsonResponse
from openai import OpenAI
import os

# ✅ Create client using your API key from environment (PowerShell)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def chat_view(request):
    return render(request, 'chat/chat.html')


def send_message(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')

        if not user_message:
            return JsonResponse({'message': 'No message provided'}, status=400)

        try:
            # ✅ NEW OpenAI API (for versions >= 1.0)
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful study assistant."},
                    {"role": "user", "content": user_message},
                ],
            )

            ai_message = completion.choices[0].message.content
            return JsonResponse({'message': ai_message})

        except Exception as e:
            return JsonResponse({'message': f'Error: {str(e)}'}, status=500)

    return JsonResponse({'message': 'Invalid request'}, status=400)
