import argparse
import os
import random
import shutil


def copy_mode_n_files(src_dir, dst_dir, n, mode):
    if not os.path.exists(src_dir):
        print(f"Source directory '{src_dir}' does not exist.")
        return
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
        print(f"Destination directory '{dst_dir}' created.")

    files = os.listdir(src_dir)
    files = [f for f in files if os.path.isfile(os.path.join(src_dir, f))]

    if mode == "first":
        files_to_copy = files[:n]
    elif mode == "last":
        files_to_copy = files[-n:]
    elif mode == "random":
        files_to_copy = random.sample(files, min(n, len(files)))
    else:
        print(f"Invalid mode '{mode}'. Use 'first', 'last', or 'random'.")
        return

    if not files_to_copy:
        print("No files to copy.")
        return

    for file in files_to_copy:
        src_path = os.path.join(src_dir, file)
        dst_path = os.path.join(dst_dir, file)
        shutil.copy(src_path, dst_path)
        print(f"Copy: {src_path} -> {dst_path}")

    print(f"Copy {len(files_to_copy)} files from '{src_dir}' to '{dst_dir}'.")


def main():
    parser = argparse.ArgumentParser(
        description="Copy first n files from one directory to another."
    )
    parser.add_argument("src_dir", type=str, help="Source directory path")
    parser.add_argument("dst_dir", type=str, help="Destination directory path")
    parser.add_argument("num_files", type=int, help="Number of files to copy")
    parser.add_argument(
        "-m",
        "--mode",
        type=str,
        choices=["first", "last", "random"],
        default="first",
        help="Mode of selecting files to copy (first, last, random)",
    )

    args = parser.parse_args()

    copy_mode_n_files(args.src_dir, args.dst_dir, args.num_files, args.mode)


if __name__ == "__main__":
    main()
