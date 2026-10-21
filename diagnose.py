with open("logs.txt") as f:
    for line in f:
        line = line.strip()
        if "offline" in line:
            print("PROBLEM: controller offline ->", line)
        else:
            print(line)