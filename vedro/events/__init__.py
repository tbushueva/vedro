from argparse import Namespace
from typing import List

from ..core._arg_parser import ArgumentParser
from ..core._event import Event
from ..core._exc_info import ExcInfo
from ..core._report import Report
from ..core._scenario_result import ScenarioResult
from ..core._step_result import StepResult
from ..core._virtual_scenario import VirtualScenario


class ArgParseEvent(Event):
    def __init__(self, arg_parser: ArgumentParser) -> None:
        self._arg_parser = arg_parser

    @property
    def arg_parser(self) -> ArgumentParser:
        return self._arg_parser

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._arg_parser!r})"


class ArgParsedEvent(Event):
    def __init__(self, args: Namespace) -> None:
        self._args = args

    @property
    def args(self) -> Namespace:
        return self._args

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._args!r})"


class StartupEvent(Event):
    def __init__(self, scenarios: List[VirtualScenario]) -> None:
        self._scenarios = scenarios

    @property
    def scenarios(self) -> List[VirtualScenario]:
        return self._scenarios

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._scenarios!r})"


class _ScenarioEvent(Event):
    def __init__(self, scenario_result: ScenarioResult) -> None:
        self._scenario_result = scenario_result

    @property
    def scenario_result(self) -> ScenarioResult:
        return self._scenario_result

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._scenario_result!r})"


class ScenarioSkippedEvent(_ScenarioEvent):
    pass


class ScenarioFailedEvent(_ScenarioEvent):
    pass


class ScenarioRunEvent(_ScenarioEvent):
    pass


class ScenarioPassedEvent(_ScenarioEvent):
    pass


class _StepEvent(Event):
    def __init__(self, step_result: StepResult) -> None:
        self._step_result = step_result

    @property
    def step_result(self) -> StepResult:
        return self._step_result

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._step_result!r})"


class StepRunEvent(_StepEvent):
    pass


class StepFailedEvent(_StepEvent):
    pass


class StepPassedEvent(_StepEvent):
    pass


class ExceptionRaisedEvent(Event):
    def __init__(self, exc_info: ExcInfo) -> None:
        self._exc_info = exc_info

    @property
    def exc_info(self) -> ExcInfo:
        return self._exc_info

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._exc_info!r})"


class CleanupEvent(Event):
    def __init__(self, report: Report) -> None:
        self._report = report

    @property
    def report(self) -> Report:
        return self._report

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._report!r})"


__all__ = ("Event", "ArgParseEvent", "ArgParsedEvent", "StartupEvent", "ScenarioRunEvent",
           "ScenarioSkippedEvent", "ScenarioFailedEvent", "ScenarioPassedEvent",
           "StepRunEvent", "StepFailedEvent", "StepPassedEvent", "ExceptionRaisedEvent",
           "CleanupEvent")
