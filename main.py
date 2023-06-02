from PIL import Image, ImageColor

im1 = Image.open("pearl.jpg")
weight, height = im1.size
print(weight, height)
rgbList = []
start_x = int(input("başlangıç X konumunu girin : "))
start_y = int(input("başlangıç Y konumunu girin : "))

finish_x = int(input("Bitiş X konumunu girin : "))
finish_y = int(input("Bitiş Y konumunu girin : "))

for y in range(height):
    rgbList.append([])

for y in range(height):
    for x in range(weight):
        rgbList[y].append(im1.getpixel((x, y)))

rgbList2 = []

for y in range(height):
    if start_y > y:
        continue
    elif y > finish_y:
        break
    else:
        for x in range(weight):
            if start_x > x:
                continue
            elif x > finish_x:
                continue
            else:
                print(rgbList[y][x])
                rgbList2.append(rgbList[y][x])

rListe2 = []
gListe2 = []
bListe2 = []
for i in rgbList2:
    r = i[0]
    rListe2.append(r)
    g = i[1]
    gListe2.append(g)
    b = i[2]
    bListe2.append(b)

# TUM RESMİN RENKLERİ
# rListe = []
# gListe = []
# bListe = []
# for x in rgbList:
#     for i in x:
#         r = i[0]
#         rListe.append(r)
#         g = i[1]
#         gListe.append(g)
#         b = i[2]
#         bListe.append(b)


avgR = 0
avgG = 0
avgB = 0
sum = 0

for x in rListe2:
    sum += x
sum /= len(rListe2)
avgR = sum

sum = 0

for x in gListe2:
    sum += x
sum /= len(gListe2)
avgG = sum

sum = 0

for x in bListe2:
    sum += x
sum /= len(bListe2)
avgB = sum

sum = 0

print(f"ortalama renk :rgb{int(avgR), int(avgG), int(avgB)}")