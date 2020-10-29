from convert import probki_str_na_liczby

def main():
  probki_str = [
    ['1', 'a', '2.2'],
    ['3', '4', '5']
  ]
  numery_atr = [0, 2]
  wynik = probki_str_na_liczby(probki_str, numery_atr)
  print(wynik)


if __name__ == '__main__':
    main()
