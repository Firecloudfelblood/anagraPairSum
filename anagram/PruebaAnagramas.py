import unittest
from anagramasgcm import anagram


class PruebaAnagramas(unittest.TestCase):

    def prueba(self, fun_solucion):
        # Anagrams
        anagrams_d = {
            1: ('Mother-in-law', 'Hitler woman'),
            2: ('Debit card', 'Bad credit'),
            3: ('Dormitory', 'Dirty room'),
            4: ('The earthquakes', 'The queer shakes'),
            5: ('Astronomer', 'Moon starrer'),
            6: ('Punishments', 'Nine thumps'),
            7: ('School master', 'The classroom')
        }

        # No anagramas
        no_anagrams_d = {
            1: ('Motherr-in-law', 'Hitler woman'),
            2: ('Debiit card', 'Bad credit'),
            3: ('Dorrmitory', 'Dirty room'),
            4: ('The earthquakes', 'The queer shakes'),
            5: ('Astrodnomer', 'Moon starrer'),
            6: ('Punishfhments', 'Nine thumps'),
            7: ('Schoool master', 'The classroom')
        }

        for ana in anagrams_d.values():
            try:
                self.assertTrue(fun_solucion(ana[0], ana[1]))
            except AssertionError as e:
                # este print solo se ejecutara si el assertTrue falla
                print('Fallo, es un anagrama (True): ', ana)
        for ana in no_anagrams_d.values():
            try:
                # este print solo se ejecutara si el assertTrue falla
                self.assertFalse(fun_solucion(ana[0], ana[1]))
            except AssertionError as e:
                print('Fallo, no es un anagrama (False): ', ana)


t = PruebaAnagramas()
t.prueba(anagram)
