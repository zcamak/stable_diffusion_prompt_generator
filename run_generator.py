import os
import sys
import json
import openai
import parser
import helper

################################################################################
# Functions

def separator():
    print("-" * helper.MAX_LENGTH)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def main_menu():
    clear()
    helper.decorate_title("Category:")
    for i, item in enumerate(data.keys()):
        print(i, item)
        keys.append(item)
    separator()
    print("[s] subject")
    print("[g] generate")
    print("[q] quit")
    separator()

    return input("[*] Please select category:\n> ")

def sub_menu(index):
    clear()
    helper.decorate_title(index.upper())
    for i, item in enumerate(data[index].keys()):
        print(i, item, " - ", data[index][item])
        if (i + 1) % 20 == 0:
            request = input("--- Press any key to continue or 'q' to quit --- ")
            if request == 'q':
                break
            clear()
            helper.decorate_title(index.upper())

    separator()
    print("[q] quit")
    separator()

    return input("[*] Please select item:\n> ")

def get_subject(apikey):
    clear()
    helper.decorate_title("subject".upper())

    print("API:", apikey)
    if apikey == None:
        subject = input("[*] Please write subject of prompt:\n> ")
    else:
        subject = input("[*] Do you want to ask GPT for subject?\n(type 'y' to confirm, otherwise enter your prompt): \n> ")

        if subject == 'y':
            openai.api_key = apikey

            model = "gpt-3.5-turbo"
            msg = [
                {
                  "role": "user",
                  "content": "Create a subject for a prompt for AI image generator Stable Diffusion. It should be one sentence and no longer than 7 words."
                }
            ]

            print("[+] Waiting for GPT response...")
            response = openai.ChatCompletion.create(model=model, messages=msg)
            subject = response.choices[0].message.content
            subject = subject.strip('"')

    return subject
################################################################################
# Main

prompt, filename, apikey = parser.parse_input()

if filename == None:
    filename = "prompt_scheme.json"

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

if apikey == None:
    try:
        with open("openai.key","r") as apifile:
            apikey = apifile.read().strip()
    except FileNotFoundError:
      print(f"[-] Failed to open openai.key")
      print("[!] Not using OpenAI API")

new_prompt = {}
subject = "<SUBJECT NOT SET>"

if prompt == None:

    while True:
        try:
            keys = []
            category = main_menu()

            if category == 'q':
                print("[+] Quitting...")
                break
            elif category == 'g':
                helper.decorate_title("PROMPT:")
                prompt = ""
                for item in new_prompt.values():
                    prompt += item + ", "
                print("\n", subject + ",", prompt)
            elif category == 's':
                subject = get_subject(apikey)
                print("[+] Subject set to:", subject)
            else:
                while True:
                    requested = sub_menu(keys[int(category)])

                    if requested == 'q':
                        print("[+] Going back...")
                        break
                    elif requested.isnumeric() == True:
                        datalength = len(data[keys[int(category)]]) 
                        if int(requested) >= datalength:
                            print(f"[-] Invalid number (max: {datalength})")
                            input("\n> Press any key to continue...")
                            continue
                            
                        category_key = keys[int(category)]
                        for i, item in enumerate(data[category_key]):
                            if i == int(requested):
                                new_prompt[category_key] = item
                                print(f"[+] Category '{category_key}' set to: {item}")
                                break
                        #input("\n> Press any key to continue...")
                        break
            input("\n> Press any key to continue...")
        except KeyboardInterrupt:
            print("[!] Program interrupted. Quitting...")
            break
        except ValueError:
            helper.decorate_title("ERROR")
            print("[-] Please provide correct value")
            input("\n> Press any key to continue...")

else:
    print("[+] Generated prompt: ", prompt)
