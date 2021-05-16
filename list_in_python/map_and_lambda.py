cir = lambda r: 2 * r * 3.14

data = [2,6,3,5.7,4,9,6,3,6,1,4,6,87,56,45,23,6,45,33,76,8,22,32]

results = []

#normal
for radius   in data:
    out = cir(radius)
    results.append(out)
print(results)

#comprehension
results = [cir(radius)for radius in data]
print(results)

#map function
results = list(map(cir,data))
print(results)