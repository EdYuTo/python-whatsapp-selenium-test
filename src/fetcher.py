import io
import os

def __getPath(of):
    script_dir = os.path.dirname(__file__)
    rel_path = f'data/{of}'
    return os.path.join(script_dir, rel_path)

def __getPreprocessed(path):
    paragraphs = []
    
    file_path = __getPath(path)

    with io.open(file_path, mode='r', encoding='utf-8') as file:
        temp = ''
        for line in file:
            if line == '\n':
                paragraphs.append(temp.replace('\n', ' ').strip())
                temp = ''
            else:
                temp += line

    return paragraphs

def getShrekScript():
    return __getPreprocessed('shrek.txt')

def getBrNationalAnthem():
    return __getPreprocessed('br_national_anthem.txt')

def getBible():
    paragraphs = []
    
    file_path = __getPath('bible.tsv')

    with open(file_path, "r") as file:
        for line in file:
            paragraphs.append(line.split("\t")[5].strip())
    
    return paragraphs

if __name__ == "__main__":
    print(getBrNationalAnthem())
