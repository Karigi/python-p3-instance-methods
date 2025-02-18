#!/usr/bin/env python3

class Person:
    # Class body goes here

    #Instance method definition
    def talk(self):
        print("Hello World!")
        return "Hello World!"
    
    def walk(self):
        print("The person is walking.")
        return "The person is walking."
    
patty = Person()
patty.talk()
patty.walk()
