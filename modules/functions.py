import os
import json
import sys
import random
from . import gpt

################################################################################
# Constants

MAX_LENGTH = 40 

################################################################################
# Functions

def separator():
    print("-" * MAX_LENGTH)

def clear():
    os.system("cls" if  os.name == "nt" else "clear")
 
def decorate_title(title):
    length = len(title)
    diff   = MAX_LENGTH - length
    diff   = int(diff / 2 - 1)
    if diff * 2 + length + 2 != MAX_LENGTH:
        additional = 1
    else:
        additional = 0
    print("#" * MAX_LENGTH)
    print("#" + " " * diff + title + " " * (diff + additional)+ "#")
    print("#" * MAX_LENGTH)
   
def load_scheme(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"[-] Failed to open {filename}")
        sys.exit()
    except Exception as e:
        print("[-] ERROR!: {e}")
        sys.exit()
    finally:
        f.close()
        return data

def load_apikey(apikey):
    if  apikey == None:
        try:
            with open("openai.key","r") as apifile:
                apikey = apifile.read().strip()
        except FileNotFoundError:
            print("[-] Failed to open openai.key")
            print("[!] Not using OpenAI API")

    return apikey

def set_subject(apikey, prompt):
    clear()
    decorate_title("subject".upper())

    if  apikey == None:
        subject = input("[*] Please write subject of prompt:\n> ")
    else:
        decision = input("[*] Do you want to ask GPT for subject?\n"
                        "(type 'y' to confirm or enter your prompt): \n> ")

        subject = gpt.prompt_gpt(apikey) if decision == 'y' else decision

    prompt['subject'] = subject

    print("[+] Subject set to:", subject)
    input("\n> Press any key to continue...")

def generate_prompt(prompt, title, decorate=True, confirm=True):
    if decorate:
        decorate_title(title)

    prompt['generated'] = ""

    for item in prompt.values():
        if not item:
            continue
        prompt['generated'] += item + ", "

    print("\n" + prompt['generated'])

    if confirm:
        input("\n> Press any key to continue...")

def generate_random(pack, decorate=True, confirm=True):
    if decorate:
        clear()

    data   = pack['data']
    prompt = pack['prompt']

    if pack['apikey']:
        prompt['subject'] = gpt.prompt_gpt(pack['apikey'], decorate)

    prompt['generated'] = ""

    for category in pack['keys']:
        max   = len(data[category])
        index = random.randint(0, max - 1)

        for i, item in enumerate(data[category]):
            if i != int(index):
                continue

            prompt[category] = item
            break

    generate_prompt(prompt, "RANDOM PROMPT", decorate, confirm)