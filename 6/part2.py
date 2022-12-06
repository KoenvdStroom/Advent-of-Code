def main():
  with open("input.txt", "r") as f:
    data = f.read()
    for i in range(13, len(data)):
    
      prev_thirteen = [*data[i-13:i]]
      if data[i] in prev_thirteen or len(prev_thirteen) != len(set(prev_thirteen)):
        continue
      else:
        print(i+1)
        break


if __name__ == "__main__":
  main()