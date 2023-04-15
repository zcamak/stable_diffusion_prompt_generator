import os
import json
import sys

################################################################################
# Constants

MAX_LENGTH = 40 

################################################################################
# Functions

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

def separator():
    print("-" * MAX_LENGTH)

def clear():
    os.system("cls" if  os.name == "nt" else "clear")
    
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

def handle_category(data, keys, category, new_prompt):
    while True:
        requested = "a" #sub_menu(data, keys[int(category)])

        if  requested == 'q':
            print("[+] Going back...")
            break

        if  requested.isnumeric() == False:
            continue

        datalength = len(data[keys[int(category)]]) 

        if  int(requested) >= datalength:
            print(f"[-] Invalid number (max: {datalength})")
            input("\n> Press any key to continue...")
            continue
            
        category_key = keys[int(category)]

        for i, item in enumerate(data[category_key]):
            if  i != int(requested):
                continue

            new_prompt[category_key] = item
            print(f"[+] Category '{category_key}' set to: {item}")
            break
        break

    input("\n> Press any key to continue...")

