import sys
import modules as m

################################################################################
# Main

filename, prompt, apikey = m.parser.parse_input()

if  prompt != None:
    m.functions.decorate_title("PROMPT:")
    print("\n", prompt)
    sys.exit()

data    = m.functions.load_scheme(filename)
apikey  = m.functions.load_apikey(apikey)

menu = {
    "main": m.classes.MainMenu("category"),
    "sub":  m.classes.SubMenu("XXXXXX")
}

pack = {
    'apikey': apikey,
    'data':   data,
    'keys':   [ item for item in data.keys() ],
    'prompt': {
        'generated': "",
        'subject': "<SUBJECT NOT SET>"
    }
}

while True:
    try:
        selected = menu["main"].run(pack)
        if not selected:
            continue

        menu["sub"].run(pack, selected)
        #m.functions.handle_category(data, keys, category, new_prompt)

    except KeyboardInterrupt:
        print("[!] Quitting...")
        break
    except ValueError:
        m.functions.decorate_title("ERROR")
        print("[-] Please provide correct value")
        input("\n> Press any key to continue...")
