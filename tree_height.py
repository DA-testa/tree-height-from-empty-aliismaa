# python3
import sys
import threading

def compute_height(n, parents):
    tree = [[] for i in range(n)]
    root = None
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            tree[parent].append(i)
    stack = [(root, 1)]
    max_height = 0
    while edge:
        node, height = edge.pop()
        if not tree[node]:

            max_height = max(max_height, height)
        else:
            for ch in tree[node]:
                edge.append((ch, height+1))
    return max_height

def main():
  choice = input("Choose the input method")
  if "I" in choice:
    num = int(input())
    val = list(map(int,input().split()))
    print(compute_height(num,val))
  
  elif "F" in choice:
      print("Enter the file name: ")
      filename = input()
      if "a" in filename:
        print("File names with letter a are not allowed")
        return
      with open("test/" + filename,'r') as file:
        num = int(file.readline())
        val = list(map(int,file.readline().split()))
        print(compute_height(num,val))
  else:
    print("Error")
    exit()

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
