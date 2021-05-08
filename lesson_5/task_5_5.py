src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

unique_values = set()
tmp = set()
for el in src:
   if el not in tmp:
       unique_values.add(el)
   else:
       unique_values.discard(el)
   tmp.add(el)

# Save source list items order
unique_values_ord = [el for el in src if el in unique_values]

print(unique_values_ord)
