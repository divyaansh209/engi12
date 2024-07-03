from openai import OpenAI
import gradio

openai = OpenAI(
    api_key='sk-proj-0CuVbPdMikmBOGxzyL40T3BlbkFJxrPKzb1Oiph0KI71ES2v',
)

initial_message = "Act like a Design Engineering Expert giving guide to design students. "
conversation = [{"role": "user", "content": initial_message}]

def get_gpt_response(You):
    message = {
        "role": "user",
        "content": You
    }
    conversation.append(message)
    response = openai.chat.completions.create(
        messages = conversation,
        model  =  "gpt-3.5-turbo"
    )
    conversation.append(response.choices[0].message)
    return response.choices[0].message.content





app = gradio.Interface(fn = get_gpt_response, inputs = ["text"], outputs="text", title = "EngiChat AI",     examples=[
        ["What is the difference between AC and DC current?"],
        ["A sample HTML code for a website. "],
        ["What is Mechatronics?"],
    ])
app.launch(share= True)
