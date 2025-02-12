from House import *


#Cottage Class with constructor
class Cottage(House):
    def __init__(self, area_code, sq_ft, num_bedrms, num_bathrms, age_home, garage_code, tax_info, air_bnb_rent):
        self.area_code = area_code
        self.sq_ft = sq_ft
        self.num_bathrms = num_bathrms
        self.num_bedrms = num_bedrms
        self.age_home = age_home
        self.garage_code = garage_code
        self.tax_info = tax_info
        self.air_bnb_rent = air_bnb_rent
      
    def __str__(self):
        return "Cottage with " + str(self.sq_ft) + " sq ft. and airbnb rent of: " + str(self.air_bnb_rent)


# TreeHouse Class with super() constructor
class TreeHouse(House):
    def __init__(self, area_code, sq_ft, num_bedrms, num_bathrms, age_home, garage_code, tax_info, air_bnb_rent):
        super().__init__(area_code, sq_ft, num_bedrms, num_bathrms, age_home, garage_code, tax_info)
        self.air_bnb_rent = air_bnb_rent

    def __str__(self):
        return f"Cottage with {self.sq_ft} sq ft and Airbnb rent of: {self.air_bnb_rent}"


# BoatHouse Class with kwargs used in constructor
class BoatHouse(House):
    def __init__(self, **kwargs):
        self.area_code = kwargs.get("area_code")
        self.sq_ft = kwargs.get("sq_ft")
        self.num_bedrms = kwargs.get("num_bedrms")
        self.num_bathrms = kwargs.get("num_bathrms")
        self.age_home = kwargs.get("age_home")
        self.garage_code = kwargs.get("garage_code")
        self.tax_info = kwargs.get("tax_info")
        self.air_bnb_rent = kwargs.get("air_bnb_rent")

    def __str__(self):
        return f"Cottage with {self.sq_ft} sq ft and Airbnb rent of: {self.air_bnb_rent}"


# BeachHouse class with default values in constructor
class BeachHouse(House):
    def __init__(self, area_code, sq_ft, num_bedrms, num_bathrms, age_home, garage_code=None, tax_info=None, air_bnb_rent=0):
        self.area_code = area_code
        self.sq_ft = sq_ft
        self.num_bedrms = num_bedrms
        self.num_bathrms = num_bathrms
        self.age_home = age_home
        self.garage_code = garage_code
        self.tax_info = tax_info
        self.air_bnb_rent = air_bnb_rent

    def __str__(self):
        return f"Cottage with {s
fun_house = Cottage(630, 1500, 2, 3, 0, 1234, 8, 250)

print(our_house)