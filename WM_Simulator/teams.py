

class Teams: 

    def __init__(self, rating, name, shortname):
        self.__rating = rating
        self.__name = name
        self.__shortname = shortname
        self.__wins = 0

    def get_rating(self):
        return self.__rating

    
    def set_rating(self, rating):
        self.__rating = rating

 
    def get_name(self):
        return self.__name



    def get_shortname(self):
        return self.__shortname

    def get_wins(self):
        return self.__wins

    def set_wins(self, wins):
        self.__wins = wins


    def printdata(self):
        print(f'{self.__name} has a rating of {self.__rating}')
