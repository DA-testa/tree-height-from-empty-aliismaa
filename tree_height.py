# python3
import sys
import threading

def compute_height(n, parents):
  tree = {}
  for i in range(n):
    if parents[i] == -1:
      root = i
    else:
      tree[parents[i]].append(i)
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
