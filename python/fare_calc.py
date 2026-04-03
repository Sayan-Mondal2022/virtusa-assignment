class FareCalc:
    def __init__(self):
        self.rates = {"Economy": 10, "Premium": 18, "SUV": 25}

    def calculate_fare(self, km: int, type: str, hour: int) -> int:
        # This function will get three params.
        # Then it will calculate the fare, by getting the rates based on the type of the cab.
        # Then based on the hour (If it's a PEAK hr then the fare increases by 1.5x)
        fare = 0

        return fare

    def get_ride_details(self) -> dict:
        # Ask for Type of Cab i.e, Economy, Premium, SUV?
        # Ask for the Distance
        # Ask for the Time in hrs, just the hr nothing more.
        # Then call the calculate_fare()
        # Return the Final Fare as a Receipt format, which will contain all the details

        return {}
