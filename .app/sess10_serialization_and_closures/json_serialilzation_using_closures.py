# Python script that uses closures to serialize and deserialize a Student object to and fro a JSON file

# import the required modules
import json
import os
from datetime import date, datetime

# Define a student class
class Student:
    """
     A class to represent a student.

     Attributes:
         reg_no (str): The student's registration number.
         name (str): The student's full name.
         birthdate (date): The student's birthdate as a `datetime.date` object.
         gender (str): The student's binary gender.

     Methods:
         to_dict(): Converts the student instance into a dictionary for serialisation.
         from_dict(data): Creates a Student instance from a dictionary (typically after deserialisation).
     """
    # constructor
    def __init__(self, reg_no, name, birthdate, gender):
        """
             Constructs all the necessary attributes for the Student object.

             Args:
                 reg_no (str): Registration number.
                 name (str): Full name of the student.
                 birthdate (date): Birthdate of the student.
                 gender (str): Gender of the student.
        """
        self.reg_no = reg_no
        self.name = name
        self.birthdate = birthdate
        self.gender = gender

    # instance method to convert the student object to a dictionary
    def to_dict(self):
        """
          Serialises the student object to a dictionary format suitable for JSON conversion.

          Returns:
              dict: Dictionary with student's data including ISO-formatted birthdate.
        """
        return {

            'reg_no': self.reg_no,
            'name': self.name,
            'birthdate': self.birthdate.isoformat(),
            'gender': self.gender,

        }

    # Static method to deserialize a dictionary back to a student obj
    @staticmethod
    def from_dict(data):
        """
        Deserialises a dictionary to create a Student object.

        Args:
            data (dict): A dictionary containing student information.

        Returns:
            Student: A new instance of the Student class.
        """
        return (Student(
            reg_no=data['reg_no'],
            name=data['name'],
            birthdate=datetime.strptime(data['birthdate'], '%Y-%m-%d').date(),
            gender=data['gender'],
        ))

# closures
def student_json_handler(file_path):
    def serialise(student):
        """
        Serialises a Student object and writes it to a JSON file.

        Args:
            student (Student): The Student instance to serialise.
        """
        with open(file_path, 'w') as f:
            json.dump(student.to_dict(), f)
        print(f"Student details serialized to JSON successfully in the file:\n{file_path}")

    def deserialise():
        with open(file_path, 'r') as f:
            data = json.load(f)
            student = Student.from_dict(data)
            print(f"Deserialized student details successfully from the file:\n{file_path}")
            return student
    return serialise, deserialise

if __name__ == '__main__':
    #Example to create a Student object, save, then load it using the above closures
    student = Student("DS2509_S8", "Mycicle Bikler", date(2000,7,12), 'Male')
    file_path = os.path.abspath(os.path.join(os.getcwd(), '..', 'files', 'students.json'))
    os.makedirs(os.path.dirname(file_path), exist_ok=True) # ensure the above directory is created to avoid errors
    serialise, deserialise = student_json_handler(file_path)
    serialise(student) # save the student details to the json file
    loaded_student = deserialise() # read in the student details from the json file

    # Display the loaded student details
    print(f"Loaded student details:\n{loaded_student.name}, {loaded_student.reg_no}, {loaded_student.birthdate},{loaded_student.gender}")

