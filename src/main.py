
from simulation.simulate import run
from drive.drive_api import upload_file
import os

def main():
    file_dir = f"{os.getcwd()}/simulation/ABM-project-group8/figures/experiments"

    files = os.listdir(file_dir)
    for file in files:
        upload_file(file, file_dir)

    # os.mkdir('data')
    # run(['param1', 10, 100, "p"], output_dir=f"{os.getcwd()}/data")

    # filedirs = os.listdir('data')
    # for file in filedirs:
    #     upload_file(file, f"{os.getcwd()}/data")


if __name__ == '__main__':
    main()