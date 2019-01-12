#lab18-Peaks_and_Valleys.py

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def drawing(data):
    everest = max(data)
    while everest > 0:
        for i in range(len(data)):
            if data[i] >= everest:
                print("x", end='')
            elif data[i] < everest:
                print(" ", end="")
        everest -= 1
        print("\n")


def peaks(data):
    peaksL = []
    for i in range(len(data)):
        if 0 < i < len(data)-1:
           # print(data[i], i, data[i-1])
            if data[i - 1] < data[i] > data[i + 1]:
                peaksL.append(i)
    return peaksL

def valleys(data):
    vals = []
    for i in range(len(data)):
        if 0 < i < len(data)-1:
            if data[i - 1] > data[i] < data[i + 1]:
                vals.append(i)
    return vals


print(peaks(data))
print(valleys(data))
drawing(data)
peaks_and_valleys = peaks(data), valleys(data)
