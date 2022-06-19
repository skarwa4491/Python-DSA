from nis import cat


def findLimit(i):
    try:
        findLimit(i+1)
    except Exception as e:
        print("The limit of recursion is ", i)

findLimit(1)