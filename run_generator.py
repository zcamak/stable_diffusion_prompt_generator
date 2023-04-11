import os
import sys
import json
import parser
import helper

prompt, filename = parser.parse_input()

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

if prompt == None:

    while True:
        try:
            os.system("cls" if os.name == "nt" else "clear")
            keys = []
            helper.decorate_title("Category:")
            for i, item in enumerate(data.keys()):
                print(i+1, item)
                keys.append(item)
            print("-" * helper.MAX_LENGTH)
            print("[g] generate")
            print("[q] quit")
            print("-" * helper.MAX_LENGTH)

            category = input("> Please select category:\n> ")

            if category == 'q':
                print("[+] Quitting...")
                break
            elif category == 'g':
                helper.decorate_title("PROMPT:")
                print("\n", prompt)
                input("\n> Press any key to continue...")
            else:
                print("KEY: ", data[keys[int(category)]])
        except KeyboardInterrupt:
            print("[!] Program interrupted. Quitting...")
            break
        except ValueError:
            helper.decorate_title("ERROR")
            print("[-] Please provide correct value")
            input("\n> Press any key to continue...")

else:
    print("[+] Generated prompt: ", prompt)
