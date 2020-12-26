
import re
import random


echos = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

answers = [
    [r'I am (.*)',
     ["Ah perfect, where would you like to travel ?",]],

    [r'I feel (.*)',
     ["Ah perfect, where would you like to travel ?",]],
    
    [r'I want to (.*) to Paris',
     ["When would you like to {0} to Paris?",
      "Paris is a very romantic and nice place to {0}. When would you like to {0}?"]],

    [r'I want to (.*) to Berlin',
      ["When would you like to {0} to Berlin?",
      "Berlin is a beautiful place to {0}. When would you like to {0}?"]],

    [r'(.*)Paris',
     ["When would you like to travel to Paris?",
      "I think Paris is very romantic and nice place to travel. When would you like to travel?"]],

    [r'(.*)Berlin',
     ["When would you like to travel to Berlin?",
      "Berlin is a beautiful place to travel. When would you like to travel?"]],
    
   [r'(.*) to Berlin',
     ["When would you like to travel?",
      "Perfect! When would you like to visit it?"]],
   
    [r'(.*) to Paris',
     ["When would you like to travel?",
      "Perfect! When would you like to visit it?"]],


    [r'(.*) travel to (.*)',
     ["Unfortunately, you should choose between Paris and Berlin, our apologies ...",
      "We are really sorry but there are no flights to {1}.I think you should book a flight to Berlin or Paris"]],
   
    [r'(.*) fly to (.*)',
     ["Unfortunately, you should choose between Paris and Berlin, our apologies ...",
      "We are really sorry but there are no flights to {1}.I think you should book a flight to Berlin or Paris"]],

    [r'(.*) travel on (.*)\?',
     ["Unfortunately, we are fully booked on {1}",
      "I think that {1} is not available for booking",]],
    
    [r'(.*) travel on (.*)',
     ["Unfortunately, we are fully booked on {1}",
      "I think that {1} is not available for booking",
      "I believe that {1} is an amazing idea"]],

    [r'(.*) to Berlin on (.*)\?',
     ["We are sorry, but we are fully booked on {1}"]],    

     [r'(.*) to Paris on (.*)\?',
     ["We are sorry, but we are fully booked on {1}"]],    

    [r'(.*) fly on (.*)\?',
     ["Unfortunately, we are fully booked on {1}",
      "I think that {1} is not available for booking",
      "I believe that {1} is an amazing idea"]],
    
    [r'(.*) fly on (.*)',
     ["Unfortunately, we are fully booked on {1}",
      "I think that {1} is not available for booking",
      "I believe that {1} would be an amazing idea"]],

    [r'On (.*)',
     ["Unfortunately, we are fully booked on {0}",
      "I think that {0} is not available for booking",
      "I believe that {0} would be an amazing idea"]],

    [r'I (.*)',
     ["I am really sorry, but i don't get you. Would you like to travel to Paris or Berlin?"]],
    
    [r'quit',
     ["Good-bye.",
      "Thank you, have a nice day!"]],

   [r'(.*)',
     ["Please tell me about your booking.",
      "I think that it would be better if you would like to tell me more about your trip."]],

   [r'(.*)\?',
     ["Why do you ask that?",
      "Would you mind telling me about your booking?"]]
]

def reflect(fragment):
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in echos:
            tokens[i] = echos[token]
    return ' '.join(tokens)

def analyze(statement):
    for pattern, responses in answers:
        match = re.match(pattern, statement.rstrip(".!"))
        if match:
            response = random.choice(responses)
            return response.format(*[reflect(g) for g in match.groups()])

def main():
    print ("Hello. How are you feeling today? Where do you want to travel?")

    while True:
        statement = raw_input("> ")
        print analyze(statement)

        if statement == "quit":
            break

if __name__ == "__main__":
    main()

