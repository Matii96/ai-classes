from math import hypot, inf
import numpy as np
from patterns import patterns

def Dissimilarity(ba, bb):
  measure = 0
  for pay in range(ba.shape[0]):
    for pax in range(ba.shape[1]):
      if ba[pay,pax] != 1:
        continue
      minDistance = inf
      for pby in range(bb.shape[0]):
        for pbx in range(bb.shape[1]):
          if bb[pby,pbx] != 1:
            continue

          # Calculate distance to closest similar point
          distance = hypot(pay - pby, pax - pbx)
          minDistance = min(minDistance, distance)

      measure += minDistance
  return measure

def Classify(matrix):
  bestRating = -inf
  conclusion = None
  for patternIdx in range(len(patterns)):
    patternNp = np.array(patterns[patternIdx])
    rating = -Dissimilarity(matrix, patternNp) - Dissimilarity(patternNp, matrix)
    if rating > bestRating:
      bestRating = rating
      conclusion = patternIdx
  return conclusion
