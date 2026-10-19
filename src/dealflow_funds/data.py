import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data" / "synthetic" / "sample.csv"


def load_rows(path=DATA):
    """Load the synthetic sample dataset (fabricated data)."""
    with open(path, newline="") as f:
        return list(csv.DictReader(f))
