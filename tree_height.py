# python3
import sys
import threading
import numpy

def compute_height(n, parents):
    tree = {}
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            tree[parent].append(i)

    def comp_height(node):
        if not tree[node]:
            return 1
        max_height = 0
        for ch in tree[node]:
            height = comp_height(ch)
            max_height = max(max_height, height)
        return max_height + 1
    
    return comp_height(root)

def main():
    choice = input()
    if "I" in choice:
        name = int(input())
        parents = list(map(int, input().split()))
        print(compute_height(name, parents))

    elif "F" in choice:
        print("Enter the file name: ")
        filename = input()
        if "a" in filename:
            print("File names with letter a are not allowed")
            return
        with open("./test/" + filename, mode = "r") as file:
            name = int(file.readline())
            parents = list(map(int, file.readline().split()))
            print(compute_height(name, parents))
    else:
        print("Error")
        exit()

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27) # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
