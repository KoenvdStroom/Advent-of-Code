def main():
  total = 0
  with open("input.txt", "r") as f:
    lines = f.readlines()
    for pair in lines:
      one = pair.split(",")[0].split("-")
      two = pair.split(",")[1].split("-")
      range_one = [*range(int(one[0]), int(one[1])+1)]
      range_two = [*range(int(two[0]), int(two[1])+1)]
      for i in range_one:
        if i in range_two:
          print(range_one, range_two)
          total += 1
          break
  print(total)
    


if __name__ == "__main__":
  main()