a = {}
try:
    a[5]
except KeyError:
    raise  # Noncompliant


if not a == 2:        # Noncompliant
    b = not i < 10    # Noncompliant
