# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print ("Length it_companies variable:",len(it_companies))
### Exercises: lvl1 
## add "Twitter" to it_companies
it_companies.add("Twitter")
print (it_companies)

## Insert multiple IT companies at once
it_companies.update( {'Rah', "mememe", 'kyah'})
print(it_companies)

it_companies.remove('Rah')
print(it_companies)

### EXERCISE LVL 2
C = A.union(B)
print (C)
intersection = A.intersection(B)
print (intersection)
subset = A.issubset(B)
print (subset)
disjoint = A.isdisjoint(B)
print ("\n")
print ("Are A and B disjoint sets:",disjoint)

print ("What is the symmetric difference between A and B:", A.difference(B))
print ("NONE")
print ("What is the symmetric difference between B and A:", B.difference(A))
del A
del B
del it_companies

