import argparse
import csv
import random


def copy_csv_rows(src_csv, dst_csv, n, mode):
    with open(src_csv, mode="r", newline="") as src_file:
        reader = csv.reader(src_file)
        rows = list(reader)

    if len(rows) <= 1:
        print(f"No rows to copy in '{src_csv}'.")
        return

    header = rows[0]
    data = rows[1:]

    if mode == "first":
        rows_to_copy = data[:n]
    elif mode == "last":
        rows_to_copy = data[-n:]
    elif mode == "random":
        rows_to_copy = random.sample(data, min(n, len(data)))
    else:
        print(f"Invalid mode '{mode}'. Use 'first', 'last', or 'random'.")
        return

    if not rows_to_copy:
        print("No rows to copy.")
        return

    with open(dst_csv, mode="w", newline="") as dst_file:
        writer = csv.writer(dst_file)
        writer.writerow(header)
        writer.writerows(rows_to_copy)

    print(
        f"Copied {len(rows_to_copy)} rows from '{src_csv}' to '{dst_csv}' in {mode} mode."
    )


def main():
    parser = argparse.ArgumentParser(
        description="Move first n files from one directory to another."
    )
    parser.add_argument("src", type=str, help="Source file path")
    parser.add_argument("dst", type=str, help="Destination file path")
    parser.add_argument("num_rows", type=int, help="Number of rows to copy")
    parser.add_argument(
        "-m",
        "--mode",
        type=str,
        choices=["first", "last", "random"],
        default="first",
        help="Mode of selecting files to move (first, last, random)",
    )

    args = parser.parse_args()

    copy_csv_rows(args.src, args.dst, args.num_rows, args.mode)


if __name__ == "__main__":
    main()
