import time
import threading

spots =["taken", "available", "taken", "available", "taken"]
print("Welcome to the Smart Parking System!")
time.sleep(2)
print("Current parking status:")
print("Spot 1: " + spots[0])
print("Spot 2: " + spots[1])
print("Spot 3: " + spots[2])
print("Spot 4: " + spots[3])
print("Spot 5: " + spots[4])
def cars_arriving():
    while True:
        print("A car wants to park. Checking for available spots...")
        time.sleep(2)
        if spots[0] == "available":
            print("Spot 1 is available. Parking the car...")
            spots[0] = "taken"
        elif spots[1] == "available":
            print("Spot 2 is available. Parking the car...")
            spots[1] = "taken"
        elif spots[2] == "available":
            print("Spot 3 is available. Parking the car...")
            spots[2] = "taken"
        elif spots[3] == "available":
            print("Spot 4 is available. Parking the car...")
            spots[3] = "taken"
        elif spots[4] == "available":
            print("Spot 5 is available. Parking the car...")
            spots[4] = "taken"
        else:
            print("No available spots. The car cannot park.")
        print("Current parking status:")
        print("Spot 1: " + spots[0])
        print("Spot 2: " + spots[1])
        print("Spot 3: " + spots[2])
        print("Spot 4: " + spots[3])
        print("Spot 5: " + spots[4])
        time.sleep(15)
        
def cars_leaving():
    while True:
        time.sleep(20)
        print("A car is leaving. Freeing up a spot...")
        if spots[0] == "taken":
            print("Spot 1 is taken. Freeing up the spot...")
            spots[0] = "available"
        elif spots[1] == "taken":
            print("Spot 2 is taken. Freeing up the spot...")
            spots[1] = "available"
        elif spots[2] == "taken":
            print("Spot 3 is taken. Freeing up the spot...")
            spots[2] = "available"
        elif spots[3] == "taken":
            print("Spot 4 is taken. Freeing up the spot...")
            spots[3] = "available"
        elif spots[4] == "taken":
            print("Spot 5 is taken. Freeing up the spot...")
            spots[4] = "available"
        print("Current parking status:")
        print("Spot 1: " + spots[0])
        print("Spot 2: " + spots[1])
        print("Spot 3: " + spots[2])
        print("Spot 4: " + spots[3])
        print("Spot 5: " + spots[4])

parking_thread = threading.Thread(target=cars_arriving)
leaving_thread = threading.Thread(target=cars_leaving)
parking_thread.start()
leaving_thread.start()
   
   
