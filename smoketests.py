from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTests
from searchtests import SearchTests

assertions_tests = TestLoader().loadTestsFromTestCase(AssertionsTests)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)

somke_test = TestSuite([assertions_tests, search_test])

kwargs = {
    'output': 'smoke_report'
}

runner = HTMLTestRunner(**kwargs)
runner.run(somke_test)
