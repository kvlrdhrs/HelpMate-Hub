class Member:
    def __init__(self, name, email, phone, city):
        self.name = name
        self.email = email
        self.phone = phone
        self.city = city


class Volunteer(Member):
    def __init__(self, name, email, phone, city, gender, birth_year, info):
        super().__init__(name, email, phone, city)
        self.gender = gender
        self.birth_year = birth_year
        self.info = info


class VolunteerSeeker(Member):
    def __init__(self, name, email, phone, city, background_info, tasks):
        super().__init__(name, email, phone, city)
        self.background_info = background_info
        self.tasks = tasks

volunteer_1 = Volunteer('David', 'davidsmits@aol.nl', '053-3849149', 'Rehovot', 'Male', 1978, "I like to work with children or with disadvantaged groups")
print(volunteer_1.name)
print(volunteer_1.email)
print(volunteer_1.phone)
print(volunteer_1.city)
print(volunteer_1.gender)
print(volunteer_1.birth_year)
print(volunteer_1.info)

volunteer_seeker_1 = VolunteerSeeker('Service Civil International', 'help@workcamps.sci.ngo', '+32 26490738', 'Antwerp', 'Organises international voluntary workcamps in order to promote a culture of peace', 'Organising a summercamp for children of refugees')
print(volunteer_seeker_1.name)
print(volunteer_seeker_1.email)
print(volunteer_seeker_1.phone)
print(volunteer_seeker_1.city)
print(volunteer_seeker_1.background_info)
print(volunteer_seeker_1.tasks)