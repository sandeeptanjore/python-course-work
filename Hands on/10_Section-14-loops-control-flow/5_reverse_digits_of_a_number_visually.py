n = 436987
step = 1

while n > 0:
    remainder = n % 10
    print(f"Step {step}: Remainder of {n} is {remainder}")
    n = n // 10
    print(f"Step {step}: New number is {n}")
    step += 1
    print("-" * 30)  # Visual separator