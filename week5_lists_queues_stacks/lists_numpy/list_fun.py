prices = []

file = open("/home/ubuntu/data5500_spring2025/week5_lists_queues_stacks/lists_numpy/AAPL.txt")
lines = file.readlines()
prices = [float(line) for line in lines]

print(prices)

