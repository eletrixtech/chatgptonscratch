import openai
import scratchattach as scratch3
#Add api key openai


openai.api_key = 'API-KEY'

def generate_text(prompt):
    try:
        # Appel de l'API de GPT-3 pour générer la réponse
        response = openai.Completion.create(
            engine='davinci',
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )

      
        return response.choices[0].text
    except Exception as e:
     
       
        return "Error", e
        




session = scratch3.Session("SESSION ID ", username="USERNAME") #replace with your session_id and username
conn = session.connect_cloud("PROJECTID") #replace with your project id

client = scratch3.CloudRequests(conn)

@client.request
def foo(argument1):
    print(f"Data requested for user {argument1}")
    


    return generate_text(prompt=argument1)

@client.event
def on_ready():
    print("Request handler is running")

client.run() #make sure this is ALWAYS at the bottom of your Python file
