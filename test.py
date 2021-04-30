import unittest
from parking import Parking, Spot, Level
from vehicle import Car, TwoWheeler

class TestParkingLot(unittest.TestCase):

    def test_park(self):
        parkingLotObj = Parking(2, 3)
        res1 = parkingLotObj.park(Car("White", 10))
        res2 = parkingLotObj.park(Car("Red", 20))
        res3 = parkingLotObj.park(Car("Yellow", 830))
        # res4 = parkingLotObj.park(Car("Orange", 430))
        # res5 = parkingLotObj.park(Car("Green", 130))
        # res6 = parkingLotObj.park(Car("TEal", 302))
        # res7 = parkingLotObj.park(Car("Turqois", 301))

        self.assertEqual(res1, True)
        self.assertEqual(res2, True)
        self.assertEqual(res3, True)
        # self.assertEqual(res4, True)
        # self.assertEqual(res5, True)
        # self.assertEqual(res6, True)
        #self.assertEqual(res7, True)


    def test_unpark(self):
        parkingLotObj = Parking(2, 3)

        res1 = parkingLotObj.un_park(Car("", 10))
        # res2 = parkingLotObj.un_park(Car("", "10"))
        # res3 = parkingLotObj.un_park(Car("", "10"))

        self.assertEqual(res1, False)
        # self.assertEqual(res2, True)
        # self.assertEqual(res3, True)


        
    # def test_all(self):
    #     parkingLotObj = ParkingLot(3, 10)
    #     # Atleast 1 parking spot for car.
    #     # First park a car, it should return True.
    #     self.assertTrue(parkingLotObj.parkVehicle(Car(10, "Google")))
    #     # Get the list of cars, it should give one car we parked.
    #     self.assertEqual(parkingLotObj.companyParked("Google"), [Car(10, "Google")])
    #     # Remove that car successfully.
    #     self.assertTrue(parkingLotObj.leaveOperation(Car(10, "Google")))
    #     # Now the list of cars should be empty.
    #     self.assertEqual(parkingLotObj.companyParked("Google"), [])


if __name__ == '__main__':
    unittest.main()