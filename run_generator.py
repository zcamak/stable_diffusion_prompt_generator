import sys
import modules as m

################################################################################
# Main

new_prompt  = {}
subject     = "<SUBJECT NOT SET>"

filename, prompt, apikey = m.parser.parse_input()

if  prompt != None:
    functions.decorate_title("PROMPT:")
    print("\n", prompt)
    sys.exit()

data    = m.functions.load_scheme(filename)
apikey  = m.functions.load_apikey(apikey)

while True:
    try:
        keys = []
        category = m.functions.main_menu(data, keys)

        if  category == 'q':
            raise KeyboardInterrupt

        if  category == 'g':
            prompt = m.functions.generate_prompt(subject, new_prompt)
            continue

        if  category == 's':
            subject = m.functions.get_subject(apikey)
            continue

        m.functions.handle_category(data, keys, category, new_prompt)

    except KeyboardInterrupt:
        print("[!] Quitting...")
        break
    except ValueError:
        functions.decorate_title("ERROR")
        print("[-] Please provide correct value")
        input("\n> Press any key to continue...")
