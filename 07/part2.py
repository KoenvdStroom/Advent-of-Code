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
    if item not in dir_sizes.keys():
      dir_sizes[item] = 0
    also_add = []
    if(item.count("/") > 1):
      add = item.split("/")[:-1]
      for i in range(len(add)):
        if add[:i] == []:
          continue
        also_add.append('/'.join(add[:i]) + "/")
    for i in directories[item]:
      for j in also_add:
        if j not in dir_sizes.keys():
          dir_sizes[j] = 0
        dir_sizes[j] += int(directories[item][i])
      dir_sizes[item] += int(directories[item][i])
      print(i, dir_sizes)
  current_size = dir_sizes['/']
  free_space = 70000000 - current_size
  amount_to_free = 30000000 - free_space
  print(current_size, free_space, amount_to_free)
  smallest_key = ""
  smallest_value = 10000000000000000000000000000000000000000000000000000
  for k, v in dir_sizes.items():
    if(v >= amount_to_free):
      print(k, v)
      if v < smallest_value:
        smallest_key = k
        smallest_value = v
  print(smallest_key, smallest_value)


if __name__ == "__main__":
  main()