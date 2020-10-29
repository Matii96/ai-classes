import sys
sys.path.append('..')
from absl import app, flags
from absl.flags import FLAGS
import matplotlib.pyplot as plt
import matplotlib.animation as animation 
import numpy as np
from lab01.fileLoader import wczytaj_baze_probek_z_tekstem
from lab02.chart import Chart
from convert import probki_str_na_liczby
from kmeans import Kmeans

flags.DEFINE_integer('liczba_grup', 4, '')
flags.DEFINE_integer('iteracje', 100, '')

chart = Chart()
progress = []
grupy, osrodki = [], []

def Animate(frameIdx):
  groups = progress[frameIdx]['groups']
  centers = progress[frameIdx]['centers']
  chart.clear()

  for i in range(len(groups)):
    group = np.array(groups[i])
    chart.wykres_punkty_rysuj(group[:,0], group[:,1], 'grupa {}'.format(i))

  # Naniesienie ośrodków
  centersNp = np.array(centers)
  chart.wykres_punkty_rysuj(centersNp[:,0], centersNp[:,1], 'ośrodki')

  plt.legend(loc='upper right')
  plt.title('Iteracja {}'.format(frameIdx+1))

def main(_argv):
  probki_string, nazwy_atr, czy_atr_symb = wczytaj_baze_probek_z_tekstem('spirala.txt', 'spirala-type.txt')
  probki = probki_str_na_liczby(probki_string, (0,1))
  grupy, osrodki = Kmeans(probki, FLAGS.liczba_grup, FLAGS.iteracje, progress)

  fig = plt.figure(1)
  anim = animation.FuncAnimation(fig, Animate, frames=len(progress), repeat=False, interval=500)
  chart.show()

if __name__ == '__main__':
  app.run(main)
