import google.generativeai as palm
from creds import palmpi
from creds import palmpi
palm.configure(api_key=palmpi)


with open('context.txt', 'r', encoding='utf-8') as f:
    contexts = f.read()

    

def chatty(message,palm=palm, contexts=contexts,response=None):
    if response is None:
        response = palm.chat(context=contexts, messages=message)
    else:
        response = response.reply(message)

    return response.last
