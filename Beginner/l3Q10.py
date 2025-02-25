def count_customers_left(N, S):
  occupied_computers = set()
  customers_in_cafe = set()
  left_without_service = 0

  for customer in S:
    if customer in customers_in_cafe:  # If customer is leaving
      customers_in_cafe.remove(customer)
      occupied_computers.discard(customer)
    else:  # If customer is arriving
      customers_in_cafe.add(customer)
      if len(occupied_computers) < N:  # If a computer is available
        occupied_computers.add(customer)
      else:  # No computers available, customer leaves
        left_without_service += 1

  return left_without_service

N = int(input("Enter the number of computers in the cafe: "))
S = input("Enter the customer sequence: ")

customers_left = count_customers_left(N, S)

print("\nNumber of customers who left without using a computer:", customers_left)
