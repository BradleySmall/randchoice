""" Select a value from a stream with equal probablility """
import random


def main():
    """ Main driver, make a list and treat it like a stream """
    the_list = random.sample(range(101), 100)

    print(the_list)
    kept = None
    for e,val  in enumerate(the_list):
        if random.randint(0, e) == e:
            kept = val
            print("Maybe ", val)
    print("*** Keeping ", kept)


if __name__ == "__main__":
    main()
