'''
Programe takes a list of numbers, and one target numbers.
IF  pair of numbers equals the traget, programe returns the pair.
for multiple solutions programe retun all instances
'''
def pair_sum(array, k):
  if (len(array) < 2):
    return "The list doesn't have enough inputs"

  seen = set() # iretable set object, empty
  output = set() 
  
  for num in array:
    target = k - num

    if target not in seen:
      seen.add(num)
    else:
      output.add((num,target))
  return output  

output = pair_sum([0,1,2,2,3,4],4)
print('\n'.join(map(str,list(output))))