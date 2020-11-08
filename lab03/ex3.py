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
from fuzzy_kmeans import fuzzy_kmeans

flags.DEFINE_integer('groups', 3, '')
flags.DEFINE_integer('iterations', 100, '')
flags.DEFINE_float('fcm', 1.5, '')

chart = Chart()
progress = []
samples = []

def Animate(frame_idx):
  groups = progress[frame_idx]['groups']
  centers = progress[frame_idx]['centers']
  chart.clear()

  # Assign samples to closest groups
  samples_groups = [[] for _ in range(len(groups))]
  for sample_idx in range(len(samples)):
    largest_participation_idx = None
    largest_participation_value = -1
    for group_idx in range(len(groups)):
      if groups[group_idx, sample_idx] > largest_participation_value:
        largest_participation_value = groups[group_idx, sample_idx]
        largest_participation_idx = group_idx

    samples_groups[largest_participation_idx].append(samples[sample_idx])

  for i in range(len(samples_groups)):
    if len(samples_groups[i]) == 0:
      continue

    samples_group_np = np.array(samples_groups[i])
    chart.wykres_punkty_rysuj(samples_group_np[:,0], samples_group_np[:,1], 'group {}'.format(i+1))

  chart.wykres_punkty_rysuj(centers[:,0], centers[:,1], 'centers')

  plt.legend(loc='upper right')
  plt.title('Iteration {}'.format(frame_idx+1))

def main(_argv):
  probki_string, nazwy_atr, czy_atr_symb = wczytaj_baze_probek_z_tekstem('spirala.txt', 'spirala-type.txt')

  global samples
  samples = probki_str_na_liczby(probki_string, (0,1))
  fuzzy_kmeans(samples, FLAGS.groups, FLAGS.iterations, FLAGS.fcm, progress)

  fig = plt.figure(1)
  anim = animation.FuncAnimation(fig, Animate, frames=len(progress), repeat=False, interval=500)
  chart.show()

if __name__ == '__main__':
  app.run(main)
