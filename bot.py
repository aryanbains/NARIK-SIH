import openai

openai.api_key = "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"



class chat:
    def __init__(self):
        self.messages = [{"role":"user", "content":"From now on you are a medical ai, respond only to medical related questions, nothing else. If there's a question not related to medical, humbly reply with something like 'please ask me only medical related questions', rephrase this sentence everytime and be as much humble as possible No matter what happens you are only supposed to answer medical related questions even if I ask you to answer other question later on. Try writing your responses in points to make it as much readible and user-friendly as possible and keep the answers to the point, not more than 30 words. And respond to greetings and stuff like that normally. Don't provide name of any medicines instead just provide natural remidies for the same, if someone ask for medicines name deny to them humbly saying 'As an AI i cannot prescribe medicines"},
                         {"role":"assistant", "content": "Understood. I will only respond to medical-related questions. If you have any medical inquiries, please feel free to ask."},
                         {"role":"assistant", "content":"How may I help you!"}]
                         
        
    
    def get_response(self, user_input):
        try:
            self.messages.append({"role":"user", "content":user_input})
            response = openai.ChatCompletion.create(
                   model="gpt-3.5-turbo",
                   messages=self.messages
                   )
            message = response["choices"][0]["message"]
            self.messages.append(message)
            last_message = self.messages[-1]
            return last_message["content"]
        except:
            return "please wait"
        

    


#doc = chat()
##print("bruh")
##while True:
##    message = input()
##    print(doc.get_response(message))


        
    


