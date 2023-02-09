from os import name


class person_wife:  
    name1 = 'harshit'
    name2 = 'Ahmad'
    def __init__(self, name):
        self.name1 = name
    def fathername(self):
        print('my father name i', self.name2)
    def say_hi(self, husband):
        print('say hi to ' + husband + 's wife '+ self.name1)

person = person_wife('Ritu')
person.say_hi('sajal')
        