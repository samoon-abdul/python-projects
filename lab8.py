from random import randint
from typing import List

class Bacteria:

    def __init__(self, dividechance :int, maxlife :int, dayslived :int):
        self.dividechance = dividechance
        self.maxlife = maxlife
        self.lifespan = randint(1, self.maxlife)
        self.dayslived = dayslived

    def live_a_day(self):
        x = randint(1, 100)
        self.dayslived = self.dayslived + 1
        if x < self.dividechance:
            newbacteria = Bacteria(self.dividechance, self.maxlife, 0)
            return newbacteria
        else:
            return None

    def isalive(self):
        if self.dayslived <= self.lifespan:
            return True
        else:
            return False


class Colony:
    def __init__(self, seed :List[int]):
        self.seed = seed

    def live_a_day(self, x :int):
        # self.seed
        dead = []
        alive = []
        special_list = []
        for i in self.seed:
            lol = i.live_a_day()
            if lol is None:
                if not i.isalive():
                    dead.append(i)
                    self.seed.remove(i)
            elif lol is not None:
                self.seed.append(lol)
                alive.append(i)
                if not i.isalive():
                    dead.append(i)
                    self.seed.remove(i)
        special_list.append(len(dead))
        print(f"Day {x} Colony Size {len(self.seed)} New Members: {len(alive)} Expired Members: {len(dead)} ")
        return len(dead)

    def print_colony_status(self, x :int, y :int):
        print(f"Colony report at DAY: {x}")
        print(f"Current colony population: {len(self.seed)}")
        print(f"Total number of bacteria: {len(self.seed) + y}")
        print(f"Total number dead: {y}")
        total_bacteria = len(self.seed) + y
        return int(total_bacteria)


def replay():
    global enabler
    prompt = input("\nTry another experiment? Saying no will close the program (Y/N): ")
    if (prompt.upper() == "Y"):
        enabler = True
    else:
        enabler = False


def main():
    global enabler
    global biglist
    biglist = []
    enabler = True
    while (enabler) is True:
        starterlist = []
        dead_counter = []
        days = int(input("Max num of days to grow: "))
        starting = int(input("Number of starting bacteria: "))
        divide_chance = int(input("% chance of daily division [1-100]: "))
        Max_life = int(input("Maximum lifespan for a bacteria (1 or greater): "))
        starting_bacteria = Bacteria(divide_chance, Max_life, 0)
        for x in range(1, starting + 1):
            starterlist.append(starting_bacteria)
        colonycreate = Colony(starterlist)
        for x in range(1, days + 1):
            dayliver = colonycreate.live_a_day(x)
            dead_counter.append(dayliver)
            if len(colonycreate.seed) > 40000 or len(colonycreate.seed) == 0:
                break
        dead_total = sum(dead_counter)
        print("\nExperiment Stopped")
        printer = colonycreate.print_colony_status(x, dead_total)
        biglist.append(printer)
        print(f"Total number of bacteria objects created so far: {sum(biglist)}")
        replay()


if __name__ == "__main__":
    main()
