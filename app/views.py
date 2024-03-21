from openai import OpenAI

from decouple import config
from django.shortcuts import render


def chatbot(request):
    api_key = config('OPENAI_APIKEY')
    client = OpenAI(api_key=api_key)

    if api_key and request.method == 'POST':
        user_input = request.POST.get('user_input')
        prompt = user_input
        # response = client.completions.create(engine='text-davinci-003',
        #                                      # prompt=prompt,
        #                                      prompt=f'translate this text to persian{prompt}',
        #                                      max_tokens=256,
        #                                      # stop='.'
        #                                      temperature=0.5)
        response = client.completions.create(model="gpt-3.5-turbo", prompt=f'translate this text to persian{prompt}')
        print(response)
        chatbot_response = response.choices[0].text
        return render(request, 'main.html', {"response": chatbot_response})
    return render(request, 'main.html', {})
