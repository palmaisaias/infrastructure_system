# Event Management System Enhancement

class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date
            self.participants = 0   #---addding attribute to keep track of number of participants

        def add_participant(self, participant):
              print(f'Youve added {participant} to the {self.name} event!')
              self.participants += 1
        
        def get_participant_count(self):
              print(f'There is currently a total of {self.participants} participants attending {self.name}')

        def get_info(self):
            print(f'This event is named {self.name}. Its scheduled for: {self.date} and has {self.participants} participants attending')      

first_event = Event('New Years Party', 'Jan 1, 2025')
print()
first_event.get_info()
print()
print('We want to add a few more people!\n')
first_event.add_participant('John')
first_event.add_participant('Diane')
first_event.add_participant('Calvin')
print()
first_event.get_participant_count()
print()