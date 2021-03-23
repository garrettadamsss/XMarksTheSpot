
# Entry is an object that holds information about each
# attraction/image


class Entry:
    def __init__(self, name, location, image, description, latitude, longitude):
        self.name = name
        # maybe like city name
        self.location = location
        self.image = image
        self.description = description
        # maybe needed to display on google map
        self.coordinate = (latitude, longitude)