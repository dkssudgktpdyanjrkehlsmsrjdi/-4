# todo.py
import os

filename = "list.txt"

# 참고한 부분: 파일이 있으면 불러오기 (출처: naemazam/todo-python-cli)
def read_list():
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        return [line.strip().split("|") for line in f.readlines()]

# 참고한 부분: 리스트 저장 방식 (출처: naemazam/todo-python-cli)
def save_list(data):
    with open(filename, "w") as f:
        for row in data:
            f.write("|".join(row) + "\n")

# 할 일 보기 기능
def show(data):
    if not data:
        print("\n할 일이 없습니다.\n")
    else:
        print("\n [할 일 목록]")
        for i, row in enumerate(data):
            task, stat = row
            print(f"{i+1}. {task} | 상태: {stat}")
    print()

# 할 일 추가 기능
def add(data):
    t = input("추가할 할 일을 입력하세요: ")
    data.append([t, "미완료"])
    save_list(data)
    print("할 일이 추가되었습니다.\n")

# 완료 처리 기능
def done(data):
    show(data)
    num = int(input("완료 처리할 번호를 입력하세요: "))
    if  num <= len(data):
        data[num - 1][1] = "완료"
        save_list(data)
        print("완료 처리됐습니다.\n")
    else:
         print("잘못된 번호입니다.\n")

# 삭제 기능
def remove(data):
    show(data)
    num = int(input("삭제할 할 일 번호를 입력하세요: "))
    if num <= len(data):
        removed = data.pop(num - 1)
        save_list(data)
        print(f"{removed[0]} 항목이 삭제되었습니다.\n")
    else:
        print("유효하지 않은 번호입니다.\n")

    
# 프로그램 메인
def main():
    items = read_list()

    while True:
        print("==== 할 일 관리 ====")
        print("1. 목록 보기")
        print("2. 새 항목 추가하기")
        print("3. 완료 처리하기")
        print("4. 삭제하기")
        print("5. 종료하기")
        print("===================")

        sel = input("메뉴 번호를 고르세요: ")

        if sel == "1":
            show(items)
        elif sel == "2":
            add(items)
        elif sel == "3":
            done(items)
        elif sel == "4":
            remove(items)
        elif sel == "5":
            print("끝.")
            break
        else:
            print("다시 입력하세요.\n")

if __name__ == "__main__":
    main()
