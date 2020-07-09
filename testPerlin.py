import perlin
import random
import matplotlib.pyplot as plt

def show_perlin_noise():
    noise=perlin.Perlin(2)

    x_vals = [x for x in range(900)]
    y_vals = [noise.valueAt(x) for x in x_vals]

    for val in y_vals:
        print(val)
    print(len(y_vals))
    print("max: ",max(y_vals))
    print("min: ",min(y_vals))

    # https://stackoverflow.com/questions/929103/convert-a-number-range-to-another-range-maintaining-ratio

    old_max_y = max(y_vals)
    old_min_y = min(y_vals)
    old_range = old_max_y - old_min_y

    new_max_y = 1.0
    new_min_y = 0
    new_range = new_max_y - new_min_y

    norm = lambda oldVal: (((oldVal - old_min_y) * new_range) / old_range) + new_min_y

    y_vals_norm = [norm(i) for i in y_vals]
    
    #print(y_vals_norm)

    # plt.title("Perlin Noise")
    # plt.xlabel("Time")
    # plt.ylabel("Value")
    # plt.plot(x_vals, y_vals)
    # plt.show()

    plt.title("Perlin Noise")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.plot(x_vals, y_vals_norm)
    plt.show()

if __name__ == '__main__':
    show_perlin_noise()