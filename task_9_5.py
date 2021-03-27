class Stationery:
    def __init__(self, title="Чем будем рисовать?"):
        self.title = title


    def draw(self):
        print(f"Начнем! {self.title}")

class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки ручкой {self.title}")

class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки карандашом {self.title}")


class Marker(Stationery):
        def draw(self):
            print(f"Запуск отрисовки маркером {self.title}")


stationery = Stationery()
stationery.draw()
pen = Pen("ErichKrause")
pen.draw()
pencil = Pencil("Koh-i-Noor")
pencil.draw()
marker = Marker("Copic")
marker.draw()
