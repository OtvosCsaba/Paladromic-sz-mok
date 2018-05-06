max = 0
eredmeny =0
for i in range(100,1000):
    for e in range(100,1000):
        max = i*e
        max = str(max)
        if max == max[::-1]:
            max = int(max)
            if max > eredmeny:
                eredmeny =max
print(eredmeny)
