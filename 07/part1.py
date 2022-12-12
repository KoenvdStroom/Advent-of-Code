directories={}

def cd(directory, current_directory):
  if(directory == ".."):
    # print(current_directory.split("/")[:-2])  
    return '/'.join(current_directory.split("/")[:-2])+'/'
  elif(directory == "/"):
    return "/"
  else:
    return current_directory + f"{directory}/"

def main():
  current_directory = ""
  with open("input.txt", "r") as f:
    data = f.readlines()
    for i in data:
      i = i.strip("\n")
      if i.startswith("$"):
        command = i.split(" ")
        if command[1] == "cd":
          current_directory = cd(''.join(command[2:]), current_directory)
      else:
        d = i.split(" ")
        if d[0] == "dir": 
          directories[current_directory+d[1]+"/"] = {}
        else:
          if current_directory not in directories.keys():
            directories[current_directory] = {}
          directories[current_directory].update({d[1]:d[0]})
  dir_sizes = {}
  for item in directories.keys():
    dir_sizes[item] = 0
    also_add = []
    if(item.count("/") > 2):
      print(item)
      add = item.split("/")[:-1]
      for i in range(len(add)):
        if add[:i] == []:
          continue
        also_add.append('/'.join(add[:i]) + "/")
        print(add[:i])
    for i in directories[item]:
      for j in also_add:
        dir_sizes[j] += int(directories[item][i])
      dir_sizes[item] += int(directories[item][i])
  total = 0
  for i in dir_sizes:
    if dir_sizes[i] < 100000:
      total += dir_sizes[i]
  print(total)


if __name__ == "__main__":
  main()