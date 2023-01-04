# Good luck on this morning problem!

length, tank, numberofstations, refueling = map(int,input().split())
listofStations = list(map(int,input().split()))
gasStops = 0
listofStations.reverse() # reverse the list to start from the end, or max length
distTraveled = length - tank # distTraveled for the first run will be the length of the trip subtracting the distance for
                             # tank to run out
gasStationsReached = 0  # begin at 0 gasStationsReached and 0 for gasStops
while distTraveled > 0: # loops while distance is larger than zero, it progressively gets smaller
    while gasStationsReached < numberofstations - 1 and listofStations[gasStationsReached+1] >= (distTraveled):
        gasStationsReached += 1
    distTraveled = listofStations[gasStationsReached] - tank # change distTraveled by the corresponding gasStation minus the tank size
    gasStationsReached += 1 # increment
    gasStops += 1 # increment

refuelTime = refueling*gasStops

print(refuelTime+length)
