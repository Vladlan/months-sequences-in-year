def count_months_variations(months_range):
  months = list(range(1,months_range+1))
  variations = []

  sInx = 0
  for startM in months:
    if sInx != len(months) - 1:
        for endM in months[sInx+1:]:
            variations.append('{0}-{1}'.format(startM, endM))
    sInx = sInx + 1
    
  print(variations)
  return len(variations)
  

vars_in_year = count_months_variations(12)
print(vars_in_year) # 66 variations in one year

vars_in_3years = count_months_variations(12*3)
print(vars_in_3years) # 630 variations in one year