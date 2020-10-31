import sys
sys.path.append('..')
from absl import app, flags
from absl.flags import FLAGS
import matplotlib.pyplot as plt
import numpy as np
from chart import Chart
from lab01.fileLoader import wczytaj_baze_probek_z_tekstem

def main(_argv):
    # Uśmiech
    usmiech = Chart(None, True)
    x = np.linspace(-2, 2, 8)
    y = (x+2)*(x-2)
    x = np.concatenate((x, np.flip(x, 0)))
    y = np.concatenate((y, np.flip(-y, 0)))
    usmiech.wykres_linie_rysuj(x, y, 'glowa')
    usmiech.wykres_linie_rysuj([-1, 0, 1], [0, -1, 0], 'usmiech')
    usmiech.wykres_punkty_rysuj([-1, 0, 1], [1, 0, 1], 'oczy i usta')
    plt.legend(loc='upper right')
    usmiech.show()

if __name__ == '__main__':
    app.run(main)
