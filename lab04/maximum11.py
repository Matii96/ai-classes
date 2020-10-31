from random import uniform
import math

def maximum11(function, dispersion, growthFactor, variation, iterations=100, progress=None):
  x = uniform(variation[0], variation[1])
  y = eval(function)
  xBest = x
  yBest = y

  for i in range(iterations):
    x = xBest + uniform(-dispersion, dispersion)
    x = min(max(x, variation[0]), variation[1])
    y = eval(function)
    if y >= yBest:
      xBest, yBest = x, y
      dispersion *= growthFactor
    else:
      dispersion /= growthFactor
    
    if not progress is None:
      progress.append({'x': xBest, 'dispersion': dispersion})

  return xBest
