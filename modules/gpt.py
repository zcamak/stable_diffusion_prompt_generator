import openai

def prompt_gpt(apikey):
    model = "gpt-3.5-turbo"
    msg = [
        {
          "role": "user",
          "content": "Create a subject for a prompt for AI image generator Stable Diffusion. It should be one sentence and no longer than 7 words."
        }
    ]

    openai.api_key = apikey

    print("[+] Waiting for GPT response...")
    response = openai.ChatCompletion.create(model=model, messages=msg)
    subject = response.choices[0].message.content
    subject = subject.strip('",.?!')

    return subject
