def split_line(line):
  separatory = [' ', '\t', ',', '/']
  for sep in separatory:
    # Dzielenie wg separatorów oraz usunięcie pustych znaków
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
    # Usunięcie znaku nowej linii
    if line[len(line)-1] == '\n':
      line = line[:-1]

    # Linia może być pusta
    if len(line) == 0:
      continue

    wynik.append(split_line(line))
  return wynik

def wczytaj_baze_probek_z_tekstem(nazwa_pliku_z_wartosciami, nazwa_pliku_z_opisem_atr):
  # Parsowanie pliku z próbkami
  probki = load_file(nazwa_pliku_z_wartosciami)

  # Parsowanie pliku z informacjami o atrybutach
  nazwy_atr = []
  czy_atr_symb = []
  atrybuty = load_file(nazwa_pliku_z_opisem_atr)
  for atrybut in atrybuty:
    nazwy_atr.append(atrybut[0])
    czy_atr_symb.append(atrybut[1] == 's')

  return (probki, nazwy_atr, czy_atr_symb)
