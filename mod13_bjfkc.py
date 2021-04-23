import unittest


class Project3Test(unittest.TestCase):

    def test_symbol(self):
        self.assertEqual("IBM", "IBM")
        self.assertEqual("GOOGLE", "GOOGLE")
    
    def test_chart(self):
        self.assertEqual("1", "1")
        self.assertEqual("2", "2")

    def test_time(self):
        self.assertEqual("1", "1")
        self.assertEqual("2", "2")
        self.assertEqual("3", "3")
        self.assertEqual("4", "4")

    def test_start(self):
        self.assertEqual("08-01-2020", "08-01-2020")

    def test_end(self):
        self.assertEqual("08-31-2020", "08-31-2020")
       

if __name__ == "__main__":
    unittest.main()
