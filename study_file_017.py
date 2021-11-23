import tarfile
from pathlib import Path

def create_tar_archive():
# images/newspaper/monsters에 있는 파일을 tar형식으로 생성
    file_list = []

    for path in Path("images/newspaper/monsters").iterdir():
        file_list.append("images/newspaper/monsters/" + path.stem + path.suffix)
    
    with tarfile.open("monster_archive.tar", "w") as tar:
        for file in file_list:
            tar.add(file)

def add_to_tar_archive():
# # images/movies/monsters에 있는 파일을 기존 tar파일에 추가
    with tarfile.open("monster_archive.tar", "a") as tar:
        tar.add("images/movies/monsters/monsters_new__new_monster01.png")
        tar.add("images/movies/monsters/monsters_new__new_monster03.png")
        tar.add("images/movies/monsters/monsters_new__new_monster05.png")

def extract_tar():
# images/movies/monsters/monsters_new__new_monster01.png만 압축해제
    with tarfile.open("monster_archive.tar", "r") as tar:
        tar.extract("images/movies/monsters/monsters_new__new_monster01.png")

def extract_all():
# extracted_monster_files에 모든 파일을 압축해제
    with tarfile.open("monster_archive.tar", "r") as tar:
        tar.extractall("extracted_monster_files")

if __name__ == "__main__":
    # create_tar_archive()
    # add_to_tar_archive()
    # extract_tar()
    extract_all()