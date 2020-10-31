from absl import app, flags
from absl.flags import FLAGS
import matplotlib.pyplot as plt
import numpy as np
import math
from pso import Pso

flags.DEFINE_string('function', 'math.sin(x[0]*0.05)+math.sin(x[1]*0.05)+0.4*math.sin(x[0]*0.15)*math.sin(x[1]*0.15)', '')
flags.DEFINE_integer('individuals_count', 4, '')
flags.DEFINE_float('inertion', 0.2, '')
flags.DEFINE_float('rglob', 0.3, '')
flags.DEFINE_float('rloc', 0.3, '')
flags.DEFINE_integer('variation_min', 0, '')
flags.DEFINE_integer('variation_max', 100, '')
flags.DEFINE_integer('iterations', 40, '')

def EvalFunction(X, Y):
  result = np.empty(X.shape)
  for i in range(len(X)):
    for j in range(len(X[i])):
      x = (X[i,j], Y[i,j])
      result[i,j] = eval(FLAGS.function)
  return result

def main(_argv):
  maximum = Pso(FLAGS.function, FLAGS.individuals_count, FLAGS.inertion, FLAGS.rglob, FLAGS.rloc,
    (FLAGS.variation_min, FLAGS.variation_min), (FLAGS.variation_max, FLAGS.variation_max), FLAGS.iterations)

  x = np.linspace(FLAGS.variation_min, FLAGS.variation_max, 100)
  y = np.linspace(FLAGS.variation_min, FLAGS.variation_max, 100)
  X, Y = np.meshgrid(x, y)
  Z = EvalFunction(X, Y)

  ax = plt.axes(projection='3d')
  ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

  x = maximum
  z = eval(FLAGS.function)
  ax.scatter3D(maximum[0], maximum[1], z, marker='*', s=400, color='red', label='best result')

  plt.legend(loc='upper right')
  plt.title('PSO maximum for ' + FLAGS.function)
  plt.show()

if __name__ == '__main__':
  app.run(main)
