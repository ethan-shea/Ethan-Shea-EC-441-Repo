import numpy as np
import matplotlib.pyplot as plt
import random

# ===== PARAMETERS =====
num_stations_list = range(5, 55, 5)
transmission_prob = 0.2
time_steps = 10000
sense_prob = 0.2

throughputs = []
collision_rates = []

# ===== SIMULATION =====
for num_stations in num_stations_list:
    successes = 0
    collisions = 0

    backoff = [0] * num_stations
    channel_busy = False

    for t in range(time_steps):
        transmitting_nodes = []

        for i in range(num_stations):
            if backoff[i] > 0:
                backoff[i] -= 1
            else:
                if channel_busy:
                    # mostly defer, rarely transmit
                    if random.random() > sense_prob:
                        continue
                    if random.random() < transmission_prob:
                        transmitting_nodes.append(i)
                else:
                    if random.random() < transmission_prob:
                        transmitting_nodes.append(i)


        if len(transmitting_nodes) == 1:
            successes += 1

        elif len(transmitting_nodes) > 1:
            collisions += 1
            for i in transmitting_nodes:
                backoff[i] = random.randint(1, 10)
        if len(transmitting_nodes) > 0:
            channel_busy = True
        else:
            channel_busy = False

    throughput = successes / time_steps
    collision_rate = collisions / time_steps

    throughputs.append(throughput)
    collision_rates.append(collision_rate)

# ===== PLOTTING =====
plt.figure()

plt.plot(num_stations_list, throughputs, label="Throughput")
plt.plot(num_stations_list, collision_rates, label="Collision Rate")

plt.xlabel("Number of Stations")
plt.ylabel("Rate")
plt.title("CSMA/CA Simulation (with Backoff)")
plt.legend()

plt.show()
