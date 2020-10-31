def split_line(line):
  separatory = [' ', '\t', ',', '/']
  for sep in separatory:
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
  wynik = []
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

    wynik.append(split_line(line))
  return wynik

def wczytaj_baze_probek_z_tekstem(nazwa_pliku_z_wartosciami, nazwa_pliku_z_opisem_atr):
  # Parse file with data
  probki = load_file(nazwa_pliku_z_wartosciami)

  # Parse file with attributes
  nazwy_atr = []
  czy_atr_symb = []
  atrybuty = load_file(nazwa_pliku_z_opisem_atr)
  for atrybut in atrybuty:
    nazwy_atr.append(atrybut[0])
    czy_atr_symb.append(atrybut[1] == 's')

  return (probki, nazwy_atr, czy_atr_symb)
