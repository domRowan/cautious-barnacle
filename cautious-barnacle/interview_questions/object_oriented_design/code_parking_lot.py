from datetime import datetime
from enum import Enum


class ParkingLot:
    def __init__(self, spaceProvider, billing):
        self.spaceProvider = spaceProvider
        self.sessionToSpaceMap = {}
        self.billing = billing

    def addVehicle(self, vehicle):
        try:
            space = self.spaceProvider.getSpace(vehicle)
        except:
            print("unable to allocate space")
        session = Session()

        self.billing.addSession(session)
        self.sessionToSpaceMap[session] = space

        return session

    def removeVehicle(self, session):
        space = self.sessionToSpaceMap[session]
        self.spaceProvider.deallocateSpace(space)
        session.setDuration()

        return space.vehicle


class Billing:
    def __init__(self):
        self.unfilfilledSessions = {}

    def addSession(self, session):
        self.unfilfilledSessions[session.id] = session

    def fulfillSssion(self, sessionId):
        del(self.unfilfilledSessions[sessionId])

    def isSessionFulfilled(self, sessionId):
        return sessionId in self.unfilfilledSessions


class SpaceProvider:
    def __init__(self):
        self.smallSpaces = []
        self.mediumSpaces = []
        self.largeSpaces = []

    def getSpace(self, vehicle):
        if self.canAllocateSmallSpace(vehicle):
            return self.smallSpaces.pop()
        elif self.canAllocateMediumSpace(vehicle):
            return self.mediumSpaces.pop()
        elif self.canAllocateLargeSpace(vehicle):
            return self.largeSpaces.pop()
        else:
            raise RuntimeError

    def canAllocateSmallSpace(self, vehicle):
        return len(self.smallSpaces) > 0 and vehicle.size == Size.small

    def canAllocateMediumSpace(self, parameter_list):
        raise NotImplementedError

    def canAllocateLargeSpace(self, parameter_list):
        raise NotImplementedError

    def deallocateSpace(self, space):
        if space.size == Size.small:
            self.smallSpaces.append(space)
        elif space.size == Size.medium:
            self.mediumSpaces.append(space)
        elif space.size == Size.large:
            self.largeSpaces.append(space)


class Size(Enum):
    small = 1
    medium = 2
    large = 3


class Space:
    def __init__(self, size):
        self.id = ""  # generate unique ID
        self.size = size
        self.vehicle = None


class Vehicle:
    def __init__(self, size, id):
        self.size = None
        self.id = id


class Car(Vehicle):
    def __init__(self, id):
        self.size = Size.medium
        self.id = id


class Motorbike(Vehicle):
    def __init__(self, id):
        self.size = Size.small
        self.id = id


class Customer:
    def __init__(self):
        self.sessions = []


class Session:
    def __init__(self):
        self.id = ""  # Get unique session ID
        self.startTime = datetime.now()
        self.duration = 0

    def getDuration(self):
        return datetime.now - self.startTime

    def setDuration(self):
        self.duration = datetime.now - self.startTime
