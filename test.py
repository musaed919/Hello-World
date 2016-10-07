import unittest
from bowling import Bowling

class BowlingTest(unittest.TestCase):
	def setUp(self):
		self.bowling = Bowling()

	def tear(self):
		del self.bowling

	def test_one_throw(self):
		self.bowling.throw(3)
		self.assertGreaterEqual(3,0)
		self.assertLessEqual(3,10)
		self.assertEqual(self.bowling.score[0], 3)
		self.assertFalse(self.bowling.first_throw)
		self.assertTrue(self.bowling.second_throw)
		self.assertEqual(self.bowling.frame, 0)


	def test_two_throws(self):
		self.bowling.throw(5)
		self.bowling.throw(2)
		self.assertEqual(self.bowling.frame_score(0),7)
		self.assertFalse(self.bowling.second_throw)
		self.assertTrue(self.bowling.first_throw)
		self.assertEqual(self.bowling.frame, 0)

	def test_three_throws(self):
		self.bowling.throw(5)
		self.bowling.throw(2)
		self.bowling.inc_frame()
		self.bowling.throw(7)
		self.assertEqual(self.bowling.score[2], 7)
		self.assertTrue(self.bowling.second_throw)
		self.assertFalse(self.bowling.first_throw)
		self.assertEqual(self.bowling.frame, 1)

	def test_Spare_Counts_Next_Frame(self):
		self.bowling.throw(4)
		self.bowling.throw(6)
		self.assertLess(self.bowling.score[0],10)
		self.assertEqual(self.bowling.frame_score(0), 10)
		self.bowling.inc_frame()
		self.bowling.throw(2)
		self.bowling.throw(4)
		"""spare happend in frame[0]"""
		self.bowling.spare(0)
		self.assertEqual(self.bowling.frame_score(0), 16)

	def test_Strike_Moves_To_Next_Frame(self):
		self.bowling.throw(10)
		self.bowling.throw(2)
		self.assertEqual(self.bowling.score[1],0)
		self.assertEqual(self.bowling.frame_score(0),10)
		self.assertEqual(self.bowling.score[2], 2)
		self.assertEqual(self.bowling.frame,1)

	def	test_Strike_Counts_Next_Frame_Scores(self):
		self.bowling.throw(10)
		self.bowling.throw(2)
		self.bowling.throw(4)
		self.bowling.throw(5)
		self.bowling.throw(3)
		"""strike happend in frame[0]"""
		self.bowling.strike(0)
		self.assertEqual(self.bowling.frame_score(0),24)



suite = unittest.TestLoader().loadTestsFromTestCase(BowlingTest)
unittest.TextTestRunner(verbosity=2).run(suite)