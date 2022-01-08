'''
Show a quote depending on what the person is feeling! 

Details:
- 1 player 

Rules:
- player will input their mood
- depending on the mood, quotes relating to their mood will pop up 

'''
#1) import necessary modules

import random 


#2) create dictionary consisting of moods and quotes

quotes_dict = {
'sad': ['There are moments when I wish I could roll back the clock and take all the sadness away, but I have the feeling that if I did, the joy would be gone as well.', 'Life\'s under no obligation to give us what we expect.','Don\'t go around saying the world owes you a living. The world owes you nothing. It was here first.', 'Things change. And friends leave. And life doesn\'t stop for anybody.', 'Being a successful person is not necessarily defined by what you have achieved, but by what you have overcome.', 'Trying to avoid sadness is trying to avoid life.', 'What brings us to tears, will lead us to grace. Our pain is never wasted.', 'What brings us to tears, will lead us to grace. Our pain is never wasted.', 'Ninety-nine percent of your problems are created by you because you take life seriously.', 'Turn your wounds into wisdom.'],
'giving up': ['Behind every successful mean or woman there are many unsuccessful years.', 'When it is all finished you will see it was never random. In the meantime, have faith that all is happening for a reason. Look for the lesson, the gift, the bridge you are to take to get yourself where you need to be.', 'Every time you thought you couldn’t keep moving forward, you did. Take a moment to appreciate your strength.', 'You have to fight through some bad days to get to the best days of your life', 'I did not come this far only to come this far.', 'Shout out to everyone who’s trying to get their life together. Working on yourself is the hardest part of life. Keep going. It gets easier.', 'Your mission: Turn your take of woe into tales of wow. Turn your tales of fury info tales of glory.', 'When everything seems to be going against you, remember that the airplane takes off against the wind, not with it.', 'Nobody can go back and start a new beginning, but anyone can start today and make a new ending.', 'The past is your lesson. And the present is your gift. The future is your motivation.'],
'happy' : ['Happiness is not the absence of problems, it’s the ability to deal with them.', 'The greatest happiness of life is the conviction that we are loved; loved for ourselves, or rather, loved in spite of ourselves.', 'A great obstacle to happiness is to expect too much happiness.', 'The secret of happiness is freedom, the secret of freedom is courage.', 'It is not how much we have, but how much we enjoy, that makes happiness.', 'Nobody really cares if you’re miserable, so you might as well be happy.', 'Happiness is not something ready made. It comes from your own actions.', 'Happiness is being content with what you have, living in freedom and liberty, having a good family life and good friends.', 'The world is full of people looking for spectacular happiness while they snub contentment.', 'Happiness grows at our own firesides, and is not to be picked in strangers’ gardens.'  ]

} 

# print(len(quotes_dict['sad']))
# print(len(quotes_dict['giving up']))
# print(len(quotes_dict['happy']))

#3) create user input
# your_mood = input("Enter mood - sad/giving up/happy")
mood = input("How are you feeling? sad/giving up/happy?")
def mood_quote_bot(mood):
    mood = mood.lower()
    quote_index = random.randint(0, len(quotes_dict[mood]) - 1)
    quotes = quotes_dict[mood]
    quote = quotes[quote_index] 
    return quote

# mood = input("How are you feeling? sad/giving up/happy?")
# result = mood_quote_bot(mood)
print(mood_quote_bot(mood))



