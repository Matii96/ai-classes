def split_line(line):
  separators = [' ', '\t', ',', '/']
  for sep in separators:
    # Split by separators and remove white spaces
    line = list(filter(None, line.split(sep)))
    if len(line) == 1:
      line = line[0]
    else:
      break
  if isinstance(line, str):
    return [line]
  return line

def load_file(filename):
  result = []
  file = open(filename, 'r')
  lines = file.readlines()
  for line in lines:
    # Remove new line sign
    if line[len(line)-1] == '\n':
      line = line[:-1]

    # Line may be empty
    parsedLine = split_line(line)
    if len(parsedLine) == 0:
      continue

    result.append(split_line(line))
  return result

def wczytaj_baze_probek_z_tekstem(nazwa_pliku_z_wartosciami, nazwa_pliku_z_opisem_atr):
  # Parse file with data
  samples = load_file(nazwa_pliku_z_wartosciami)

  # Parse file with attributes
  names = []
  isSymbolic = []
  attributes = load_file(nazwa_pliku_z_opisem_atr)
  for attribute in attributes:
    names.append(attribute[0])
    isSymbolic.append(attribute[1] == 's')

  return (samples, names, isSymbolic)
