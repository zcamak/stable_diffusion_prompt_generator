import random
from abc import ABC, abstractmethod
from . import functions
from . import gpt

########################################
# Abstract

class Menu(ABC):
    def __init__(self, title) -> None:
        #super().__init__()
        self.__title = title.upper()

    @abstractmethod
    def get_classname():
        pass

    @abstractmethod
    def display():
        pass

    @abstractmethod
    def handle_input():
        pass

    @abstractmethod
    def run():
        pass

########################################
# Classes

#----------------------------------------
class MainMenu(Menu):
    def __init__(self, title="MainMenu") -> None:
        super().__init__(title)
        self.__title = title

    def get_classname(self):
        return self.__title

    def run(self, pack):
        self.display(pack['data'])
        option = input("[*] Please select category:\n> ")
        return self.handle_input(pack, option)

    def display(self, data):
        functions.clear()
        functions.decorate_title(self.get_classname())
        for i, item in enumerate(data.keys()):
            print(i, item)
        functions.separator()
        print("[s] subject")
        print("[g] generate")
        print("[r] random")
        print("[q] quit")
        functions.separator()

    def handle_input(self, pack, option):
        if  option == 'q':
            raise KeyboardInterrupt

        if  option == 'g':
            self.generate_prompt(pack['prompt'], "PROMPT")
            return ""

        if  option == 's':
            self.set_subject(pack['apikey'], pack['prompt'])
            return ""

        if  option == 'r':
            self.generate_random(pack)
            return ""

        return option

    def set_subject(self, apikey, prompt):
        functions.clear()
        functions.decorate_title("subject".upper())

        if  apikey == None:
            subject = input("[*] Please write subject of prompt:\n> ")
        else:
            decision = input("[*] Do you want to ask GPT for subject?\n"
                            "(type 'y' to confirm or enter your prompt): \n> ")

            subject = gpt.prompt_gpt(apikey) if decision == 'y' else decision

        prompt['subject'] = subject

        print("[+] Subject set to:", subject)
        input("\n> Press any key to continue...")

    def generate_prompt(self, prompt, title):
        functions.decorate_title(title)

        prompt['generated'] = ""

        for item in prompt.values():
            if not item:
                continue
            prompt['generated'] += item + ", "

        print("\n" + prompt['generated'])
        input("\n> Press any key to continue...")

    def generate_random(self, pack):
        functions.clear()

        data   = pack['data']
        prompt = pack['prompt']

        if pack['apikey']:
            prompt['subject'] = gpt.prompt_gpt(pack['apikey'])

        prompt['generated'] = ""

        for category in pack['keys']:
            max   = len(data[category])
            index = random.randint(0, max - 1)

            for i, item in enumerate(data[category]):
                if i != int(index):
                    continue

                prompt[category] = item
                break

        self.generate_prompt(prompt, "RANDOM PROMPT")

#----------------------------------------
class SubMenu(Menu):
    def __init__(self, title="SubMenu") -> None:
        super().__init__(title)
        self.__title = title

    def get_classname(self):
        return self.__title

    def run(self, pack, index):
        keys   = pack['keys']
        data   = pack['data']

        self.__title = keys[int(index)]

        while True:
            self.display(data)
            option = input("[*] Please select item:\n> ")

            if  option == 'q':
                print("[+] Going back...")
                break

            if not self.handle_input(pack, index, option):
                continue

            break
        input("\n> Press any key to continue...")

    def display(self, data):
        category = self.get_classname()

        functions.clear()
        functions.decorate_title(category.upper())
        for i, item in enumerate(data[category].keys()):
            print(i, item, " - ", data[category][item])
            if  (i + 1) % 20 == 0:
                option = input("--- Press any key to continue or 'q' to quit --- ")
                if  option == 'q':
                    break
                functions.clear()
                functions.decorate_title(category.upper())

        functions.separator()
        print("[q] back")
        functions.separator()

    def handle_input(self, pack, index, option):
        keys   = pack['keys']
        data   = pack['data']
        prompt = pack['prompt']

        if  option.isnumeric() == False:
            return ""

        length = len(data[keys[int(index)]]) 

        if  int(option) >= length:
            print(f"[-] Invalid number (max: {length})")
            input("\n> Press any key to continue...")
            return ""

        category = keys[int(index)]

        for i, item in enumerate(data[category]):
            if i != int(option):
                continue

            prompt[category] = item
            print(f"[+] Category '{category}' set to: {item}")
            break

        return "done"

