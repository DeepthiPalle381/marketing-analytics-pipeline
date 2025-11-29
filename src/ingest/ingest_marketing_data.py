import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")
CLEAN_DIR = Path("data/clean")


def clean_bank_marketing(input_path: Path, output_path: Path) -> None:
    """Read raw bank marketing CSV and write a basic cleaned version."""
    print(f"Reading raw data from {input_path}...")
    df = pd.read_csv(input_path, sep=";")


    # Standardize column names: lower_snake_case
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(".", "_")
    )

    # Drop completely empty rows (just in case)
    df = df.dropna(how="all").reset_index(drop=True)

    CLEAN_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Saved cleaned data to {output_path} with {len(df)} rows")


def main() -> None:
    # If you renamed the files, adjust these names:
    train_input = RAW_DIR / "train.csv"
    train_output = CLEAN_DIR / "bank_marketing_train_clean.csv"

    clean_bank_marketing(train_input, train_output)


if __name__ == "__main__":
    main()
