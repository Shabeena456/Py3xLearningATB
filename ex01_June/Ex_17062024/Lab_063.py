def print_argument(*args):  # ["pramod","amit","lucky"]
    for i in args:
        print(i, end="\n")
print_argument("pramod", "amit", "lucky")


print("========================")

# *args -> List
a = ["pramod", "amit", "lucky"]
for i in a:
    print(i)


for i in range(1, 10):
    print(i)
