
rps = {
  "A": "R",
  "B": "P",
  "C": "S",
  "X": "L",
  "Y": "D",
  "Z": "W"
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
losers = {v: k for k, v in winners.items()}

def calculate_points(one, two):
  if one == two:
    return points["D"]
  winner = winners[one]
  if two == winner:
    return points["W"]
  else:
    return points["L"]

def get_rps(one, action):
  if action == "W":
    return winners[one]
  elif action == "D":
    return one
  else:
    return losers[one]


def main():
  total_points = []
  with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
      one = rps[line.split(" ")[0]]
      action = rps[line.split(" ")[1].strip("\n")]
      two = get_rps(one, action)
      point = points[two] + points[action]
      total_points.append(point)
  print(sum(total_points))


if __name__ == "__main__":
  main()