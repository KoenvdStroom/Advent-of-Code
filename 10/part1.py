signal_strengths = {}

def get_right_value(x:int):
  keys = signal_strengths.keys()
  smaller = [k for k in keys if k <= x]
  return x*signal_strengths[max(smaller)]
  


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

  print(signal_strengths)
  result = map(get_right_value,[20, 60, 100, 140, 180, 220])
  print(sum(list(result)))


if __name__ == "__main__":
  main()