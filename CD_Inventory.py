#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# TFang, 2021-Dec-04, added code to create a CD inventory program using OOP
#------------------------------------------#

# -- DATA -- #
menuChoice = ''
strFileName = 'cdInventory.txt'
lstOfCDObjects = []
cd_id = ''
cd_title = ''
cd_artist = ''

class CD:
    """Stores data about a CD:

    Properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    Methods:
        __str__(self): replace standard class/address identifier with string 

    """
    
    # -- Fields -- #
    cd_id = ''
    cd_title = ''
    cd_artist = ''
    # -- Constructor -- #
    def __init__(self, cdID, titl, art):
        # -- Attributes -- #
        self.cd_id = cdID
        self.cd_title = titl
        self.cd_artist = art
    # -- Properties -- #
    @property
    def cd_id(self):
        return self.__cd_id
    
    @cd_id.setter
    def cd_id(self, value):
        if str(value).isnumeric():
            self.__cd_id = int(value)
        else:
            raise Exception('That\'s not a number.')
    
    @property
    def cd_title(self):
        return self.__cd_title
    
    @cd_title.setter
    def cd_title(self, value):
        if str(value).isnumeric():
            raise Exception('That\'s not a string.')
        else:
            self.__cd_title = value
    
    @property
    def cd_artist(self):
        return self.__cd_artist
    
    @cd_artist.setter
    def cd_artist(self, value):
        if str(value).isnumeric():
            raise Exception('That\'s not a string.')
        else:
            self.__cd_artist = value
    
    #-- Methods -- #
    def __str__(self):
        value = '{}\t\t{}\t\t\t{}'.format(self.__cd_id, self.__cd_title, self.__cd_artist)
        return value

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    Properties:
        file_name (string): name of file used to load CD objects
        lst_Inventory (list of objects): 2D list of objects

    Methods:
        load_inventory(file_name): -> (a list of CD objects)
        save_inventory(file_name, lst_Inventory): -> None

    """
    def load_inventory(file_name, table):
        table.clear()
        try:
            objFile = open(file_name, 'r')
            for row in objFile:
                lstRow = row.strip().split(',')
                cdInventory = [lstRow[0], lstRow[1], lstRow[2]]
                table.append(cdInventory)
            objFile.close()
        except FileNotFoundError:
            print('\nFile not found. Proceeding to Menu:')
        except EOFError:
            print('\nFile is empty. Proceeding to Menu:')


    def save_inventory(file_name, table):
        try:
            objFile = open(file_name, 'w')
            strInventory = ''
            for row in table:
                for item in row:
                    strInventory += str(item) + ','
                strInventory = strInventory[:-1] + '\n'
            objFile.write(strInventory)
            objFile.close()
        except AttributeError:
            print('\nNo data. Proceeding to Menu:')

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Input / Output"""

    @staticmethod
    def show_menu():
        """Displays menu options to user
        Properties:
            None.

        Methods:
            None.
            
        """
        print('\nMenu Options:\n\n[L] Load Inventory from File\n[A] Add CD')
        print('[I] Show Current Inventory\n[S] Save Inventory to File\n[X] Exit')

    @staticmethod
    def menu_input():
        """Receives user input

        Properties:
            None.

        Methods:
            Returns choice (lower case string type): User input of menu options
            
        """
        choice = ''
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Please enter a menu option: ').lower().strip()
        print()
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory to user
        
        Properties:
            table: 2D list of objects entered by user

        Methods:
            None.
            
        """
        print('~~~~~ Current Inventory ~~~~~')
        print('CD ID\tCD Title\t\t\t\tCD Artist\n')
        for row in table:
            print(row)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    @staticmethod
    def cd_input(cd_id, cd_title, cd_artist):
        """Receives user input for CD data

        Properties:
            cd_id (string): CD identifier
            cd_title (string): Name of CD title
            cd_artist (string): Name of CD artist

        Methods:
            None.
            
        """
        print('Please enter your CD information:\n')
        cd_id = input('CD ID: ').strip()
        cd_title = input('CD Title: ').strip()
        cd_artist = input('CD Artist: ').strip()
        return cd_id, cd_title, cd_artist

# -- Main Body of Script -- #
FileIO.load_inventory(strFileName, lstOfCDObjects)  # load data from file into list of CD objects on start
while True:
    IO.show_menu()  # Display menu to user
    menuChoice = IO.menu_input()
    if menuChoice == 'i':  # show user current inventory
        IO.show_inventory(lstOfCDObjects)
        continue
    elif menuChoice == 'a':  # let user add data
        cd_id, cd_title, cd_artist = IO.cd_input(cd_id, cd_title, cd_artist)
        newCD = CD(cd_id, cd_title, cd_artist)  # creates instance of CD object and assigns return value to variable
        cdlst = (newCD.cd_id, newCD.cd_title, newCD.cd_artist)
        lstOfCDObjects.append(cdlst)  # appends variable to list of CD objects
        print(lstOfCDObjects)  # print statement to check objects in list
        print()
        IO.show_inventory(lstOfCDObjects)
        continue
    elif menuChoice == 's':  # let user save inventory to file
        FileIO.save_inventory(strFileName, lstOfCDObjects)
    elif menuChoice == 'l':  # let user load inventory from file
        FileIO.load_inventory(strFileName, lstOfCDObjects)
    elif menuChoice == 'x':  # let user exit program
        break