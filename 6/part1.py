def main():
  with open("input.txt", "r") as f:
    data = f.read()
    for i in range(13, len(data)):
    
      prev_three = [*data[i-13:i]]
      if data[i] in prev_three or len(prev_three) != len(set(prev_three)):
        continue
      else:
        print(i+1)
        break


if __name__ == "__main__":
  main()