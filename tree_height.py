#python3
import sys
import threading

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
            height = compute_height(ch)
            max_height = max(max_height, height)
        return max_height + 1

    return compute_height(root)

def main():

    choice = input()
    if "I" in choice:
        name = int(input())
        parents = list(map(int, input().split()))
    elif "F" in choice:
        path = './test/'
        filename = input("Enter file name: ")
        if 'a' in file_name:
            print("File contains letter 'a'")
            return
        with open(path + filename, 'r') as file:
                n = int(file.readline())
                parents = list(map(int, file.readline().split()))
    else:
        print("Error")
        return 
       
    print(compute_height(name, parents))

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
