from __future__ import annotations
from typing import List


class TestResult:
    def __init__(self) -> None:
        self.run_count = 0
        self.failure_count = 0

    def test_started(self) -> None:
        self.run_count += 1

    def test_failed(self) -> None:
        self.failure_count += 1

    def summary(self) -> str:
        return f"{self.run_count} run, {self.failure_count} failed"


class TestSuite:
    def __init__(self) -> None:
        self.tests: List[TestCase] = []

    def add(self, test: TestCase) -> None:
        self.tests.append(test)

    def run(self, result: TestResult) -> None:
        for test in self.tests:
            test.run(result)


class TestCase:
    def __init__(self, name: str) -> None:
        self.name = name

    def run(self, result: TestResult) -> None:
        result.test_started()
        self.set_up()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.test_failed()
        self.tear_down()
        return result

    def set_up(self) -> None:
        pass

    def tear_down(self) -> None:
        pass


class WasRun(TestCase):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def test_method(self) -> None:
        self.log += "test_method "

    def set_up(self) -> None:
        self.log = "set_up "

    def tear_down(self) -> None:
        self.log += "tear_down "

    def test_broken_method(self) -> None:
        raise Exception


class TestCaseTest(TestCase):
    def set_up(self):
        self.result = TestResult()

    def test_template_method(self) -> None:
        test = WasRun("test_method")
        test.run(self.result)
        assert test.log == "set_up test_method tear_down "

    def test_result(self) -> None:
        test = WasRun("test_method")
        test.run(self.result)
        assert "1 run, 0 failed" == self.result.summary()

    def test_failed_result(self) -> None:
        test = WasRun("test_broken_method")
        test.run(self.result)
        assert "1 run, 1 failed" == self.result.summary()

    def test_failed_result_formatting(self) -> None:
        self.result.test_started()
        self.result.test_failed()
        assert "1 run, 1 failed" == self.result.summary()

    def test_suite(self):
        suite = TestSuite()
        suite.add(WasRun("test_method"))
        suite.add(WasRun("test_broken_method"))
        suite.run(self.result)
        assert "2 run, 1 failed" == self.result.summary()


if __name__ == "__main__":
    suite = TestSuite()
    suite.add(TestCaseTest("test_template_method"))
    suite.add(TestCaseTest("test_result"))
    suite.add(TestCaseTest("test_failed_result"))
    suite.add(TestCaseTest("test_failed_result_formatting"))
    suite.add(TestCaseTest("test_suite"))
    result = TestResult()
    suite.run(result)
    print(result.summary())
