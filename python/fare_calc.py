class FareCalc:
    def __init__(self):
        self.rates = {"Economy": 10, "Premium": 18, "SUV": 25}

    def calculate_fare(self, km: int, type: str, hour: int) -> int:
        # This function will get three params.
        # Then it will calculate the fare, by getting the rates based on the type of the cab.
        # Then based on the hour (If it's a PEAK hr then the fare increases by 1.5x)
        fare = self.rates[type]

        return fare

    def get_ride_details(self) -> dict:
        # Ask for Type of Cab i.e, Economy, Premium, SUV?
        # Ask for the Distance
        # Ask for the Time in hrs, just the hr nothing more.
        # Then call the calculate_fare()
        # Return the Final Fare as a Receipt format, which will contain all the details
        cab_types = {1: "Economy", 2: "Premium", 3: "SUV"}

        distance = input("Enter the distance (in km): ")

        # The Cab Choice must come under the TRY BLOCK
        cab_choice = int(
            input(
                """Choose the Cab Type:\n1 -> Economy\n2 -> Premium\n3 -> SUV\nENter your choice: """
            )
        )
        # This might throw a KeyError
        cab_type = cab_types[cab_choice]

        # The HR input also must come under the try block
        # Might be other than a int.
        hr = int(input("Enter the time: "))

        fare = self.calculate_fare(distance, cab_type, hr)

        return {}


obj = FareCalc()
obj.get_ride_details()
