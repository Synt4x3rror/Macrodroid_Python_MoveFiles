import os
import pathlib
import sys

def main():
    setup_process = True
    # List hard drives and capacity using lsblk (Prerequisite)

    # Setup devices that will be copied from/to
    while(setup_process):
        os.system('clear')
        source, target = __target_select()
        print(f"Use {source} as Source and {target} as Target?")
        confirm = input("[Y]es\t|\t[N]o\t|\t[Q]uit\n")
        if(confirm.upper() == 'Q'):
            sys.exit('Exit script. No changes were made!')
        elif(confirm.upper() == 'Y'):
            setup_process = False

    print('Script Finished!')

def __target_select():
    """
    Takes the user input of which filesystem should be used as input or output.
    :return: source, target
    :rtype: list[str]
    """
    source = input("Select Source Device: ")
    target = input("Select Target device: ")

    return source, target


if __name__ == '__main__':
    main()