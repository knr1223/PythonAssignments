def stone_piles(n):
    # List to store the piles
    piles = []
    
    if n % 2 == 0: 
        pile = 2# For even
    else:
        pile = 1# For odd
        
    # Add piles
    while sum(piles) + pile <= n:
        piles.append(pile)
        pile += 2  # Increment for the next pile
    
    return piles

# Get the input
n = int(input("Enter the number of stones: "))

result = stone_piles(n)
print(f"Stones in a single pile = {result}")