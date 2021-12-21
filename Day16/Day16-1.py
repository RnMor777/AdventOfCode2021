f = open("Day16.txt", "r")
h = f.read().strip()
print(bin(int(h, 16))[2:].zfill(len(h) * 4))
