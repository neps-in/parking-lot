# Multiple story parking system
# Number of levels  -> n
# number of parking slots per level - 5
# park(color, reg_no)
# Ashutosh Tiwari15:07
# unpark(reg_no)
# fetch_slot()
# ashutosh.tiwari@treebohotels.com
import vehicle
from vehicle import Vehicle, Car, TwoWheeler

class Spot():

    # def __init__(self , spot_type ):
    def __init__(self, level_num, spot_num):
        self.level_no = level_num
        self.spot_num = spot_num
        self.vehicle = None
        self.spot_type = ''
        print("Creating Spot...", self.level_no, self.spot_num )

    # Check if Spot is free
    def isSpotFree(self):
        return self.vehicle == None

    # Lets park the vehicle
    def park(self, vehicle):
        print('spot.park Try parking ', self.level_no, self.spot_num )

        # Park in free spaces
        if not self.vehicle:
            self.vehicle = vehicle
            print('spot.park method PARKING SUCCESS-----------------------', self.level_no, self.spot_num )
            return True

        return False
    
    def un_park(self, vehicle):
        print("checking Vehicle reg match ", vehicle )
        if self.vehicle.reg == vehicle.reg:
            print("checking Vehicle reg MATCH SUCCESS , DELETING... ", vehicle.reg )
            self.vehicle = None
            return True

        return False

    # Get the Vehicle details 
    def getVehicle(self):
        return self.vehicle

    # def add_vehicle( self, level_num, spot_num, vehicle ):
    #     self.level_num = level_num
    #     self.vehicle = vehicle 
    #     self.spot_num = spot_num

    # Str rep. of the Spot object
    def __str__(self):
        s  = "Spot.str Level" + str(self.level_no)
        s += " spot nu" + str(self.spot_num)
        if self.vehicle:
            s += " Vehicle reg " + str(self.vehicle.reg)
            s += " Vehicle color " + str(self.vehicle.color)
        else:
            s += " Vehicle is EMPTY"
        return s

class Level():

    def __init__(self, level_num, num_of_spots ):
        # self.levels = []
        self.spots = []
        self.level_num = level_num
        self.parkingspots = []  

        print("creating level.. ", level_num )

        # Add spots to the level
        for i in range(num_of_spots):
                self.parkingspots.append(Spot(level_num, i))
                # self.availableSpots.append(Slots(lane, i, type_of_vehicle))


    # Show spots in 
    # def show_spots(self):
    #     print("Show spot")
    #     for i in range(self.spots):
    #         print( i, " : " , spot(i).__str__() )

    # Try parking in this level
    def park(self, vehicle):
        print( "Level.park method try park in level ", self.level_num )
        # print( 'spots in level ')
        # print( self.parkingspots )

        for spot in self.parkingspots:
            print(" trying Spot ", spot )
            if spot.park(vehicle):
                print('Level.parking found a spot ')
                return True
            #print('level park above false')
            return False

    # Try unparking in the level
    def un_park(self, vehicle):
        print("Level.unpark Trying unpark vehicle in level number " , self.level_num )
        for spot in self.parkingspots:
            print( ' vehicle in spot ', spot.__str__() )
            if spot.getVehicle() is not None :
                print("spot.getveh is not empty")
                if vehicle.reg == spot.getVehicle().reg:
                    print('veh reg match veh.reg == spot.veh.reg UNPARKING SUCCESS' , vehicle.reg, spot.getVehicle().reg)
                    if spot.getVehicle() == vehicle:
                        return spot.un_park()
            #         return True
            # return False

    # Get Spots
    def get_spots(self):
            all_vehicles = []
            for spot in self.parkingspots:
                vehicle = spot.getVehicle()
                if (vehicle is not None) :
                    all_vehicles.append(vehicle)
                    
            print(all_vehicles)
            return all_vehicles

class Parking():

    def __init__(self, no_of_levels, no_of_spots):
        self.level = []

        # Lets add level to the parking slot
        for i in range(no_of_levels):
            print('creating levels....and attaching to parking ')
            self.level.append(Level(i, no_of_spots))

    # Try parking in the parking lot
    def park(self, vehicle):
        print("===================================================================")
        print('Parking.park Trying to park vehicle ', vehicle.reg , vehicle.color )
        for level in self.level:
            print('Parking.park method trying to park in the level ', level.level_num )
            if level.park(vehicle):
                print('parking.park success in parking')
                return True
        return False

    # Try unpark
    def un_park(self, vehicle):
        for level in self.level:
            if level.un_park(vehicle):
                return True


    # def add_level(self,level):
    #     print( "level obj " , level )
    #     self.level.append(level)

    # Show levels in parking slot
    def show_levels(self):
        print("Levels in parking lot")
        for i in self.level:
                for j in i:
                    self.level(Spot(level_num, i))
    
    # Show levels and spots - dummy function
    # def show_levels_and_its_spots(self):
    #     print("Parking Spots ")
    #     for i in self.level:
    #         print( "---Level ", i )
    #         for j in i:
    #             print( " Spots " , j )

    # # Just for testing
    # def show_parking_lots(self):
    #     all_vehicles = []
    #     for level in self.level:
    #         all_vehicles.append(self.level.get_spots())
    #     return all_vehicles


if __name__ == '__main__':

    print("Creating spots and adding to level ")
    spots_count, level_count = input("Spot Count, Level count ").split()

    spots_count = int( spots_count )
    level_count = int( level_count )

    pk = Parking( level_count , spots_count )
    
    pk.park(Car("White", 10))
    pk.park(Car("Yello", 20))
    pk.park(Car("White", 22))

    print("UNPARKING ------------------------------------------------------")
    pk.un_park(Car("",10))
    pk.un_park(Car("", 20))

