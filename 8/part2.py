def generate_relevant_items(data, row, column):
  rows = data.split("\n")
  columns = []
  for i in range(len(rows)):
    columns.append("")
    for j in range(len(rows[0])):

      columns[i] += rows[j][i]
  return (rows[row], columns[column])

def check(row, col, index_row, index_col):
  item = row[index_row]
  check_before_row = row[:index_row]
  check_after_row = row[index_row+1:]
  check_before_col = col[:index_col]
  check_after_col = col[index_col+1:]
  before_row = all(int(item) > int(x) for x in check_before_row)
  after_row = all(int(item) > int(x) for x in check_after_row)
  before_col = all(int(item) > int(x) for x in check_before_col)
  after_col = all(int(item) > int(x) for x in check_after_col)
  # print(check_before_row, check_after_row, check_before_col, check_after_col)
  # print(before_row, after_row, before_col, after_col)
  return  before_row or after_row or before_col or after_col

def calc_scenic(row, col, index_row, index_col):
  item = int(row[index_row])
  check_before_row = row[:index_row][::-1]
  check_after_row = row[index_row+1:]
  check_before_col = col[:index_col][::-1]
  check_after_col = col[index_col+1:]
  before_row = all(int(item) > int(x) for x in check_before_row)
  after_row = all(int(item) > int(x) for x in check_after_row)
  before_col = all(int(item) > int(x) for x in check_before_col)
  after_col = all(int(item) > int(x) for x in check_after_col)
  scenic_left = 0
  for i in range(len(check_before_row)):


    if int(check_before_row[i]) < item:


      scenic_left +=1
    else:
      scenic_left+=1
      break
  scenic_right = 0

  for i in range(len(check_after_row)):

    if int(check_after_row[i]) < item:

      scenic_right +=1
    else:
      scenic_right+=1
      break
  scenic_up = 0

  for i in range(len(check_before_col)):

    if int(check_before_col[i]) < item:


      scenic_up+=1
    else:
      scenic_up +=1
      break
  scenic_down = 0

  for i in range(len(check_after_col)):


    if int(check_after_col[i]) < item:


      scenic_down+=1
    else:
      scenic_down+=1
      break
  scenic = scenic_left * scenic_right * scenic_up * scenic_down
  return scenic

def main():
  scenic = []
  with open("input.txt", "r") as f:
    data = f.read()
    total_count = 0
    total_rows = len(data.split("\n")[0])
    total_columns = len(data.split("\n"))
    for i in range(total_rows):
      for j in range(total_columns):
        relevant_info = generate_relevant_items(data, i, j)
        scenic.append(calc_scenic(relevant_info[0], relevant_info[1], j, i))
        # if check(relevant_info[0], relevant_info[1], j, i):
          
        #   total_count += 1
        # print(relevant_info[0], relevant_info[1], relevant_info[0][j])
        # print("\n")
    # print(total_count)
  print(max(scenic))


if __name__ == "__main__":
  main()