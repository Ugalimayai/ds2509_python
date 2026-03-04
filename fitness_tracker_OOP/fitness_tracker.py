# Using Object Oriented Programming to describe a Workout to create a Fitness tracker
# think about a workout, there are many activities that can be related to working out but there are some common properties across all
# A descriptive icon, the kind of workout i.r cycling, running, jogging, swimming etc., Date, Start Time, End Time, Calories, Heart Rate, Distance
# Each specific kind of workout will have its own specific properties
# e.g for swimming we can have the pace, stroke type and no. of 100yd splits, for running we can have cadence, Running Pace, Mile Splits, Elevation etc.
# The next question is how we can represent our object with data(data attributes). e.g. for a workout: start time, end time, calories
# We also have functional attributes, i.e. methods controlling how we can interact with the object
from dateutil import parser #make datetime parsing easy
from fit_helper import gpsDistance

class Workout(object):
    # we are going to be assuming that every hour of a workout burns 200 cals
    cal_per_hour = 200
    def __init__(self, start, end, calories=None):
        self.start = parser.parse(start)
        self.end = parser.parse(end)
        self.calories = calories
        self.icon = '😠'
        self.kind = 'Workout'

    #As explained and documented in the Animals class earlier, we use getters and setters to
    # hide information about our class implementation.
    def get_calories(self):
        if (self.calories == None):
            return Workout.cal_per_hour*(self.end - self.start).total_seconds()/3600
        else:
            return self.calories
    def set_calories(self, calories):
        self.calories = calories
    def get_duration(self):
        """Return the duration of the workout, as a datetime.interval object"""
        return self.end - self.start
    def get_start(self):
        return self.start
    def set_start(self, start):
        self.start = start
    def get_end(self):
        return self.end
    def set_end(self, end):
        self.end = end
    def get_kind(self):
        """Return the kind of the workout as a string"""
        return self.kind

    def __eq__(self, other):
        """Returns true if this workout is equal to another workout, false o.w."""
        # the \ breaks up the line
        return type(self) == type(other) and \
            self.start == other.start and \
            self.end == other.end and \
            self.kind == other.kind and \
            self.get_calories() == other.get_calories()
    def __str__(self):
        """Return a text-based graphical depiction of the workout"""
        width = 16
        retstr = f"|{'–' * width}|\n"
        retstr += f"|{' ' * width}|\n"
        retstr += f"| {self.icon}{' ' * (width - 3)}|\n"  # assume width of icon is 2 chars - len('🏃🏽‍♀️');  doesn't do what you'd epxect
        retstr += f"| {self.kind}{' ' * (width - len(self.kind) - 1)}|\n"
        retstr += f"|{' ' * width}|\n"
        duration_str = str(self.get_duration())
        retstr += f"| {duration_str}{' ' * (width - len(duration_str) - 1)}|\n"
        cal_str = f"{round(self.get_calories(), 1)}"
        retstr += f"| {cal_str} Calories {' ' * (width - len(cal_str) - 11)}|\n"

        retstr += f"|{' ' * width}|\n"
        retstr += f"|{'_' * width}|\n"

        return retstr


# we can find the memory locations of class methods, with its keys and values. The same method can be applied for any instances of the object and return all keys and values associated
# print(Workout.__dict__.keys())
# print(Workout.__dict__.values())

class RunWorkout(Workout):
    cals_per_km = 100
    def __init__(self, start, end, elev=0, calories= None, route_gps_points=None):
        super().__init__(start, end, calories) # when you run super() you return the superclass in this example you have Workout().__init__ ....
        self.icon = '🏃🏽‍♂️'
        self.kind = 'Running'
        self.elev = elev
        self.route_gps_points = route_gps_points

    def get_elev(self):
        return self.elev
    def set_elev(self, e):
        self.elev = e
    def get_calories(self):
        """Return the calories consumed during the workout
        Derived using 1) the GPS points if supplied, 2) calories, if supplied, or 3) an estimate of the calories based on the duration
        """
        if (self.route_gps_points != None):
            dist = 0
            lastP = self.route_gps_points[0]
            for p in self.route_gps_points[1:]:
                dist += gpsDistance(lastP, p)
                lastP = p
            return dist * RunWorkout.cals_per_km
        else:
            return super().get_calories()

    def __eq__(self, other):
        """Returns true if this workout is equal to another workout, false o.w."""
        return super().__eq__(other) and self.elev == other.elev


class SwimWorkout(Workout):
    """Subclass of workout to representing swimming"""
    # redefine class variable cal_per_hr
    cal_per_hr = 400

    def __init__(self, start, end, pace, calories=None):
        """Create a new instance of a swimming workout, where start and
        end are strings representing the start and end time of the workout,
        and pace is the pace of the workout in min/100yd, and calories
        is an optional parameter specifying the calories burned in the workout
        """
        super().__init__(start, end, calories)
        self.icon = '🏊‍'
        self.kind = 'Swimming'
        self.pace = pace

    def get_pace(self):
        """Return the pace of the workout"""
        return self.pace

    def get_calories(self):
        """Return the total calories burned in the swim workout
           using the SwimWorkout cal_per_hr class variable"""
        if (self.calories == None):
            # calc the calories based on the length of the workout and cal_per_hr
            return SwimWorkout.cal_per_hr * (self.end - self.start).total_seconds() / 3600.0
        else:
            return self.calories


# my_workout = RunWorkout("19:00", "19:30", 500)
# print(my_workout)
points = [(42.3601,-71.0589),(42.3370,-71.2092)] # (latitude,longitude) pairs
run1 = RunWorkout('9/30/2021 1:35 PM','9/30/2021 3:57 PM', 100, route_gps_points=points)
print(f'Cals with route points: {run1.get_calories():.4f}')