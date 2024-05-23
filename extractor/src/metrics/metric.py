from typing import Any


class Metric:
    "Class to represent a model's metrics for a specific field"

    def __init__(self, name: str, tp: int = 0, fp: int = 0, fn: int = 0, tn: int = 0):
        self.name = name
        self.tp = tp
        self.fp = fp
        self.fn = fn
        self.tn = tn
        self.error = []

    def __str__(self) -> str:
        return f"{self.name}: TP={self.tp}, FP={self.fp}, FN={self.fn}, TN={self.tn}, Precision={self.precision}, Recall={self.recall}, F1={self.f1}"

    def __repr__(self) -> str:
        return str(self)

    def dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "tp": self.tp,
            "fp": self.fp,
            "fn": self.fn,
            "tn": self.tn,
            "precision": self.precision,
            "recall": self.recall,
            "f1": self.f1,
            "error": self.error,
        }

    @property
    def precision(self) -> float:
        "Get the precision of the metric"
        if (self.tp + self.fp) == 0:
            return 0
        return self.tp / (self.tp + self.fp)

    @property
    def recall(self) -> float:
        "Get the recall of the metric"
        if (self.tp + self.fn) == 0:
            return 0
        return self.tp / (self.tp + self.fn)

    @property
    def f1(self) -> float:
        "Get the F1-score of the metric"
        p = self.precision
        r = self.recall
        if (p + r) == 0:
            return 0
        return 2 * ((p * r) / (p + r))

    def add_error(self, context: str, actual: str, expected: str):
        "Add an error to the metric"
        self.error.append({"context": context, "actual": actual, "expected": expected})
