#lab18-Peaks_and_Valleys.py

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def drawing(data):
    everest = max(data)
    visual = []
    while everest > 0:
        for i in range(len(data)):
            row = []
            if data[i] >= everest:
                row.append("x")
            elif data[i] < everest and row[i-1] != " " or row[i] == row[0]:
                row.append(" ")
            else:
                row.append("o")
        visual.append(''.join(row))
        everest -= 1
        print("\n")
#elif the point is beween two peaks and less than everest

def peaks(data):
    peaksL = []
    for i in range(1, len(data) - 1):
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
