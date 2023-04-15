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
            functions.generate_prompt(pack['prompt'], "PROMPT")
            return ""

        if  option == 's':
            functions.set_subject(pack['apikey'], pack['prompt'])
            return ""

        if  option == 'r':
            functions.generate_random(pack)
            return ""

        return option

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

