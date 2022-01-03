months = [1,2,3,4,5,6,7,8,9,10,11,12]
variations = []

sInx = 0
for startM in months:
  print(sInx, startM)    
  if sInx != len(months) - 1:
      for endM in months[sInx+1:]:
          variations.append('{0}-{1}'.format(startM, endM))
  sInx = sInx + 1
  
print(variations, len(variations))
# 66 variations in one year
    