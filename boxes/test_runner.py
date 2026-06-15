from django.test.runner import DiscoverRunner
from unittest.runner import TextTestResult


class RichTestResult(TextTestResult):
    def __init__(self, stream, descriptions, verbosity):
        super().__init__(stream, descriptions, verbosity)
        self.executed_tests = []   # stores tests in execution order

    def addSuccess(self, test):
        super().addSuccess(test)
        self.executed_tests.append(('✅ Pass', test))

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.executed_tests.append(('❌ Fail', test))

    def addError(self, test, err):
        super().addError(test, err)
        self.executed_tests.append(('⚠️ Error', test))


class RichTestRunner(DiscoverRunner):
    def get_resultclass(self):
        return RichTestResult

    def run_suite(self, suite, **kwargs):
        result = super().run_suite(suite, **kwargs)

        print("\n\n📋 Test Cases Summary")
        print("=" * 70)
        print(f"| {'#':<3} | {'Test Name':<45} | {'Result':<10} |")
        print("-" * 70)

        for idx, (status, test) in enumerate(result.executed_tests, 1):
            test_name = test.id().split('.')[-1]
            print(f"| {idx:<3} | {test_name:<45} | {status:<10} |")
        print("=" * 70)
        return result