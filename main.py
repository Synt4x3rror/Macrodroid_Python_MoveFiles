import os
import shutil
import argparse

def main():
    parser = argparse.ArgumentParser("Copies moves files from source directory to a target directory in a NON RECURSIVE way (No directory nesting).")
    parser.add_argument("source_dir", help="Input Directory", type=str)
    parser.add_argument("target_dir", help="Target Directory", type=str)
    args = parser.parse_args()

    files = os.listdir(args.source_dir)
    for file in files:
        full_path_src = os.path.join(args.source_dir, file)
        full_path_target = os.path.join(args.target_dir, file)
        if(os.path.isfile(full_path_src)):
            try:
                shutil.move(full_path_src, full_path_target)
            except FileExistsError:
                pass
            except Exception as e:
                print(repr(e))

    print('Script Finished!')

if __name__ == '__main__':
    main()