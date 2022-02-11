from time import sleep, time


def run(params, output_dir):
    # wait 20 seconds
    for i in range(20):
        print("test simulation started:\n")
        print(params)
        sleep(1)
        with open(f"{output_dir}/simulation_{i}.txt", 'w') as f:
            f.write(str(params))
            f.write(str(time()))

    print("done with all the simulations!")


if __name__ == '__main__':
    run(['a', 10, 199, 20], 'data')
