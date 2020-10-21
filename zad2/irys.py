import sys
sys.path.append('..')
from absl import app, flags
from absl.flags import FLAGS
import matplotlib.pyplot as plt
import numpy as np
from chart import Chart
from zad1.fileLoader import wczytaj_baze_probek_z_tekstem

def main(_argv):
    # Irys
    probki, nazwy_atr, czy_atr_symb = wczytaj_baze_probek_z_tekstem('iris.txt', 'iris-type.txt')

    # Podział na 3 klasy
    classes = [[], [], []]
    for probka in probki:
        classIdx = int(probka[4]) - 1
        classes[classIdx].append(probka[:-1])
    classes = np.float32(np.array(classes))

    irys = Chart(2)
    ax1 = plt.subplot(221)
    ax1.set_title('atrybut 3 / 4')
    irys.wykres_punkty_rysuj(classes[0,:,2], classes[0,:,3], 'klasa 1')
    irys.wykres_punkty_rysuj(classes[1,:,2], classes[1,:,3], 'klasa 2')
    irys.wykres_punkty_rysuj(classes[2,:,2], classes[2,:,3], 'klasa 3')
    plt.legend(loc='upper right')

    ax2 = plt.subplot(222)
    ax2.set_title('atrybut 2 / 4')
    irys.wykres_punkty_rysuj(classes[0,:,1], classes[0,:,3], 'klasa 1')
    irys.wykres_punkty_rysuj(classes[1,:,1], classes[1,:,3], 'klasa 2')
    irys.wykres_punkty_rysuj(classes[2,:,1], classes[2,:,3], 'klasa 3')
    plt.legend(loc='upper right')

    ax2 = plt.subplot(223)
    ax2.set_title('atrybut 1 / 4')
    irys.wykres_punkty_rysuj(classes[0,:,0], classes[0,:,3], 'klasa 1')
    irys.wykres_punkty_rysuj(classes[1,:,0], classes[1,:,3], 'klasa 2')
    irys.wykres_punkty_rysuj(classes[2,:,0], classes[2,:,3], 'klasa 3')
    plt.legend(loc='upper right')

    ax2 = plt.subplot(224)
    ax2.set_title('atrybut 2 / 3')
    irys.wykres_punkty_rysuj(classes[0,:,1], classes[0,:,2], 'klasa 1')
    irys.wykres_punkty_rysuj(classes[1,:,1], classes[1,:,2], 'klasa 2')
    irys.wykres_punkty_rysuj(classes[2,:,1], classes[2,:,2], 'klasa 3')
    plt.legend(loc='upper right')

    irys.show()

if __name__ == '__main__':
    app.run(main)
