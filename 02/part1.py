
rps = {
  "A": "R",
  "B": "P",
  "C": "S",
  "X": "R",
  "Y": "P",
  "Z": "S"
}
points = {
  "R": 1,
  "P": 2,
  "S": 3,
  "W": 6,
  "L": 0,
  "D": 3
}

winners = {
  "R": "P",
  "P": "S",
  "S": "R"
}

def calculate_points(one, two):
  if one == two:
    return points["D"]
  winner = winners[one]
  if two == winner:
    return points["W"]
  else:
    return points["L"]



def main():
  total_points = []
  with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
      one = rps[line.split(" ")[0]]
      two = rps[line.split(" ")[1].strip("\n")]
      point = points[two] + calculate_points(one, two)
      total_points.append(point)
  print(sum(total_points))


if __name__ == "__main__":
  main()