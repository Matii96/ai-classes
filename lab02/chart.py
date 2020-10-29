import matplotlib.pyplot as plt

class Chart:
    def __init__(self, id=1):
        self.seriesIdx = 0
        self.lineSeriesStyles = [('-.', 'black', 3), ('--', 'red', 2), ('-', 'blue', 1), (':', 'red', 2), ('-', 'green', 3)]
        self.pointSeriesStyles = [('o', 'orange', 25), ('^', 'black', 30), ('D', 'green', 25), ('*', 'red', 25), ('*', 'blue', 30)]
        plt.figure(id)
        plt.axes().set_aspect('equal')

    def wykres_linie_rysuj(self, wartosci_x, wartosci_y, nazwa=None):
        lenght = min(len(wartosci_x), len(wartosci_y)) - 1
        for i in range(0, lenght):
            style = self.lineSeriesStyles[self.seriesIdx%5]
            line = plt.plot(
                (wartosci_x[i], wartosci_x[i+1]),
                (wartosci_y[i], wartosci_y[i+1])
            , linestyle=style[0], color=style[1], linewidth=style[2], label= nazwa if nazwa and i == lenght-1 else None)
        self.seriesIdx += 1

    def wykres_punkty_rysuj(self, wartosci_x, wartosci_y, nazwa=None):
        lenght = min(len(wartosci_x), len(wartosci_y))
        for i in range(0, lenght):
            style = self.pointSeriesStyles[self.seriesIdx%5]
            plt.scatter(wartosci_x[i], wartosci_y[i], marker=style[0], color=style[1], s=style[2], label= nazwa if nazwa and i == lenght-1 else None)
        self.seriesIdx += 1

    def clear(self):
        plt.clf()

    def show(self):
        plt.show()
