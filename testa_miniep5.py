#!/usr/bin/python3
#-------------------------------------------------------------------------------
#  Autor: Christian M. T. Takagi            No. USP: 7136971                   -
#  Disciplina: MAC0242                      Prof.  Alfredo Goldman             -
#  Mini-EP 5                                Arquivo: testa_miniep5.py          -
#-------------------------------------------------------------------------------

import unittest as ut
import miniep5 as ep5
import sys

class TestaMiniEP5(ut.TestCase):
    def SetUp(self):
        with open('.temp', 'w+') as arq:
            arq.write('')
    
    def testa_soma(self):
        with open('.temp', 'w+') as arq:
            arq.write('4 3 + \n')
        with open('.temp', 'r') as sys.stdin:
            ep5.main()
            self.assertEqual(7, ep5.result['resultado'])

    def testa_subtracao(self):
        with open('.temp', 'w+') as arq:
            arq.write('4 3 - \n')
        with open('.temp', 'r') as sys.stdin:
            ep5.main()
            self.assertEqual(1, ep5.result['resultado'])

    def testa_produto(self):
        with open('.temp', 'w+') as arq:
            arq.write('4 3 * \n')
        with open('.temp', 'r') as sys.stdin:
            ep5.main()
            self.assertEqual(12, ep5.result['resultado'])

    def testa_fracao(self):
        with open('.temp', 'w+') as arq:
            arq.write('4 3 / \n')
        with open('.temp', 'r') as sys.stdin:
            ep5.main()
            self.assertAlmostEqual((4.0/3), ep5.result['resultado'])

    def testa_variavel(self):
        with open('.temp', 'w+') as arq:
            arq.write('a 3 = \n')
        with open('.temp', 'r') as sys.stdin:
            ep5.main()
                self.assertEqual(3, ep5.nomes['a'])

    def testa_negativo(self):
        with open('.temp', 'w+') as arq:
            arq.write('-2 \n')
        with open('.temp', 'r') as sys.stdin:
            ep5.main()
            self.assertEqual(-2, ep5.result['resultado'])

    def testa_negativo_soma(self):
        with open('.temp', 'w+') as arq:
            arq.write('-2 -2 +\n')
        with open('.temp', 'r') as sys.stdin:
            ep5.main()
            self.assertEqual(-4, ep5.result['resultado'])

    def testa_negativo_conflito(self):
        with open('.temp', 'w+') as arq:
            arq.write('3 -2 -2 + + \n')
        with open('.temp', 'r') as sys.stdin:
            ep5.main()
            self.assertEqual(True, ep5.result['erro'])
            self.assertEqual('+', ep5.result['token'])

    def testa_parenteses(self):
        with open('.temp', 'w+') as arq:
            arq.write('3 (-2) (-2) + + \n')
        with open('.temp', 'r') as sys.stdin:
            ep5.main()
            self.assertEqual(-1, ep5.result['resultado'])

    def testa_expressao(self):
        with open('.temp', 'w+') as arq:
            arq.write('(-2) 6 2 * - 5 3 / + \n')
        with open('.temp', 'r') as sys.stdin:
            ep5.main()
            self.assertAlmostEqual(-12.33333334, ep5.result['resultado'])

if __name__ == '__main__':
    ut.main(buffer=True)
