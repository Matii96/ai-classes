from math import hypot, inf
import random

def Kmeans(data, groupsCount, iterations=100, progress=None):
  assignments = [-1 for _ in range(len(data))]
  groupsCenters = random.sample(data, groupsCount)

  for iteration in range(iterations):
    for s in range(len(data)):
      sample = data[s]

      # Find closest group to given sample
      closestGroupIdx = 0
      minDistance = inf
      for j in range(groupsCount):
        groupCenter = groupsCenters[j]
        distance = hypot(groupCenter[0] - sample[0], groupCenter[1] - sample[1])
        if distance < minDistance:
          minDistance = distance
          closestGroupIdx = j

      # Assign sample
      assignments[s] = closestGroupIdx

      # Recalculate closest group center
      xValues = []
      yValues = []
      for i in range(len(assignments)):
        if assignments[i] == closestGroupIdx:
          xValues.append(data[i][0])
          yValues.append(data[i][1])
      x = sum(xValues) / len(xValues)
      y = sum(yValues) / len(yValues)
      groupsCenters[closestGroupIdx] = (x, y)
    
    if not progress is None:
      groups = [[] for _ in range(groupsCount)]
      for s in range(len(data)):
        groups[assignments[s]].append(data[s])
      progress.append({ 'groups': groups, 'centers': groupsCenters.copy() })

  # Parse result
  groups = [[] for _ in range(groupsCount)]
  for s in range(len(data)):
    groups[assignments[s]].append(data[s])
  return groups, groupsCenters
