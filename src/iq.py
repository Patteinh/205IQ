import sys
import math

def normal(x, mean, std_dev):
    return (1 / (std_dev * math.sqrt(2 * math.pi))) * math.exp(-(x - mean) ** 2 / (2 * std_dev ** 2))

def cdf(x, mean, std_dev):
    num_steps = 1000
    step_size = x / num_steps
    total_probability = 0
    for i in range(num_steps):
        total_probability += normal(i * step_size, mean, std_dev) * step_size
    return total_probability

def iqBasic(average, devt):
    distrib = 1 / (devt * math.sqrt(2 * math.pi))

    for i in range(201):
        total = distrib * math.exp(-1 * math.pow(i - average, 2) / (2 * math.pow(devt, 2)))
        print(f"{i} {total:.5f}")

def iqLower(average, devt, min):
    cdf_value = cdf(min, average, devt)
    percentage = cdf_value * 100
    print(f"{percentage:.1f}% of people have an IQ inferior to {int(min)}")

def iqBetween(average, devt, min, max):
    ...

def iq(args):
    if len(args) == 3:
        iqBasic(float(args[1]), float(args[2]))
    elif len(args) == 4:
        iqLower(float(args[1]), float(args[2]), float(args[3]))
    else:
        iqBetween(args[1], args[2], args[3], args[4])