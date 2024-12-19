FILE_NAME = "input.txt"

def main():
  with open(FILE_NAME, "r") as f:
    safe_count = 0
    for row in f:
      row = list(map(int, row.strip().split(" ")))
      print(row)
      if (sorted(row) != row) and (sorted(row, reverse=True) != row):
        print(f"skipping because {row} not in order")
      else:
        for i, x in enumerate(row):
          try:
            diff = abs(int(row[i+1]) - int(x))
            print(f"{int(row[i+1])} - {int(x)} = {diff}")
            if diff > 3 or diff < 1:
              break
          except IndexError:
            print("adding to safe count")
            safe_count += 1 
  print(f"safe count: {safe_count}")
           
if __name__ == "__main__":
   main()
