class Stationery:
    title = ''

    def draw(self):
        print('Start drawing!')


class Pen(Stationery):
    def draw(self):
        print('Start drawing with a Pen!')


class Pencil(Stationery):
    def draw(self):
        print('Start drawing with a Pencil!')


class Handle(Stationery):
    def draw(self):
        print('Start drawing with a Handle!')


s = Stationery()
s.draw()

pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
