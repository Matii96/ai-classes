from random import uniform
from sys import float_info
import numpy as np
import math

def Pso(function, individualsCount, rinertion, rglob, rloc, xmin, xmax, iterations=30):
  individuals = []
  for i in range(individualsCount):
    individuals.append([uniform(xmin[j], xmax[j]) for j in range(len(xmin))])

  # Set local optimum and velocity for each individual
  optima = [individual[:] for individual in individuals]
  velocity = np.zeros((individualsCount, len(xmin)))

  bestIndividual = None
  bestIndividualValue = -math.inf
  for i in range(iterations):
    # Find best individual
    for j in range(individualsCount):
      x = individuals[j]
      value = eval(function)
      if value >= bestIndividualValue:
        bestIndividualValue = value
        bestIndividual = x

    # Adjust individuals ratings if needed
    for j in range(individualsCount):
      x = individuals[j]
      individualRating = eval(function)
      x = optima[j]
      individualOptimumRating = eval(function)
      if individualOptimumRating < individualRating:
        optima[j] = individuals[j]

    # Recalculate velocity
    for j in range(individualsCount):
      individual = individuals[j]
      rndGlob = uniform(float_info.min, 1-float_info.min)
      rndLoc = uniform(float_info.min, 1-float_info.min)
      for i in range(len(individual)):
        velocity[j,i] = velocity[j,i] * rinertion + (bestIndividual[i] - individual[i]) * rglob * rndGlob + (optima[j][i] - individual[i]) * rloc * rndLoc
        individuals[j][i] = individual[i] + velocity[j, i]

  return bestIndividual
