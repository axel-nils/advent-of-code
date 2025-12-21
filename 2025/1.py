def solve(file):
   position = 50
   zeroes = 0
   with open(file) as f:
      full_list = f.readlines()
   for line in full_list:
      direction = -1 if line[0] == "L" else 1
      amount = int(line[1:].strip())
      position += direction * amount
      if position % 100 == 0:
         zeroes += 1
   print(zeroes)

if __name__ == "__main__":
   solve("1.txt")
