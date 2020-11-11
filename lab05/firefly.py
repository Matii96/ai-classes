from random import uniform, shuffle
from math import hypot
import numpy as np
import math

def firefly(function, xmin, xmax, N=4, beta0=0.3, gamma0=0.1, mu=0.05, iterations=30):
  attributes = len(xmin)
  individuals = np.array([
    [uniform(xmin[i], xmax[i]) for i in range(attributes)]
    for _ in range(N)
  ])

  # Calculate gamma and attributes variation
  rmax = 0
  attributes_variation = np.empty(attributes)
  for i in range(len(individuals)):
    for j in range(i, len(individuals)):
      rmax = max(hypot(*(individuals[i] - individuals[j])), rmax)

      # Find biggest difference between attributes
      for t in range(attributes):
        attributes_variation[t] = max(hypot(individuals[i,t] - individuals[j,t]), attributes_variation[t])
  gamma = gamma0 / rmax

  # Rate each individual
  individuals_rate = np.empty(N)
  for i in range(len(individuals)):
    x = individuals[i]
    value = eval(function)
  
  for _ in range(iterations):
    a_order = list(range(len(individuals)))
    shuffle(a_order)
    for a in a_order:
      b_order = list(range(len(individuals)))
      shuffle(b_order)
      for b in b_order:
        if individuals_rate[b] > individuals_rate[a]:
          # Calculate attraction and update individual
          beta = beta0 * math.exp(-gamma * hypot(*(individuals[a] - individuals[b])))
          individuals[a] = individuals[a] + beta * (individuals[b] - individuals[a])

          # Update rate
          x = individuals[a]
          individuals_rate[a] = eval(function)

    # Apply mutation
    for t in range(attributes):
      individuals[a,t] = uniform(-attributes_variation[t], attributes_variation[t])

    # Update rate
    x = individuals[a]
    individuals_rate[a] = eval(function)

  return individuals[np.where(individuals_rate == np.amax(individuals_rate))[0][0]]
