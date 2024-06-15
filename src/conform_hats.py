def please_conform(caps:str)-> None:
    start = forward = backward = 0
    intervals = []
    for i in range(1 , len(caps)):
        if caps[start] != caps[i]:
            intervals.append((start, i-1, caps[start]))
            if caps[start] == "F" :
                forward += 1
            else:
                backward += 1
            start = i
        intervals.append((start, len(caps)-1, caps[start]))
        if caps[start] == "F":
            forward += 1
        else:
            backward += 1
        flip = "F" if forward < backward else "B"
        for t in intervals:
            if t[2] == flip:
                print("People in positions", t[0], "through", t[1], "flip your caps!")

if __name__ == "__main__":
    caps = "FFFBFFBFF"
    please_conform(caps)
