import os
import drive_api
import lorem

def main():
    for i in range(2):
        text = lorem.paragraph()
        with open(f"{os.getcwd()}/data/file-{i}.txt", "w") as f:
            f.write(text)

        drive_api.upload_file(f'file-{i}.txt', "data")



if __name__ == '__main__':
    main()