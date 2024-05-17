from dining import get_menu, make_api_request

class DiningHall:
    def __init__(self, dining_hall, date, response_data):
        self.dining_hall = dining_hall;
        self.date = date;
        self.breakfast = [];
        self.lunch = [];
        self.dinner = [];
        
        self.exclusions = ["Light Rye w/ Seeds Sandwhich Loaf", "Whipped Butter", "Whipped Margarine"]
        
        self.retrieve_menu(response_data)  # Call retrieve_menu during initialization

    def retrieve_menu(self, response_data):
        if 'filterableEntries' in response_data:
            filterableEntries = response_data['filterableEntries']
            self.breakfast = get_menu(filterableEntries, self.date, "BREAKFAST", self.dining_hall)
            self.lunch = get_menu(filterableEntries, self.date, "LUNCH", self.dining_hall)
            self.dinner = get_menu(filterableEntries, self.date, "DINNER", self.dining_hall)
          
    def organize_menu(self, meals):
        # # Filter out any meals that contain any keyword from the exclusions list
        filtered_meals = [meal for meal in meals if all(exclusion.lower() not in meal.lower() for exclusion in self.exclusions)]
        organized_meals = "\n".join([f"- {meal}" for meal in meals])
        return organized_meals
    
       
    def get_meal(self, meal):
        if (meal == "Breakfast"):
            return self.organize_menu(self.breakfast);
        if (meal == "Lunch"):
            return self.organize_menu(self.lunch);
        if (meal == "Dinner"):
            return self.organize_menu(self.dinner);






    
