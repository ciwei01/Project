import unittest
import HTMLTestRunner
import random
class MyUnitTest(unittest.TestCase):
  
    @classmethod
    def setUpClass(cls):
        print('before case run setUPClass only load onces')
    def setUp(self):
        self.a=1
        self.b=2
        print('---setUp')
        
    def test_1(self):
        a=random.randint(0,50)
        print(a)
        b=20
        if a>b:
            print(a+3)
        else:
            print(b)
        print('case 1')
    
    def test_2(self):
        print('case2')        
        
    def tearDown(self):
        print('----tearDown')
    
    @classmethod
    def tearDownClass(cls):
        print('11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111')
        print('tearDownClass only load onces after case run ')
if __name__=='__main__':
    testcase1=unittest.TestLoader().loadTestsFromTestCase(MyUnitTest)
    filename="C:\\Users\\qiuc2\\Desktop\\test\\test.html"
    fb=open(filename,'wb')
    suite=unittest.TestSuite(testcase1)
    runer=HTMLTestRunner.HTMLTestRunner(stream=fb,title='Report_title',description='Report_description')
    runer.run(suite)
#     suite=unittest.TestSuite()
#     suite.addTest(MyUnitTest('test_2'))
#     suite.addTest(MyUnitTest('test_1'))
#     runner=unittest.TextTestRunner()
#     runner.run(suite)
        