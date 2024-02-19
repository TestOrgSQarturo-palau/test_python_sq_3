init = "Bob is a Bird... Bob is a Plane... Bob is Superman!"
changed = re.sub(r"Bob is", "It's", init) # Noncompliant
changed = re.sub(r"\.\.\.", ";", changed) # Noncompliant


narg=len(sys.argv)
if narg == 1:
    print('@Usage: input_filename nelements nintervals')
    break
