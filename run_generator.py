import sys
import modules as m

################################################################################
# Main

def load_data():
    filename, prompt, apikey, random = m.parser.parse_input()

    if  prompt != None:
        m.functions.decorate_title("PROMPT:")
        print("\n", prompt)
        sys.exit()

    data    = m.functions.load_scheme(filename)
    apikey  = m.functions.load_apikey(apikey)

    pack = {
        'apikey': apikey,
        'data':   data,
        'keys':   [ item for item in data.keys() ],
        'prompt': {
            'generated': "",
            'subject': "<SUBJECT NOT SET>"
        }
    }

    return pack, random

def create_menus():
    menu = {
        "main": m.classes.MainMenu("category"),
        "sub":  m.classes.SubMenu("submenu")
    }

    return menu

def main_loop(menu, pack):
    while True:
        try:
            selected = menu["main"].run(pack)

            if not selected:
                continue

            menu["sub"].run(pack, selected)

        except KeyboardInterrupt:
            print("[!] Exiting...")
            break
        except ValueError:
            m.functions.decorate_title("ERROR")
            print("[-] Please provide correct value")
            input("\n> Press any key to continue...")

if __name__ == "__main__":
    pack, random = load_data()

    if random:
        m.functions.generate_random(pack, decorate=False, confirm=False)
        sys.exit()

    menu = create_menus()
    main_loop(menu, pack)