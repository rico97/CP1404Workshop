from car import Car

def main():
    bus = Car("Bus", 180)
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print(bus)

main()

def golimo():
    limo = Car("Limo",100)
    limo.add_fuel(20)
    print("Current fuel is {}".format(limo.fuel))
    limo.drive(115)
    print("Odo is {}".format(limo.odometer))
    print(limo)

golimo()