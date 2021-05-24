from time import sleep
import os


def clear_console():
    """
    Clear console.
     os.name == nt in Windows system and posix in Mac and Linux
    :return:
    """
    os.system('cls' if os.name == 'nt' else 'clear')


class TrafficLightColorError(Exception):
    def __init__(self, color):
        self.message = f' "{color}" is not traffic light color!'
        super().__init__(self.message)


class TrafficLight:
    __color = {
        'red': (7, '\033[31m'),
        'yellow': (2, '\033[33m'),
        'green': (8, '\033[32m')
    }

    __color_order = ('red', 'yellow', 'green')

    def __init__(self, color='red'):
        color = color.lower()
        if not self.__color.get(color):
            raise TrafficLightColorError(color)

        self.__counter = self.__color.get(color)[0]
        self.__current_color = color

    def __change_light(self, color):
        color_index = self.__color_order.index(color) + 1
        if color_index > (len(self.__color_order) - 1):
            color_index = 0

        self.__current_color = self.__color_order[color_index]
        self.__counter = self.__color.get(self.__current_color)[0]

    def __set_text_color(self):
        print(f'{self.__color[self.__current_color][1]}', end='')

    def running(self):
        self.__set_text_color()

        while True:
            if self.__counter <= 0:
                self.__change_light(self.__current_color)
                self.__set_text_color()

            # clear_console()

            print(f"{self.__counter}")
            self.__counter -= 1
            sleep(1)


trafic_light = TrafficLight('green')
trafic_light.running()
