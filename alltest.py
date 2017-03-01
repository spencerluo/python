import unittest
testsuite = unittest.TestSuite()
discover = unittest.defaultTestLoader.discover(r'testcases', pattern='test*.py')
for test in discover:
    for test_case in test:
        testsuite.addTests(test_case)

runner = unittest.TextTestRunner()
runner.run(testsuite)