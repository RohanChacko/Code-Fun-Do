import random

class Person(object):
    """ Person Class. Simulates a stranded
    person in a calamity. 
    """
    def __init__(self, area_height, area_width):
        self.id = None # unique identifier
        self.x_coordinate = random.randint(0,area_width+1) # random
        self.y_coordinate = random.randint(0,area_height+1)# random
        self.center_of_motion = (self.x_coordinate, self.y_coordinate) # initial position
        self.displacement_x = random.randint(1,6) # constant
        self.displacement_y = random.randint(1,6) # constant
        self.range_of_motion = random.randint(50,200) # random
        self.wifi_range = random.randint(15,30) # random
        self.cell_connectivity = None # boolean value true for only some people
        self.connected_people = [] # the people whose wifi range has been discovered.
                                     # has dictionary with the person and the time-stamp 
                                     # of last seen/ last updated.
        self.message = None

    def move(self):
        """ Move within the defined range
        within the stranded region. Use 2D
        random walk.
        """
        if random.randint(0,2) == 0:
            if self.center_of_motion[0] - self.range_of_motion <= self.x_coordinate + self.displacement_x <= self.center_of_motion[0] + self.range_of_motion:
                self.x_coordinate += self.displacement_x
            else:
                pass
        else:
            if self.center_of_motion[0] - self.range_of_motion <= self.x_coordinate - self.displacement_x <= self.center_of_motion[0] + self.range_of_motion:
                self.x_coordinate -= self.displacement_x
            else:
                pass
        if random.randint(0,2) == 0:
            if self.center_of_motion[1] - self.range_of_motion <= self.y_coordinate + self.displacement_y <= self.center_of_motion[1] + self.range_of_motion:
                self.y_coordinate += self.displacement_y
            else:
                pass
        else:
            if self.center_of_motion[1] - self.range_of_motion <= self.y_coordinate - self.displacement_y <= self.center_of_motion[1] + self.range_of_motion:
                self.y_coordinate -= self.displacement_y
            else:
                pass

    def detect_signal(self, personB):
        """ Checks if a personA has detected the wifi 
        signal of personB. Return the personB's position 
        and any relevant data, incase the scan is successful.
        """
        if personB.x_coordinate <= self.x_coordinate <= personB.x_coordinate + personB.wifi_range:
            if personB.y_coordinate <= self.y_coordinate <= personB.y_coordinate + personB.wifi_range:
                self.connect(personB)
        pass

    def connect(self, personB):
        """ If the signal is detected, then connect 
        with the person and exchange the location 
        coordinates. In case already in the connected
        list then update the timestamp and location.
        """
        if personB in self.connected_people:
            self.connected_people.remove(personB) #insert time stamp aswell
            self.connected_people.append(personB)
        else:
            self.connected_people.append(personB)
        pass

    def send_message(self):
        """ If there is any message by the person,
        it is sent to all the people connected in the cluster
        """
        pass

    def connect_server(self):
        """ If there is any internet connectivity
        of the person's phone, all the data is
        posted to the server and informed to the 
        nearest relief camp
        """
        pass
        