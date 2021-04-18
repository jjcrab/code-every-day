# https: // www.codewars.com/kata/5981a139f5471fd1b2000071/python

def task(w, n, c):
    workers = ["James", "John", "Robert", "Michael", "William"]
    if w == 'Monday':
        name = workers[0]
    elif w == 'Tuesday':
        name = workers[1]
    elif w == 'Wednesday':
        name = workers[2]
    elif w == 'Thursday':
        name = workers[3]
    elif w == 'Friday':
        name = workers[4]
    return f'It is {w} today, {name}, you have to work, you must spray {n} trees and you need {n*c} dollars to buy liquid'
