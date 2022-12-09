import math
head_position = [0,0]
tail_position = [0,0]

def move_head(action):
  if action == "R":
    head_position[0] += 1
  elif action == "L":
    head_position[0] -= 1
  elif action == "U":
    head_position[1] += 1
  elif action == "D":
    head_position[1] -= 1

def calc_diagonal_distance():
  return math.floor(math.sqrt((head_position[0]-tail_position[0])**2 + (head_position[1] -tail_position[1])**2))

def move_tail():
  horizontal_distance = head_position[0]-tail_position[0]
  vertical_distance = head_position[1] - tail_position[1]

  if abs(horizontal_distance) != 2 and abs(vertical_distance) != 2:
    return 
  
  if abs(horizontal_distance) >= 1:
    tail_position[0] += 1 if horizontal_distance > 0 else -1
  if abs(vertical_distance) >= 1:
    tail_position[1] += 1 if vertical_distance > 0 else -1
  

def main():
  history = []
  action_string = ""
  with open("input.txt", "r") as f:
    data = f.read().split("\n")
    for i in data:
      (action, amount) = i.split(" ")
      action_string += int(amount) * action
  
  for i in action_string:
    move_head(i)
    move_tail()
    history.append(','.join(map(str, tail_position)))
  print(len(set(history)))
      

if __name__ == "__main__":
  main()