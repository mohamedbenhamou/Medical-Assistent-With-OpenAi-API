import openai
import gradio as gr

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a doctor"}]

def CustomChatGPT(Symptoms):
    messages.append({"role": "user", "content": Symptoms})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gr.Interface(fn=CustomChatGPT, inputs=gr.Textbox(lines=1, placeholder="Entrez vos symptomes..."), outputs = gr.Textbox(lines=1, placeholder="...."), title = "Ensem's Doctor 👨‍⚕️")

demo.launch(share=True)