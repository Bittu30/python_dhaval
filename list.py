avengers = ["Iron man", "Captain America", " Black widow", "Hulk", "Thor", "HawkEye"]

print(len(avengers))

avengers.append("Spider-Man")
print(avengers)
avengers.remove("Captain America")
print(avengers)
avengers = ["Captain America"]+avengers

print("the new order of avengers are {}".format(avengers))

avengers.sort()
print(avengers)

