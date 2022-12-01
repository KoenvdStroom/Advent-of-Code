def main():
  counts = []
  with open("input.txt", 'r') as f:
    i=0
    data = f.readlines()
    for item in data:
      if item == "\n":
        i += 1
        continue
      if(len(counts) != i+1):
        counts.append(0)
      counts[i] += int(item)
  counts.sort()
  counts.reverse()
  # Part one
  print(counts[0])
  # Part two
  total = counts[0] + counts[1] + counts[2]
  print(total)

if __name__ == "__main__":
  main()