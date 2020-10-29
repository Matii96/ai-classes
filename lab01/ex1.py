from absl import app, flags
from absl.flags import FLAGS
from fileLoader import wczytaj_baze_probek_z_tekstem

flags.DEFINE_string('nazwa_pliku_z_wartosciami',
                    './australian.txt', 'Nazwa pliku z wartosciami')
flags.DEFINE_string('nazwa_pliku_z_opisem_atr', './australian-type.txt', 'Nazwa pliku z opisem atr')

def main(_argv):
  probki, nazwy_atr, czy_atr_symb = wczytaj_baze_probek_z_tekstem(FLAGS.nazwa_pliku_z_wartosciami, FLAGS.nazwa_pliku_z_opisem_atr)

  # Test
  print("probki (1sza linia): {}".format(probki[0]))
  print("nazwy_atr: {}".format(nazwy_atr))
  print("czy_atr_symb: {}".format(czy_atr_symb))

if __name__ == '__main__':
  app.run(main)
