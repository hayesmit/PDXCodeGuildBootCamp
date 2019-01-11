#SockSorter.py

import random

sock_types = ['ankle', 'crew', 'calf', 'thigh']
my_socks = {'ankle': 0, 'crew': 0, 'calf': 0, 'thigh': 0}
for x in range(100):
    sock = random.choice(sock_types)
    my_socks[sock] += 1


for
