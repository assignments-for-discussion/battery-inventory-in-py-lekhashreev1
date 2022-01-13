
def count_batteries_by_usage(cycles):
  lowcount=0
  highcount=0
  mediumcount=0
  for i in range(len(cycles):
       if cycles[i]<400:
           lowcount+=1
       elif cycles[i]>400 and cycles[i]<919:
            mediumcount+=1
       else:
            high+=1
                    
  return {
    lowcount
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
