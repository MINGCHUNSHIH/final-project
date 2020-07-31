def eat(p):
    p['weight'] += 1


def exercise(p):
    p['weight'] -= 1


def speak(p):
    print('%s, weight: %d' % (p['name'], p['weight']))

def eat_2(p):
    p['weight'] += 2


def exercise_2(p):
    p['weight'] -= 2


def speak_2(p):
    print('%s, weight: %d' % (p['name'], p['weight']))

def eat_3(p):
    p['weight'] += 3


def exercise_3(p):
    p['weight'] -= 3


def speak_3(p):
    print('%s, weight: %d' % (p['name'], p['weight']))
if __name__ == '__main__':
    person_1 = {'name': 'Kevin',
              'weight': 50}
    person_2 = {'name': 'Kevi',
              'weight': 50}
    person_3= {'name': 'Kev',
              'weight': 50}
    speak(person_1)
    eat(person_1)
    speak(person_1)
    exercise(person_1)
    speak(person_1)
    
    speak_2(person_2)
    eat_2(person_2)
    speak_2(person_2)
    exercise_2(person_2)
    speak_2(person_2)
    
    speak_3(person_3)
    eat_3(person_3)
    speak_3(person_3)
    exercise_3(person_3)
    speak_3(person_3)
    
    
    
