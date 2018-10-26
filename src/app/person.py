import random
import os, uuid, sys
from azure.storage.blob import BlockBlobService, PublicAccess

class Person(object):
    """ Person Class. Simulates a stranded
    person in a calamity.
    """
    def __init__(self, area_height, area_width):
        self.id = None # unique identifier
        self.image = None
        self.displacement_x = random.randint(1,6) # constant
        self.displacement_y = random.randint(1,6) # constant
        # self.range_of_motion = random.randint(50,70) # random
        self.range_of_motion = area_width # random
        self.area_height = area_height
        self.area_width = area_width # random
        self.x_coordinate = random.randint(0,area_width+1) # random
        self.y_coordinate = random.randint(0,area_height+1)# random
        self.center_of_motion = (self.x_coordinate, self.y_coordinate) # initial position
        self.wifi_range = random.randint(100, 150) # random
        self.cell_connectivity = False # boolean value true for only some people
        self.connected_people = [] # the people whose wifi range has been discovered.
                                     # has dictionary with the person and the time-stamp
                                     # of last seen/ last updated.
        self.ismessage = False
        self.message = None
        self.chat = []

        self.initialize_blob()

    def initialize_blob(self):
        """
        Initialization for Azure blob storage
        """
        self.block_blob_service = BlockBlobService(account_name='blueticks', account_key='key')
        self.container_name = 'peopledata'
        # Probably not needed
        # self.block_blob_service.create_container(self.container_name)
        # self.block_blob_service.set_container_acl(self.container_name, public_access=PublicAccess.Container)


    def move(self):
        """ Move within the defined range
        within the stranded region. Use 2D
        random walk.
        """
        x = random.randint(0,5)
        y = random.randint(0,5)
        if x == 0:
            if 0 <= self.x_coordinate + self.displacement_x <= self.area_width:
                self.x_coordinate += self.displacement_x
            else:
                pass
        elif x == 1:
            if 0 <= self.x_coordinate - self.displacement_x <= self.area_width:
                self.x_coordinate -= self.displacement_x
            else:
                pass
        else:
            pass
        if y == 0:
            if 0 <= self.y_coordinate + self.displacement_y <= self.area_height:
                self.y_coordinate += self.displacement_y
            else:
                pass
        elif y == 1:
            if 0 <= self.y_coordinate - self.displacement_y <= self.area_height:
                self.y_coordinate -= self.displacement_y
            else:
                pass
        else:
            pass

        # if random.randint(0,2) == 0:
        #     if self.center_of_motion[0] - self.range_of_motion <= self.x_coordinate + self.displacement_x <= self.center_of_motion[0] + self.range_of_motion:
        #         self.x_coordinate += self.displacement_x
        #     else:
        #         pass
        # else:
        #     if self.center_of_motion[0] - self.range_of_motion <= self.x_coordinate - self.displacement_x <= self.center_of_motion[0] + self.range_of_motion:
        #         self.x_coordinate -= self.displacement_x
        #     else:
        #         pass
        # if random.randint(0,2) == 0:
        #     if self.center_of_motion[1] - self.range_of_motion <= self.y_coordinate + self.displacement_y <= self.center_of_motion[1] + self.range_of_motion:
        #         self.y_coordinate += self.displacement_y
        #     else:
        #         pass
        # else:
        #     if self.center_of_motion[1] - self.range_of_motion <= self.y_coordinate - self.displacement_y <= self.center_of_motion[1] + self.range_of_motion:
        #         self.y_coordinate -= self.displacement_y
        #     else:
        #         pass

    def detect_signal(self, personB):
        """ Checks if a personA has detected the wifi
        signal of personB. Return the personB's position
        and any relevant data, incase the scan is successful.
        """
        if personB.x_coordinate <= self.x_coordinate <= personB.x_coordinate + personB.wifi_range:
            if personB.y_coordinate <= self.y_coordinate <= personB.y_coordinate + personB.wifi_range:
                self.connect(personB)
                return True
        return False
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
        if self.ismessage:
            for person in self.connected_people:
                person.receive_message(self.id, self.message)
            pass
            self.ismessage = False

    def receive_message(self,identifier,message):
        """ Receive messages from any of the mobile device
        from the cluster and save it in the chat history
        """
        self.chat.append(
            {
                'id':identifier,
                'message':message
            }
        )
        pass

    def connect_server(self):
        """ If there is any internet connectivity
        of the person's phone, all the data is
        posted to the server and informed to the
        nearest relief camp
        """
        filename=str(self.id)
        path_to_file=os.path.expanduser("~/Documents")
        fullpath = os.path.join(path_to_file, filename)

        pobject = open(fullpath, "w")
        if self.cell_connectivity:
            print("DATA POSTED TO THE SERVER FOR : ")
            for people in self.connected_people:
                print(str(people.id)+":"+str(people.x_coordinate)+","+str(people.y_coordinate))
                pobject.write(str(people.id)+":"+str(people.x_coordinate)+","+str(people.y_coordinate))

        # Disabled because access keys are not supposed to be public
        # self.block_blob_service.create_blob_from_path(self.container_name, filename, fullpath)
