import upload
import lorem

def main():
    for i in range(2):
        text = lorem.paragraph()
        with open(f"./data/file-{i}.txt", "w") as f:
            f.write(text)

        upload.upload_file(f'./data/file-{i}.txt')



if __name__ == '__main__':
    main()