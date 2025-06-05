"Run an AI model for QA, NER and RBM and compute the results"
import argparse
import os
import warnings
from typing import Callable

import pandas as pd

warnings.filterwarnings("ignore", message=r"\[W008\]", category=UserWarning)

def save_dataframe_to_csv(data, output: str) -> pd.DataFrame:
    df = pd.DataFrame(data, index=None)
    df.set_index("description", inplace=True)
    df.to_csv(output)
    return df

def process_input(args: argparse.Namespace) -> pd.DataFrame:
    df: pd.DataFrame
    nrows: int = int(args.nrows) if args.nrows else None
    df = pd.read_csv(args.file.name, nrows=nrows, sep="|")
    return df

def run_rbm(input: pd.DataFrame) -> tuple[pd.DataFrame, str]:
    from src.rbm import rbm

    return rbm(input), "rbm"

def parse_args() -> argparse.Namespace:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-f",
        "--file",
        metavar='file',
        type=argparse.FileType('r'),
        help="Run extractions over specific file without evaluation metrics",
    )
    parser.add_argument(
        "-nr",
        "--nrows",
        type=int,
        help="Select the first NROWS rows of the file",
    )
    return parser.parse_args()


def main():
    from src.metrics import Evaluation

    if not os.path.exists("output"):
        os.makedirs("output")

    args: argparse.Namespace = parse_args()
    input: pd.DataFrame = process_input(args)

    results, filenames = run_rbm(input)
    results = results if isinstance(results, list) else [results]

    filenames = filenames if isinstance(filenames, list) else [filenames]

    for result, filename in zip(results, filenames):
        evaluation = Evaluation(input, result)
        evaluation.evaluate()

        save_dataframe_to_csv(result, f"output/{filename}.csv")
        evaluation.save(f"output/evaluation_{filename}.json")

if __name__ == "__main__":
    main()
