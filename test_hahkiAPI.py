from unittest import TestCase

from Hahkiapi import HahkiAPI


class TestHahkiAPI(TestCase):
    game = HahkiAPI()

    def test_without_net(self):
        None

    def test_gameLogic(self):
        None

    def test_hodWithEnemyForDamka(self):
        self.game.iFirstActivePosition=0
        self.game.jFirstActivePosition=9
        self.game.gameField = [
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
        self.game.hod_with_enemy_for_king(2, 5)
        self.assertEqual(self.game.gameField, accesmass)
        #For black damka
        self.game.iFirstActivePosition = 2
        self.game.jFirstActivePosition = 5

        self.game.gameField = [
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
        self.game.hod_with_enemy_for_king(0, 7)
        self.assertEqual(self.game.gameField, accesmassForBlack)

    def test_accesHodForDamka(self):
        self.game.iFirstActivePosition = 2
        self.game.jFirstActivePosition = 5

        self.game.playDraught = 'b'
        self.game.playerDraught = 'w'


        self.game.gameField = [
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

        self.assertTrue(self.game.correct_hod_for_king(0, 7))

        self.game.iFirstActivePosition = 0
        self.game.jFirstActivePosition = 7

        self.game.gameField = [
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

        self.assertTrue(self.game.correct_hod_for_king(2, 5))

        self.game.iFirstActivePosition = 4
        self.game.jFirstActivePosition = 3

        self.game.gameField = [
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

        self.assertTrue(self.game.correct_hod_for_king(0, 7))

    def test_checkEnemyForDamka(self):
        None

    def test_ruleOne(self):
        self.game.playDraught = "w"

        self.game.gameField = [
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

        self.game.playDraught = "b"

        self.game.gameField = [
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
        self.game.playDraught = "b"

        self.game.gameField = [
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

        self.game.playDraught = "w"

        self.game.gameField = [
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
        self.game.playDraught = 'w'
        self.game.set_king(0, 1)
        self.assertEqual(self.game.gameField[0][1], 'q')

        self.game.playDraught = 'b'
        self.game.set_king(0, 1)
        self.assertEqual(self.game.gameField[0][1], 'v')

    def test_damkaCheckAfterEnemy(self):
        self.game.playDraught = "w"
        self.game.playerDraught = "w"

        self.game.gameField = [
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

        self.assertFalse(self.game.king_check_after_enemy(0, 7))
        self.assertTrue(self.game.king_check_after_enemy(0, 3))

        self.game.gameField = [
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

        self.assertTrue(self.game.king_check_after_enemy(0, 7))
        self.assertTrue(self.game.king_check_after_enemy(0, 3))

        self.game.playDraught = "b"
        self.game.playerDraught = "b"

        self.game.gameField = [
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

        self.assertFalse(self.game.king_check_after_enemy(0, 7))
        self.assertTrue(self.game.king_check_after_enemy(0, 1))

    def test_damkaCheckWithoutEnemy(self):
        self.game.playDraught = "b"
        self.game.playerDraught = "b"

        self.game.gameField = [
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

        self.assertTrue(self.game.king_check_without_enemy(0, 1))
        self.assertFalse(self.game.king_check_without_enemy(9, 0))

        self.game.playerDraught= 'w'
        self.assertTrue(self.game.king_check_without_enemy(9, 0))

    def test_hodWithEnemy(self):
        self.game.playDraught = "b"
        self.game.playerDraught = "b"

        self.game.iFirstActivePosition = 0
        self.game.jFirstActivePosition = 7

        self.game.gameField = [
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

        self.game.step_with_enemy(2, 5)
        self.assertTrue(self.game.gameField[2][5] == 'b')
        self.assertTrue(self.game.gameField[1][6] == '.')
        self.assertTrue(self.game.gameField[0][7] == '.')

        self.game.iFirstActivePosition=8
        self.game.jFirstActivePosition=1

        self.game.step_with_enemy(6, 3)
        self.assertTrue(self.game.gameField[6][3] == 'w')
        self.assertTrue(self.game.gameField[7][2] == '.')
        self.assertTrue(self.game.gameField[8][1] == '.')

    def test_accessHodWithEnemy(self):
        None

    def test_checkEnemy(self):
        self.game.gameField = [
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

        self.assertEqual(self.game.check_enemy(0, 7), [(1, 6)])
        self.assertEqual(self.game.check_enemy(6, 3), [(5, 2), (5, 4)])

    def test_checkChessWithEnemy(self):
        self.game.playDraught = "b"
        self.game.gameField = [
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

        self.assertEqual(self.game.check_chess_with_enemy(), [(0, 3), (0, 7), (5, 4)])

    def test_normalHodRule(self):
        self.game.playerDraught = "w"
        self.game.playDraught = "w"
        self.game.gameField = [
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

        self.assertTrue(self.game.normal_step_rule(2, 5, 1, 6))
        self.assertFalse(self.game.normal_step_rule(2, 5, 3, 6))
        self.assertFalse(self.game.normal_step_rule(2, 5, 3, 5))
        self.assertFalse(self.game.normal_step_rule(1, 2, 0, 3))
        self.assertFalse(self.game.normal_step_rule(2, 5, 4, 3))

    def test_changeNumber(self):
        self.game.playDraught= 'w'
        self.game.change_number_of_live_draughts()
        self.assertEqual(self.game.numberOfBlack,19)
        self.game.change_number_of_live_draughts()
        self.assertEqual(self.game.numberOfBlack, 18)
        self.game.playDraught = 'b'
        self.game.change_number_of_live_draughts()
        self.assertEqual(self.game.numberOfWhite, 19)

    def test_endGame(self):
        None

    def test_how_kill(self):
        self.game.playDraught = "w"
        self.assertEqual(self.game.who_was_killed(), "b")
        self.game.playDraught = "b"
        self.assertEqual(self.game.who_was_killed(), "w")

    def test_hod(self):
        self.game.gameField = [
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
        self.game.simple_step(0, 1, 1, 2)
        self.assertEqual(self.game.gameField[0][1], '.')
        self.assertEqual(self.game.gameField[1][2], 'b')

    def test_checkchess(self):
        None

    def test_startpos(self):
        None

    def test_changeGoChess(self):
        self.game.playDraught= 'w'
        self.game.change_godraught()
        self.assertEqual(self.game.playDraught, 'b')

        self.game.playDraught = 'b'
        self.game.change_godraught()
        self.assertEqual(self.game.playDraught, 'w')
