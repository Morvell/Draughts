from unittest import TestCase

from Hahkiapi import HahkiAPI


class TestHahkiAPI(TestCase):
    game = HahkiAPI()

    def test_without_net(self):
        None

    def test_gameLogic(self):
        None

    def test_hodWithEnemyForDamka(self):
        self.game.ipos=0
        self.game.jpos=9
        self.game.polemass = [
            list(' . . . . q'),
            list('. . . b . '),
            list(' . . . . .'),
            list('. . . . . '),
            list(' . . . . .'),
            list('. . . . . '),
            list(' w w w w w'),
            list('w w w w w '),
            list(' w w w w w'),
            list('w w w w w '),
        ]


        accesmass = [
            list(' . . . . .'),
            list('. . . . . '),
            list(' . . q . .'),
            list('. . . . . '),
            list(' . . . . .'),
            list('. . . . . '),
            list(' w w w w w'),
            list('w w w w w '),
            list(' w w w w w'),
            list('w w w w w '),
        ]
        self.game.hodWithEnemyForDamka(2, 5)
        self.assertEqual(self.game.polemass, accesmass)
        #For black damka
        self.game.ipos = 2
        self.game.jpos = 5

        self.game.polemass = [
            list(' . . . . .'),
            list('. . . w . '),
            list(' . . v . .'),
            list('. . . . . '),
            list(' . . . . .'),
            list('. . . . . '),
            list(' w w w w w'),
            list('w w w w w '),
            list(' w w w w w'),
            list('w w w w w '),
        ]

        accesmassForBlack = [
            list(' . . . v .'),
            list('. . . . . '),
            list(' . . . . .'),
            list('. . . . . '),
            list(' . . . . .'),
            list('. . . . . '),
            list(' w w w w w'),
            list('w w w w w '),
            list(' w w w w w'),
            list('w w w w w '),
        ]
        self.game.hodWithEnemyForDamka(0, 7)
        self.assertEqual(self.game.polemass, accesmassForBlack)

    def test_accesHodForDamka(self):
        self.game.ipos = 2
        self.game.jpos = 5

        self.game.gochess ='b'
        self.game.playerchess = 'w'


        self.game.polemass = [
            list(' . . . . .'),
            list('. . . w . '),
            list(' . . v . .'),
            list('. . . . . '),
            list(' . . . . .'),
            list('. . . . . '),
            list(' w w w w w'),
            list('w w w w w '),
            list(' w w w w w'),
            list('w w w w w '),
        ]

        self.assertTrue(self.game.accesHodForDamka(0, 7))

        self.game.ipos = 0
        self.game.jpos = 7

        self.game.polemass = [
            list(' . . . v .'),
            list('. . . w . '),
            list(' . . . . .'),
            list('. . . . . '),
            list(' . . . . .'),
            list('. . . . . '),
            list(' w w w w w'),
            list('w w w w w '),
            list(' w w w w w'),
            list('w w w w w '),
        ]

        self.assertTrue(self.game.accesHodForDamka(2, 5))

        self.game.ipos = 4
        self.game.jpos = 3

        self.game.polemass = [
            list(' . . . . .'),
            list('. . . w . '),
            list(' . . . . .'),
            list('. . v . . '),
            list(' . . . . .'),
            list('. . . . . '),
            list(' w w w w w'),
            list('w w w w w '),
            list(' w w w w w'),
            list('w w w w w '),
        ]

        self.assertTrue(self.game.accesHodForDamka(0, 7))

    def test_checkEnemyForDamka(self):
        None

    def test_ruleOne(self):
        self.game.gochess = "w"

        self.game.polemass = [
            list(' b v . . .'),
            list('. . . . . '),
            list(' . . . . .'),
            list('. . v . . '),
            list(' . . . . .'),
            list('. . . . . '),
            list(' w w w w w'),
            list('w w w w w '),
            list(' w w w w w'),
            list('w w w w w '),
        ]

        self.assertTrue(self.game.ruleOne(0,1))
        self.assertTrue(self.game.ruleOne(0,3))

        self.game.gochess = "b"

        self.game.polemass = [
            list(' . v . . .'),
            list('q w . . . '),
            list(' . . . . .'),
            list('. . v . . '),
            list(' . . . . .'),
            list('. . . . . '),
            list(' w w w w w'),
            list('w w w w w '),
            list(' w w w w w'),
            list('w w w w w '),
        ]

        self.assertTrue(self.game.ruleOne(1, 0))
        self.assertTrue(self.game.ruleOne(1, 2))


    def test_ruleTwo(self):
        self.game.gochess = "b"

        self.game.polemass = [
            list(' b v . . .'),
            list('. . . . . '),
            list(' . . . . .'),
            list('. . v . . '),
            list(' . . . . .'),
            list('. . . . . '),
            list(' w w w w w'),
            list('w w w w w '),
            list(' w w w w w'),
            list('w w w w w '),
        ]

        self.assertTrue(self.game.ruleTwo(0, 1))
        self.assertTrue(self.game.ruleTwo(0, 3))

        self.game.gochess = "w"

        self.game.polemass = [
            list(' . v . . .'),
            list('q w . . . '),
            list(' . . . . .'),
            list('. . v . . '),
            list(' . . . . .'),
            list('. . . . . '),
            list(' w w w w w'),
            list('w w w w w '),
            list(' w w w w w'),
            list('w w w w w '),
        ]

        self.assertTrue(self.game.ruleTwo(1, 0))
        self.assertTrue(self.game.ruleTwo(1, 2))

    def test_setDamka(self):
        self.game.gochess = 'w'
        self.game.setDamka(0,1)
        self.assertEqual(self.game.polemass[0][1], 'q')

        self.game.gochess = 'b'
        self.game.setDamka(0, 1)
        self.assertEqual(self.game.polemass[0][1], 'v')

    def test_damkaCheckAfterEnemy(self):
        self.game.gochess = "w"
        self.game.playerchess = "w"

        self.game.polemass = [
            list(' . w . w .'),
            list('. . . b . '),
            list(' . . . b .'),
            list('. . v . . '),
            list(' . . . . .'),
            list('. . . . . '),
            list(' w w w w w'),
            list('w w w w w '),
            list(' w w w w w'),
            list('w w w w w '),
        ]

        self.assertFalse(self.game.damkaCheckAfterEnemy(0,7))
        self.assertTrue(self.game.damkaCheckAfterEnemy(0,3))

        self.game.polemass = [
            list(' . w . w .'),
            list('. . . . . '),
            list(' . . . b .'),
            list('. . v . . '),
            list(' . . . . .'),
            list('. . . . . '),
            list(' . . . . .'),
            list('. . . . . '),
            list(' . . . . .'),
            list('. . . . . '),
        ]

        self.assertTrue(self.game.damkaCheckAfterEnemy(0, 7))
        self.assertTrue(self.game.damkaCheckAfterEnemy(0, 3))

        self.game.gochess = "b"
        self.game.playerchess = "b"

        self.game.polemass = [
            list(' b . . b .'),
            list('. . . w . '),
            list(' . . . . .'),
            list('. . . . . '),
            list(' . . . . .'),
            list('. . . . . '),
            list(' . . . . .'),
            list('. . . . . '),
            list(' . . . . .'),
            list('. . . . . '),
        ]

        self.assertFalse(self.game.damkaCheckAfterEnemy(0, 7))
        self.assertTrue(self.game.damkaCheckAfterEnemy(0, 1))

    def test_damkaCheckWithoutEnemy(self):
        self.game.gochess = "b"
        self.game.playerchess = "b"

        self.game.polemass = [
            list(' b . . b .'),
            list('. . . w . '),
            list(' . . . . .'),
            list('. . . . . '),
            list(' . . . . .'),
            list('. . . . . '),
            list(' . . . . .'),
            list('. . . . . '),
            list(' . . . . .'),
            list('b . . . . '),
        ]

        self.assertTrue(self.game.damkaCheckWithoutEnemy(0, 1))
        self.assertFalse(self.game.damkaCheckWithoutEnemy(9, 0))

        self.game.playerchess='w'
        self.assertTrue(self.game.damkaCheckWithoutEnemy(9, 0))

    def test_hodWithEnemy(self):
        self.game.gochess = "b"
        self.game.playerchess = "b"

        self.game.ipos = 0
        self.game.jpos = 7

        self.game.polemass = [
            list(' . . . b .'),
            list('. . . w . '),
            list(' . . . . .'),
            list('. . . . . '),
            list(' . . . . .'),
            list('. . . . . '),
            list(' . . . . .'),
            list('. b . . . '),
            list(' w . . . .'),
            list('. . . . . '),
        ]

        self.game.hodWithEnemy(2, 5)
        self.assertTrue(self.game.polemass[2][5]=='b')
        self.assertTrue(self.game.polemass[1][6]=='.')
        self.assertTrue(self.game.polemass[0][7]=='.')

        self.game.ipos=8
        self.game.jpos=1

        self.game.hodWithEnemy(6, 3)
        self.assertTrue(self.game.polemass[6][3] == 'w')
        self.assertTrue(self.game.polemass[7][2] == '.')
        self.assertTrue(self.game.polemass[8][1] == '.')

    def test_accessHodWithEnemy(self):
        None

    def test_checkEnemy(self):
        self.game.polemass = [
            list(' . . . b .'),
            list('. . . w . '),
            list(' . . . . .'),
            list('. . . . . '),
            list(' . . . . .'),
            list('. b b . . '),
            list(' . w . . .'),
            list('. . b . . '),
            list(' . . b . .'),
            list('. . . . . '),
        ]

        self.assertEqual(self.game.checkEnemy(0, 7), [(1, 6)])
        self.assertEqual(self.game.checkEnemy(6, 3), [(5, 2), (5, 4)])

    def test_checkChessWithEnemy(self):
        self.game.gochess = "b"
        self.game.polemass = [
            list(' . b . v .'),
            list('. w . . . '),
            list(' . . w . .'),
            list('. . . . w '),
            list(' . . . . w'),
            list('. b b . . '),
            list(' . w . . .'),
            list('. . b . b '),
            list(' . . b . b'),
            list('. . . . . '),
        ]

        self.assertEqual(self.game.checkChessWithEnemy(),[(0,3), (0, 7), (5, 4)])

    def test_normalHodRule(self):
        self.game.playerchess = "w"
        self.game.gochess = "w"
        self.game.polemass = [
            list(' . b . v .'),
            list('. w . . . '),
            list(' . . w . .'),
            list('. . . . w '),
            list(' . . . . w'),
            list('. b b . . '),
            list(' . w . . .'),
            list('. . b . b '),
            list(' . . b . b'),
            list('. . . . . '),
        ]

        self.assertTrue(self.game.normalHodRule(2,5,1,6))
        self.assertFalse(self.game.normalHodRule(2,5,3,6))
        self.assertFalse(self.game.normalHodRule(2,5,3,5))
        self.assertFalse(self.game.normalHodRule(1,2,0,3))
        self.assertFalse(self.game.normalHodRule(2,5,4,3))

    def test_changeNumber(self):
        self.game.gochess='w'
        self.game.changeNumber()
        self.assertEqual(self.game.numberOfBlack,19)
        self.game.changeNumber()
        self.assertEqual(self.game.numberOfBlack, 18)
        self.game.gochess = 'b'
        self.game.changeNumber()
        self.assertEqual(self.game.numberOfWhite, 19)

    def test_endGame(self):
        None

    def test_how_kill(self):
        self.game.gochess = "w"
        self.assertEqual(self.game.how_kill(), "b")
        self.game.gochess = "b"
        self.assertEqual(self.game.how_kill(), "w")

    def test_hod(self):
        self.game.polemass = [
            list(' b . . v .'),
            list('. . . . . '),
            list(' . . w . .'),
            list('. . . . w '),
            list(' . . . . w'),
            list('. b b . . '),
            list(' . w . . .'),
            list('. . b . b '),
            list(' . . b . b'),
            list('. . . . . '),
        ]
        self.game.hod(0,1,1,2)
        self.assertEqual(self.game.polemass[0][1], '.')
        self.assertEqual(self.game.polemass[1][2], 'b')

    def test_checkchess(self):
        None

    def test_startpos(self):
        None

    def test_changeGoChess(self):
        self.game.gochess='w'
        self.game.changeGoChess()
        self.assertEqual(self.game.gochess,'b')

        self.game.gochess = 'b'
        self.game.changeGoChess()
        self.assertEqual(self.game.gochess, 'w')
