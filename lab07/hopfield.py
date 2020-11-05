import numpy as np
from math import sqrt

def ConvertInputArray(array, pixelsCount):
  arrayConverted = np.where(array<=0, -1, 1)
  arrayConverted = arrayConverted.reshape(pixelsCount)
  return arrayConverted

def Train(patterns):
  firstPattern = np.array(patterns[0])
  pixelsCount = firstPattern.shape[0] * firstPattern.shape[1]

  # Convert arrays to vectors
  patternsConverted = np.array([ConvertInputArray(np.array(pattern), pixelsCount) for pattern in patterns])

  # Initial weights matrix
  weights = np.zeros((pixelsCount, pixelsCount))

  # Correct weights
  for i in range(pixelsCount):
    for j in range(pixelsCount):
      if i != j:
        for p in range(patternsConverted.shape[0]):
          weights[i, j] += patternsConverted[p, i] * patternsConverted[p, j]
      else:
        weights[i, j] = 0
  weights /= pixelsCount

  return weights

def Correct(weights, array, iterations=5):
  pixelsCount = array.shape[0]*array.shape[1]
  correctedArray = ConvertInputArray(array, pixelsCount)

  change = np.empty((pixelsCount))
  for _ in range(iterations):
    for i in range(pixelsCount):
      change[i] = 0
      for j in range(pixelsCount):
        change[i] += correctedArray[j] * weights[i, j]
    correctedArray = np.where(change<0, -1, 1)

  correctedArray = np.where(correctedArray==-1, 0, 1).reshape(array.shape[0], array.shape[1])
  return correctedArray
