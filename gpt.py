import openai

input = "Hello!"

def chatgpt(input, token):
    openai.api_key = token
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": input }, 
        ]
    )
    print(f'\n\nGPT-3.5:\n{response["choices"][0]["message"]["content"]}\n\n') #返信のみを出力