import unittest
from BabylonRoot import sqrt_babylon

class TestBabylonRoot(unittest.TestCase):

    def testBabylonExists(self):
        self.assertIsNotNone(sqrt_babylon)


    def testBabylonNeg(self):
        self.assertIsNone(sqrt_babylon(-5))


    def testBabylon0(self):
        self.assertEqual(sqrt_babylon(0), 0)


    def testBabylonRoot4(self):
        self.assertEqual(sqrt_babylon(4), 2)


    def testBabylonRoot16(self):
        self.assertEqual(sqrt_babylon(16), 4)


    def testBabylonRoot1(self):
        self.assertEqual(sqrt_babylon(1), 1)


    def testBabylonRoot2(self):
        self.assertEqual(sqrt_babylon(2), 1.414213562373095)


    def testBabylonRoot3(self):
        self.assertEqual(sqrt_babylon(3), 1.7320508075688772)




unittest.main()
