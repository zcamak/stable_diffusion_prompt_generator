from abc import ABC, abstractmethod
from . import functions

class Menu(ABC):
    def __init__(self, title) -> None:
        #super().__init__()
        self.title = title.upper()

    @abstractmethod
    def display():
        pass

    @abstractmethod
    def handle_input():
        pass

class MainMenu(Menu):
    def __init__(self, title="MainMenu") -> None:
        super().__init__(title)

    def display(self, data, keys):
        functions.clear()
        functions.decorate_title(self.title)
        for i, item in enumerate(data.keys()):
            print(i, item)
            keys.append(item)
        functions.separator()
        print("[s] subject")
        print("[g] generate")
        print("[q] quit")
        functions.separator()

        return input("[*] Please select category:\n> ")

    def handle_input(self):
        pass

class SubMenu(Menu):
    def __init__(self, title="SubMenu") -> None:
        super().__init__(title)