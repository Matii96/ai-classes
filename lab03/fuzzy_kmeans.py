from math import hypot
import numpy as np

def fuzzy_kmeans(data, groups_count, iterations=100, fcm_m=2, progress=None):
  attributes = 2
  U = np.empty((groups_count, len(data)))      # Samples participation in groups
  D = np.empty((groups_count, len(data)))      # Sample - group distances
  V = np.random.rand(groups_count, attributes) # Groups centers

  power = 1 / (1 - fcm_m)
  data_np = np.array(data)
  for _ in range(iterations):
    for j in range(groups_count):
      for s in range(len(data)):
        sample = data[s]
        D[j,s] = max(hypot(V[j,0] - sample[0], V[j,1] - sample[1]), 1e-10)

    for j in range(groups_count):
      for s in range(len(data)):
        U[j,s] = (D[j,s] ** power) / np.sum(D[:,s] ** power)
        
    if not progress is None:
      progress.append({ 'groups': np.array(U), 'centers': np.array(V) })

    for j in range(groups_count):
      for i in range(attributes):
        u_adjusted = U[j,:] ** fcm_m
        V[j,i] = np.sum(np.multiply(u_adjusted, data_np[:,i])) / np.sum(u_adjusted)

  return U, V
