class House:
    def __init__(self, area_code, sq_ft, num_bedrms, num_bathrms, age_home, garage_code, tax_info, has_safe):
        self.area_code = area_code
        self.sq_ft = sq_ft
        self.num_bathrms = num_bathrms
        self.num_bedrms = num_bedrms
        self.age_home = age_home
        self.tax_info = tax_info
        self.__garage_code = garage_code
        self.__has_safe = has_safe
        
    def __str__(self):
        return "House with " + str(self.sq_ft) + " sq ft."

    def get_garage_code(self):
        return self.__garage_code

    def set_garage_code(self, garage_code):
        self.__garage_code = garage_code


our_house = House(435, 3000, 3, 5, 0, 1234, 7, True)

print(our_house.get_garage_code())
print(our_house.__garage_code)


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


fun_house = Cottage(630, 1500, 2, 3, 0, 1234, 8, 250)

print(fun_house)

print(our_house)
print(fun_house.sq_ft, fun_house.air_bnb_rent)
