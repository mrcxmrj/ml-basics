import argparse
import os
import shutil


def move_first_n_files(src_dir, dst_dir, n):
    if not os.path.exists(src_dir):
        print(f"Source directory '{src_dir}' does not exist.")
        return
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
        print(f"Destination directory '{dst_dir}' created.")

    files = os.listdir(src_dir)
    files = [f for f in files if os.path.isfile(os.path.join(src_dir, f))]

    files_to_move = files[:n]

    if not files_to_move:
        print("No files to move.")
        return

    for file in files_to_move:
        src_path = os.path.join(src_dir, file)
        dst_path = os.path.join(dst_dir, file)
        shutil.move(src_path, dst_path)
        print(f"Moved: {src_path} -> {dst_path}")

    print(f"Moved {len(files_to_move)} files from '{src_dir}' to '{dst_dir}'.")


def main():
    parser = argparse.ArgumentParser(
        description="Move first n files from one directory to another."
    )
    parser.add_argument("src_dir", type=str, help="Source directory path")
    parser.add_argument("dst_dir", type=str, help="Destination directory path")
    parser.add_argument("num_files", type=int, help="Number of files to move")

    args = parser.parse_args()

    move_first_n_files(args.src_dir, args.dst_dir, args.num_files)


if __name__ == "__main__":
    main()
