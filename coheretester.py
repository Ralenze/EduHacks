import cohere 
from cohere.classify import Example 
import sys

def classifysentence(sent):
    co = cohere.Client('redacted') 
    ins = []
    ins.append(sent)
    response = co.classify( 
    model='large', 
    # inputs=["Confirm your email address", "hey i need u to send some $"], 
    inputs = ins,
    examples=[Example("Dermatologists don\'t like her!", "not good"), Example("Hello, open to this?", "good"), Example("I need help please wire me $1000 right now", "not good"), Example("Hot new investment, don’t miss this!", "not good"), Example("Nice to know you ;)", "good"), Example("Please help me?", "good"), Example("Your parcel will be delivered today", "not good"), Example("Review changes to our Terms and Conditions", "good"), Example("Weekly sync notes", "good"), Example("Re: Follow up from today’s meeting", "good"), Example("Pre-read for tomorrow", "good"), Example("I am forcing", "not good"), Example("tell me your address", "not good"), Example("please let me know of a good address", "good"), Example("scroll down", "not good"), Example("I noticed", "not good"), Example("I have observed", "good"), Example("Regards", "good"), Example("sincerely", "good"), Example("thanks,", "not good"), Example("Can you", "not good"), Example("Is it possible", "good")]) 
    print ("the input sentence is " + sent)
    print('The confidence levels of the labels are: {}'.format(response.classifications)) 
    


##test main

sent = ""

for i in range(1, len(sys.argv)):
    sent = sent + sys.argv[i] + " "

print (sent)

classifysentence(sent)
