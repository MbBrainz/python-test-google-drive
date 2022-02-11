from simulation.simulate import run
from drive.drive_api import upload_file
import os

def main():
    os.mkdir('data')
    run(['param1', 10, 100, "p"], output_dir=f"{os.getcwd()}/data")

    filedirs = os.listdir('data')
    for file in filedirs:
        upload_file(file, f"{os.getcwd()}/data")


if __name__ == '__main__':
    main()