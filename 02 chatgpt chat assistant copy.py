from openai import OpenAI
import os

modelGPT = "gpt-3.5-turbo"
#modelGPT = "gpt-4o-mini"

#obfuscated API Key
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)
messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while input != "quit()":
   
    message = input()
    messages.append({"role": "user", "content": message})
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream = True
    
    )

    reply = ""

    for chunk in stream:
        if chunk.choices[0].delta.content != None:
            reply += chunk.choices[0].delta.content


    print("The reply - "+ reply)

    #reply = stream.choices[0].delta.content
    #messages.append({"role": "assistant", "content": reply})



#for blerb in reply:
   # print(blerb)