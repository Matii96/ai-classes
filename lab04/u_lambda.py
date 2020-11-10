from random import uniform
import numpy as np
import math

def u_lambda(function, xmin, xmax, mu=4, lambda_param=10, tournament_size=2, mutation=0.1, iterations=20):
  attributes = len(xmin)

  # Firts attribute of individual is its rate
  individuals = np.array([
    [0.0] + [uniform(xmin[i], xmax[i]) for i in range(attributes)]
    for _ in range(mu)
  ])

  # Rate each individual
  for individual_idx in range(mu):
    x = individuals[individual_idx,1:]
    individuals[individual_idx,0] = eval(function)

  for _ in range(iterations):
    descendants = []

    for _ in range(lambda_param):
      # Pick radom tournament contestants
      tournament_indexes = np.random.choice(mu, size=tournament_size, replace=False)

      # Choose winner
      best_contestant_idx = None
      best_contestant_value = None
      for contestant_idx in tournament_indexes:
        if best_contestant_idx is None or individuals[contestant_idx,0] > best_contestant_value:
          best_contestant_value = individuals[contestant_idx,0]
          best_contestant_idx = contestant_idx

      # Mutate winner
      new_individual = np.array(individuals[best_contestant_idx])
      for attribute_idx in range(attributes):
        new_individual[attribute_idx + 1] += uniform(-mutation, mutation)
      x = new_individual[1:]
      new_individual[0] = eval(function)
      
      descendants.append(new_individual)

    # Merge generations
    individuals = np.concatenate((individuals, np.array(descendants)), axis=0)
    individuals = individuals[np.argsort(individuals[:,0])]
    np.delete(individuals, list(range(lambda_param)))

  # Return best individual without its rate
  return individuals[-1,1:]
