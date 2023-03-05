# python3
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
    FileName = input()
    if "a" in FileName:
      print("File names with letter a are not allowed")
      return
      with open("test/" + FileName, ) as file:
        name = int(file.readline())
        parents = list(map(int, file.readline().split()))
        print(compute_height(name, parents))
    else:
      print("Error")
      exit()

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
main()
