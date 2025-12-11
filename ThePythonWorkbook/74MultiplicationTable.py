
print("\t""1\t 2\t 3\t 4\t 5\t 6\t 7\t 8\t 9\t 10")
print("")

for i in range(1,11,1):
    print(i,end="\t")
    for j in range(1,11,1):
        
        print(j*i,end="\t")
        

    
    print("")
    #print(i)
    
'''# Print the top header row
print("\t", end="")      # Empty corner cell
for col in range(1, 11):
    print(col, end="\t")
print()

# Print each row
for row in range(1, 11):
    print(row, end="\t")   # Row label
    for col in range(1, 11):
        print(row * col, end="\t")
    print()   # Move to next line
'''      