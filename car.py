class Car(object):
    """"The Car class boiler plate
    """

    def __init__(self, name='General', model='GM', car_type='saloon'):
        self.name = name
        self.model = model
        self.car_type = car_type
        self.num_of_doors = 4
        self.num_of_wheels = 4
        self.speed = 0
        self.motion_speed = 0

        #The car shoud have four (4) doors except its a Porshe or Koenigsegg
        if (self.name == 'Porshe') or (self.name == 'Koenigsegg'):
            self.num_of_doors = 2

        #The car shoud have four (4) wheels except its a type of trailer
        if self.car_type == 'trailer':
            self.num_of_wheels = 8



    def drive(self, motion_speed):
        #Return the speed of a moving car
        pass


    def is_saloon(self):
        #The car type should be saloon if it is not a trailer
        if self.car_type != 'trailer':
            return True
        return False
        pass
