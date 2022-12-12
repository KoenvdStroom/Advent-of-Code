def main():
  total = 0
  with open("input.txt", "r") as f:
    lines = f.readlines()
    for pair in lines:
      one = pair.split(",")[0].split("-")
      two = pair.split(",")[1].split("-")
      if int(one[0]) == int(two[0]) and int(one[1]) == int(two[1]):
        total+=1
      elif int(one[0]) >= int(two[0]) and int(one[1]) <= int(two[1]):
        total+=1
      elif int(one[0]) <= int(two[0]) and int(one[1]) >= int(two[1]):
        total += 1
  print(total)
    


if __name__ == "__main__":
  main()