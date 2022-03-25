class TestResult:
    def __init__(self) -> None:
        self.runCount = 0
        self.errorCount = 0
    def testStarted(self) -> None:
        self.runCount += 1
    def testFailed(self) -> None:
        self.errorCount += 1
    def summary(self) -> str:
        return f'{self.runCount} run, {self.errorCount} failed'

class TestCase:
    def __init__(self, name: str) -> None:
        self.name = name
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    def run(self,result: TestResult) -> None:
        result.testStarted()
        print(self.name)
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()
        self.tearDown()

class TestSuite:
    def __init__(self) -> None:
        self.tests: list[TestCase] = []
    def add(self, test: TestCase):
        self.tests.append(test)
    def run(self, result: TestResult):
        for test in self.tests:
            test.run(result)
class WasRun(TestCase):
    def setUp(self) -> None:
        self.log = 'setUp '
    def testMethod(self) -> None:
        self.log = self.log + 'testMethod '
    def testBrokenMethod(self) -> None:
        raise Exception
    def tearDown(self) -> None:
        self.log = self.log + 'tearDown '

class TestCaseTest(TestCase):
    def setUp(self) -> None:
        self.result = TestResult()
    def testTemplateMethod(self) -> None:
        test = WasRun('testMethod')
        test.run(self.result)
        assert('setUp testMethod tearDown ' == test.log)
    def testResult(self) -> None:
        test = WasRun('testMethod')
        test.run(self.result)
        assert('1 run, 0 failed' == self.result.summary())
    def testFailedResult(self) -> None:
        test = WasRun('testBrokenMethod')
        test.run(self.result)
        assert('1 run, 1 failed' == self.result.summary())

class TestResultTest(TestCase):
    def testFailedResultFormatting(self) -> None:
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert('1 run, 1 failed' == result.summary())

suite = TestSuite()
result = TestResult()

suite.add(WasRun('testMethod'))
suite.add(TestCaseTest('testTemplateMethod'))
suite.add(TestCaseTest('testResult'))
suite.add(TestCaseTest('testFailedResult'))
suite.add(TestResultTest('testFailedResultFormatting'))

suite.run(result)
print(result.summary())
