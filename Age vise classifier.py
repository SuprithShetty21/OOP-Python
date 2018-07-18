class Person:
    age = 0     # Initialize age to zero. This variable will be used throughout the class.
    
    def __init__(self,initialAge):
        # Checking for negative values of age
        self.initialAge = initialAge
        if(self.initialAge < 0):
            print('Age is not valid, setting age to 0.')
            self.initialAge = 0
        Person.age = self.initialAge    #saving the age value in a global variable

    def age_classifier(self):
        # Check whether a person is a kid, teenager or an adult
        if(Person.age < 13):
            print('You are young.')
        elif(Person.age >= 13 and Person.age <= 19):
            print('You are a teenager.')
        else:
            print('You are an adult.')

    def ageIncrementer(self):
        # Increment the age of the person in here
        Person.age = Person.age + 1
        
# Enter the no of values of age you need to evaluate
# enter the values of age one after 
# for example
# 5
# -3
# 7
# 23
# 18
# 10

t = int(input())
for i in range(0, t):
    age = int(input())         
    per = Person(age)  
    per.age_classifier()
    for j in range(0, 5):       # increments the age by five, so this loop gives the age after five years.
        per.ageIncrementer()       
    per.age_classifier()
    print("")
