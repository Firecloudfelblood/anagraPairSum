import unittest
from SumaPares import suma_pares


class PuebaSumaPares(unittest.TestCase):

    def prueba(self, fun_solucion):
        sumas_prueba = {
            1: ([8, 7, 2, 5, 3, 1], 10, 2),
            2: ([-1, 1, -2, 2, 0], 0, 2),
            3: ([], 0, 0),
            4: ([-2, -2, 0, 0], 1, 0),
            5: ([-2, -2, 0, 0], -2, 1),
            6: ([-1, 1, -2, 2, 0], 1, 2)
        }
        sol = 'Error'
        for p in sumas_prueba.values():
            try:
                sol = fun_solucion(arr=p[0], k=p[1])
                self.assertEqual(sol, p[2])
            except AssertionError as e:
                print(f'Fallo! arr={p[0]},  k={p[1]},  output={sol}, esperada={p[2]}')


t = PuebaSumaPares()
t.prueba(suma_pares)
