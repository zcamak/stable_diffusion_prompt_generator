import openai

def prompt_gpt(apikey, decorate=True):
    if decorate:
        print("[+] Waiting for GPT response...")

    model = "gpt-3.5-turbo"
    msg = [
        {
          "role": "user",
          "content": "Create a subject for a prompt for AI image generator Stable Diffusion. It should be one sentence and no longer than 10 words."
        }
    ]

    openai.api_key = apikey

    response = openai.ChatCompletion.create(model=model, messages=msg)
    subject = response.choices[0].message.content
    subject = subject.strip('",.?!')

    return subject
