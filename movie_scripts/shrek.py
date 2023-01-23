import io
import os

def getShrekScript():
    paragraphs = []
    
    script_dir = os.path.dirname(__file__)
    rel_path = "shrek.txt"
    abs_file_path = os.path.join(script_dir, rel_path)

    with io.open(abs_file_path, mode="r", encoding="utf-8") as file:
        temp = ""
        for line in file:
            if line == '\n':
                paragraphs.append(temp.replace('\n', ' ').strip())
                temp = ""
            else:
                temp += line

    return paragraphs

if __name__ == "__main__":
    print(getShrekScript())
