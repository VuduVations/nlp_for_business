from google.colab import auth as google_auth
import vertexai
from vertexai.preview.language_models import ChatModel, InputOutputTextPair
import gradio as gr

google_auth.authenticate_user()

vertexai.init(project="bionic-water-394610", location="us-central1")

chat_model = ChatModel.from_pretrained("chat-bison@001")

parameters = {
    "temperature": .5,
    "max_output_tokens": 256,
    "top_p": 0.8,
    "top_k": 60,
    
}

# Merge the context and examples into one initialization of chat
chat = chat_model.start_chat(
    context="""""",   
    examples=[
        InputOutputTextPair(
            input_text="""""",
            output_text=""""""
        ),
                
    ]
) 

def generate_text(prompt):
    response = chat.send_message(prompt)
    return response.text

# Define Gradio Interface
interface = gr.Interface(
    fn=generate_text,  
    inputs="text",     
    outputs="text",    
    live=False,        
    title="Stoked Delivery Chat",
    description="Welcome To Stoked Delivery Chat!",
    allow_screenshots=False,
    
)

# For colab, use the `share` parameter to get a public link.
interface.launch(share=True)

