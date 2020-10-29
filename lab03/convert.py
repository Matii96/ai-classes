def probki_str_na_liczby(probki_str, numery_atr):
  result = []
  for rowIdx in range(0, len(probki_str)):
    row = probki_str[rowIdx]
    newRow = []
    for colIdx in numery_atr:
      cell = row[colIdx]
      try:
        newRow.append(float(cell))
      except:
        raise Exception('Invalid float at position {},{}'.format(rowIdx, colIdx))
    result.append(newRow)
  return result
