import time
import itertools
from colorama import Fore


class TrafficLight:
    __color = "красный"

    def running(self):
        while True:
            print(Fore.RED + "Красный")
            time.sleep(7)
            print(Fore.YELLOW + "Желтый")
            time.sleep(2)
            print(Fore.GREEN + "Зеленый")
            time.sleep(5)
            print(Fore.YELLOW + "Желтый")
            time.sleep(2)


trafficlight = TrafficLight()
trafficlight.running()