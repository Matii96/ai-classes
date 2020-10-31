from absl import app, flags
from absl.flags import FLAGS
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math
from maximum11 import Maximum11

flags.DEFINE_string('function', 'math.sin(x/10)*math.sin(x/200)', '')
flags.DEFINE_integer('dispersion', 10, '')
flags.DEFINE_float('growth_factor', 1.5, '')
flags.DEFINE_integer('variation_min', 0, '')
flags.DEFINE_integer('variation_max', 100, '')
flags.DEFINE_integer('iterations', 100, '')

xProgress, yProgress = [], []
bestResult = None

def Animate(frameIdx):
  global bestResult
  if bestResult:
    bestResult.remove()
  bestResult = plt.scatter(xProgress[frameIdx]['x'], yProgress[frameIdx], marker='*', s=50, color='green', label='best result')
  plt.legend(loc='upper right')
  plt.title('Iteration {} ({:.1f},{:.1f}): dispersion={:.2f}'.format(frameIdx+1, xProgress[frameIdx]['x'], yProgress[frameIdx], xProgress[frameIdx]['dispersion']))


def main(_argv):
  # Calculate main function values
  xVector = list(np.linspace(FLAGS.variation_min, FLAGS.variation_max, 100))
  yVector = [eval(FLAGS.function) for x in xVector]

  # Find minimum and way to achieve it
  global yProgress
  minimum = Maximum11(FLAGS.function, FLAGS.dispersion, FLAGS.growth_factor, (FLAGS.variation_min, FLAGS.variation_max), FLAGS.iterations, xProgress)
  yProgress = [eval(FLAGS.function) for x in map(lambda stage: stage['x'], xProgress)]

  # Show chart
  fig = plt.figure(1)
  plt.plot(xVector, yVector, label='function')
  anim = animation.FuncAnimation(fig, Animate, frames=FLAGS.iterations, repeat=False, interval=500)
  plt.show()

if __name__ == '__main__':
  app.run(main)
