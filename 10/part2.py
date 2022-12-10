signal_strengths = {0:1}

def get_right_value(x:int):
  keys = signal_strengths.keys()
  smaller = [k for k in keys if k <= x]
  return signal_strengths[max(smaller)]
  


def main():
  with open("input.txt", "r") as f:
    data = f.read().split("\n")
    cycle = 1
    signal_strength = 1
    for i in data:
      if i == "noop":
        cycle += 1
        continue
      cycle += 2
      amount = int(i.split(" ")[1])
      signal_strength += amount
      signal_strengths[cycle] = signal_strength
  
  for i in range(1, max(signal_strengths.keys())+2):
    x = get_right_value(i+1)
    # print("\n", i, x, i+1 % 40, end="\n",)
    if i % 40 in range(x-1, x+2):
      print("#", end="")
    else:
      print(" ", end="")
    if i % 40 == 0:
      print("")


if __name__ == "__main__":
  main()