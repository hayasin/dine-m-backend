from dining import get_menu, make_api_request

class Account:
    def __init__(self, date, meal, dining_hall):
        self.date= date;
        self.meal = meal;
        self.dining_hall = dining_hall
    def retrieve_menu(self, response_data):
        if 'filterableEntries' in response_data:
            filterableEntries = response_data['filterableEntries']
            menu = get_menu(filterableEntries, self.date, self.meal, self.dining_hall)
            print("Menu for", self.meal, "at", self.dining_hall, "on", self.date, ":", menu)





    
    
    #DINING HALL< STORES BRAWKFAST< LUNCH <DINNER 
    #TAKE MESSAGING SYSTEM AND MAKE IT SO THAT YOU ONLY HAVE TO CALL ONE FUNCTION TO MAKE MESSAGE
    
    




    
    