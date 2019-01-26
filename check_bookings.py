# imports the os and sys module
import os
import sys
# imports the pandas module
import pandas as pd


class CheckBookings:
    """CheckBookings class


    Attributes:
        filepath: path to the file that contains the room booking data to be checked 
                  for potential booking conflicts.
    """

    def __init__(self, filepath):
        """ constructor initialises the CheckBookings class """
        self.filepath = filepath

    # check_bookings method that checks the bookings made to identify if any conflict with each other
    def check_bookings(self):
        """ check_bookings class method """

        # error handling
        try:

            # if the file size is greater than zero (not empty)
            if os.path.getsize(self.filepath) > 0:

                # reads in the csv and creates pandas dataframe
                room_data = pd.read_csv(self.filepath)

                # empty conflicts list
                conflicts = []

                # conflicts_present boolean flag set tentitively as False
                conflicts_present = False

                # for loop that iterates through each row in the room_data dataframe
                for i in range(len(room_data)):

                    # nested for loop
                    for j in range(i + 1, len(room_data)):

                        """
                        meeting 1 start time = 9am
                        meeting 1 end time = 11am

                        meeting 2 start time = 10am
                        meeting 2 end time = 1pm

                        if meeting 1 starts before meeting 2 ends and 
                        meeting 1 ends before meeting 2 starts then a booking 
                        conflict has occurred
                        """
                        if (room_data['Start_Time'].iloc[i] < room_data['End_Time'].iloc[j] and
                                room_data['End_Time'].iloc[i] > room_data['Start_Time'].iloc[j]):

                            # conflicts detected so flag set as True
                            conflicts_present = True

                            # appends the details of the booking conflicts to the conflicts list
                            conflicts.append(('Booking conflict detected between request',
                                              room_data['Request_ID'].iloc[i], 'and request', room_data['Request_ID'].iloc[j]))

                # if the conflicts_present flag is true, return the contents of the conflicts list
                if conflicts_present:
                    return conflicts

                # else return that no conflicts have been detected
                else:
                    return 'No booking conflicts detected in file'

            # else the file is empty
            else:
                #
                return 'File provided is empty'

        except IOError:
            return 'File could not be read'

    # End check_bookings


#
if __name__ == '__main__':

    check = CheckBookings(sys.argv[1])
    print(check.check_bookings())
    
