class User:
    def __init__(self, id, lv):
        print("user codetree lv 10")
        print(f"user {id} lv {lv}")

a, b = input().split()
u = User(a, b)