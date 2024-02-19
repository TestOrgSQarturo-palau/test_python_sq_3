init = "Bob is a Bird... Bob is a Plane... Bob is Superman!"
changed = re.sub(r"Bob is", "It's", init) # Noncompliant
changed = re.sub(r"\.\.\.", ";", changed) # Noncompliant


n = 1
while n < 10:
    if n % 3 == 0:
      print("Found a number divisible by 3", n)
      break
    n = n + 1
