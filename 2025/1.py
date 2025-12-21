def solve_part_one(file):
   position = 50
   zeroes = 0
   with open(file) as f:
      full_list = f.readlines()
   for line in full_list:
      direction = -1 if line[0] == "L" else 1
      amount = int(line[1:].strip())
      position = (position + direction*amount) % 100
      if position == 0:
         zeroes += 1
   print(zeroes)

def solve_part_two(file):
   position = 50
   zeroes = 0
   passed_zeroes = 0
   with open(file) as f:
      full_list = f.readlines()
   for line in full_list:
      direction = -1 if line[0] == "L" else 1
      if position == 0 and direction == -1:
         position += 100
      amount = int(line[1:].strip())
      if direction == -1:
         while position - amount < 0:
            passed_zeroes += 1
            amount -= 100
      else:
         while position + amount > 100:
            passed_zeroes += 1
            amount -= 100
      position = (position + direction*amount) % 100
      if position == 0:
         zeroes += 1
   print(zeroes+passed_zeroes)
if __name__ == "__main__":
   solve_part_one("1.txt")
   solve_part_two("1.txt")

