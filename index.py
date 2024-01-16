import random
import itertools

print("Enter number of times to flip the coin:")
n=int(input())

def flip():
	return random.choice(['heads','tails'])


result = [flip() for _ in range(n)]
print(result)

num_heads=result.count('heads')
num_tails=result.count('tails')
pHead=(num_heads/n)*100
pTail=(num_tails/n)*100
print("Percentage of Singlet Heads : %d",pHead)
print("Percentage of Singlet Tails : %d",pTail)

dresults=list(itertools.product(result,repeat=2))
double = list(itertools.product(['heads','tails'],repeat=2))
print(dresults)
for combination in double:
            count = dresults.count(combination)
            percentage = (count / len(dresults)) * 100
            print(f"Percentage of {combination}: {percentage:.2f}%")
