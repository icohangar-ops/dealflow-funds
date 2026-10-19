from .data import load_rows


def main():
    rows = load_rows()
    print(f"dealflow-funds: {len(rows)} synthetic rows, columns: {list(rows[0])}")
    print("Scaffold only - features are built on event day (Oct 24).")


if __name__ == "__main__":
    main()
