import time

print("Welcome to the Traffic Light Control System!")
time.sleep(2)
while True:
    print("Red Light is ON. Please wait...")
    pedestrian_signal = input("Is there a pedestrian waiting to cross? (yes/no): ")
    if pedestrian_signal.lower() == "yes":
        print("Pedestrian signal is ON. Please wait for the pedestrian to cross.")
        time.sleep(10)
        print("Pedestrian has crossed. You can go now!")
    else:
        time.sleep(5)
    print("Green Light is ON. You can go now!")
    time.sleep(5)
    print("Yellow Light is ON. Please slow down and prepare to stop.")
    time.sleep(5)