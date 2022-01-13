
def count_batteries_by_usage(cycles):
     return {
       "lowcount"=0,
       "mediumcount"=0,
       "highcount"=0
     }
       


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  for i in counts:
      if(i<400):
           counts["lowcount"]+=1
      elif(i>=400 and i<=919):
           counts["mediumcount"]+=1
      else:
           counts["highcount"]+=1
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
