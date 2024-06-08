"Run an AI model for QA, NER and RBM and compute the results"
import argparse
import os
import warnings
from typing import Callable

import pandas as pd

warnings.filterwarnings("ignore", message=r"\[W008\]", category=UserWarning)

INPUT_WITH_INFERENCES: str = "input/ground_truth_100.csv"
INPUT_WITHOUT_INFERENCES: str = "input/ground_truth_100_sin_inferencias.csv"


def save_dataframe_to_csv(data, output: str) -> pd.DataFrame:
    df = pd.DataFrame(data, index=None)
    df.set_index("descripcion", inplace=True)
    df.to_csv(output, sep="|")
    return df


def process_input(args: argparse.Namespace) -> pd.DataFrame:
    input: str = INPUT_WITH_INFERENCES if args.inferences else INPUT_WITHOUT_INFERENCES
    df: pd.DataFrame = pd.read_csv(input, sep="|")
    return df


def process_result(result: pd.DataFrame, args: argparse.Namespace) -> pd.DataFrame:
    from src.helper import descubrir_nuevos

    if args.inferences:
        clean_result = result.apply(descubrir_nuevos, axis=1)
        assert type(clean_result) == pd.DataFrame
        result = clean_result
    return result


def run_qa(input: pd.DataFrame) -> tuple[list[pd.DataFrame], list[str]]:
    from src.qa import qa

    models: list[str] = [
        "rvargas93/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es",
        "mrm8488/bert-base-spanish-wwm-cased-finetuned-spa-squad2-es",
        "timpal0l/mdeberta-v3-base-squad2",
    ]

    results = [qa(input, model) for model in models]
    return results, [model.split("/")[0] for model in models]


def run_rbm(input: pd.DataFrame) -> tuple[pd.DataFrame, str]:
    from src.rbm import rbm

    return rbm(input), "rbm"


def run_ner(input: pd.DataFrame) -> tuple[pd.DataFrame, str]:
    from src.ner import ner

    return ner(input), "ner"


def parse_args(functions: list[str]) -> argparse.Namespace:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument(
        "-s",
        "--strategy",
        choices=functions,
        required=True,
        help="Select the strategy",
    )
    parser.add_argument(
        "-i",
        "--inferences",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="Run with inferences",
    )
    return parser.parse_args()


def main():
    from src.metrics import Evaluation

    if not os.path.exists("output"):
        os.makedirs("output")

    functions: dict[str, Callable] = {
        "qa": run_qa,
        "rbm": run_rbm,
        "ner": run_ner,
    }

    args: argparse.Namespace = parse_args(list(functions.keys()))
    input: pd.DataFrame = process_input(args)

    results, filenames = functions[args.strategy](input)
    results = results if isinstance(results, list) else [results]
    results = [process_result(result, args) for result in results]

    filenames = filenames if isinstance(filenames, list) else [filenames]

    for result, filename in zip(results, filenames):
        evaluation = Evaluation(input, result)
        evaluation.evaluate()

        save_dataframe_to_csv(result, f"output/{filename}.csv")
        evaluation.save(f"output/evaluation_{filename}.json")


if __name__ == "__main__":
    main()
