name = "Bruno"

for letter in name:
    print(letter)

print("\n")
# Using range to iterate over a sequence of numbers
for i in range(1, 11, 2):
    print(i)

print("\n")

name = "Bruno"
for i in range(10):
    print(f"{i+1} {name}")

print("\n")

#Loop ao contrário
for i in range(10, 0, -1):
    print(i)


print("\n")

nomes = ["Julia", "Alberto", "Bruno", "Lucas"]

for i in range(len(nomes)):
    if nomes[i] == "Bruno":
      continue
    print(nomes[i])
        