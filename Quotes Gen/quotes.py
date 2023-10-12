import random
Q = {
    "life_quotes":[
        "Life is about growing and improving and getting better", "Try to be a rainbow in someone else’s cloud.",
        "Sometimes, when things are falling apart, they may actually be falling into place", "Even miracles take a little time",
        "Happiness is not by chance but by choice","Positive anything is better than negative nothing", "Choose to be optimistic, it feels better",
        "Be yourself, everyone else is already taken.","Learn as if you will live forever, live like you will die tomorrow.",
        "When you change your thoughts, remember to also change your world", "The road to success and the road to failure are almost exactly the same",
        "Develop success from failures. Discouragement and failure are two of the surest stepping stones to success",
        "There are three ways to ultimate success: The first way is to be kind. The second way is to be kind. The third way is to be kind",
        "Don’t let yesterday take up too much of today","To know how much there is to know is the beginning of learning to live "
        "Each day comes bearing its gifts. Untie the ribbon", "In every day, there are 1,440 minutes. That means we have 1,440 daily opportunities to make a positive impact.",



    ],

    "gym_quotes":[
        "I hated every minute of training, but I said, ‘Don’t quit. Suffer now and live the rest of your life as a champion.-Muhammad Ali",
        "The body achieves what the mind believes","What hurts today makes you stronger tomorrow",
        "The journey to stronger muscles passes through sore muscles.","If you think lifting is dangerous, try being weak. Being weak is dangerous",
        "Workout till you feel that pain and soreness in muscles. This one is a good pain. No pain, no gain",
        "The pain you feel today will be the strength you feel tomorrow-Arnold Schwarzenegger",
        "Look in the mirror. That’s your competition","Exercise is labor without weariness",
        "If when you look in the mirror you don’t see the perfect version of yourself you better see the hardest working version of yourself.",
        "One awesome workout is not gonna give you the results you want","Making excuses burns zero calories per hour",
        "Pain is temporary. Quitting lasts forever.","Get comfortable with being uncomfortable",
        "Our bodies are gardens, our wills are our gardeners", "Be Humble. Be Hungry. And always be the hardest worker in the room",





    ],
    "study_quotes":[
        "There are no secrets to success. It results from preparation, hard work, and learning from failure.”"
        "The best way to predict your future is to create it.",
        "Hard work beats talent when talent doesn’t work hard", "Learn as if you will live forever, live like you will die tomorrow.",
        "There are no shortcuts to any place worth going.",
        "The harder I work, the more luck I seem to have.",
        "Failure is the opportunity to begin again intelligently.",
        "Do what is right, not what is easy", "It’s never too late to be what you might have been.",
        "Nobody can go back and start a new beginning, but anyone can start today and make a new ending",
        "Don’t wish it were easier. Wish you were better","To change your life, you must first change your day",
        "Nothing is impossible. The word itself says ‘I’m Possible","Success consists of going from failure to failure without loss of enthusiasm",
        "It always seems impossible until it’s done.","Don’t let what you cannot do interfere with what you can do","Don't be afraid of failure"


    ]
}

def get_moti(types):
    types_Q = Q.get(types.lower(),[])
    if types_Q:
        return random.choice(types_Q)
    else:
        return "Sorry,no motivation found GET SELF-MOTIVATED!!!"

def main():
    print("ENTER THE TYPES IN THIS FORMATE ONLY-> (life_quotes,study_quotes,gym_quotes)")
    types = input("Enter the type of quotes/motivation needed ")

    quote = get_moti(types)
    print(quote)

if __name__=="__main__":
    main()


