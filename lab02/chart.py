import matplotlib.pyplot as plt

class Chart:
    def __init__(self, id=1, equalAxes=False):
        self.seriesIdx = 0
        self.lineSeriesStyles = [('-.', 'black', 3), ('--', 'red', 2), ('-', 'blue', 1), (':', 'red', 2), ('-', 'green', 3)]
        self.pointSeriesStyles = [('o', 'orange', 40), ('^', 'magenta', 40), ('D', 'green', 40), ('*', 'red', 40), ('*', 'blue', 40)]
        plt.figure(id)
        if equalAxes:
            plt.axes().set_aspect('equal')

    def wykres_linie_rysuj(self, values_x, values_y, name=None):
        style = self.lineSeriesStyles[self.seriesIdx%5]
        plt.plot(values_x, values_y, linestyle=style[0], color=style[1], linewidth=style[2], label= name if name else None)
        self.seriesIdx += 1

    def wykres_punkty_rysuj(self, values_x, values_y, name=None):
        lenght = min(len(values_x), len(values_y))
        for i in range(0, lenght):
            style = self.pointSeriesStyles[self.seriesIdx%5]
            plt.scatter(values_x[i], values_y[i], marker=style[0], color=style[1], s=style[2], label= name if name and i == lenght-1 else None)
        self.seriesIdx += 1

    def clear(self):
        plt.clf()

    def show(self):
        plt.show()
