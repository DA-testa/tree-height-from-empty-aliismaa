# python3
import sys
import threading

def compute_height(n, parents):
    tree = {}
    for i in range(n):
        tree[i] = []
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
        path = './test/'
        filename = input("Enter the file name: ")
        
        if "a" in filename:
            print("File names with letter a are not allowed")
            return
        try:
          with open(path + filename, 'r', encoding='utf-8') as file:
            name = int(file.readline())
            parents = list(map(int, file.readline().split()))
            print(compute_height(name, parents))
        except FileNotFoundError:
            print("Error: File not found")
            return
    else:
        print("Error")

    print(compute_height(name, parents))
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27) # new thread will get stack of such size
threading.Thread(target=main).start()
main()
