import random

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
print("Percentage of Heads : %d",pHead)
print("Percentage of Tails : %d",pTail)


