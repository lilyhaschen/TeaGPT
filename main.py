'''!pip install transformers torch
'''
# TeaGPT - AI Mood Tea Recommender (Terminal Version)

from transformers import pipeline
import random
import time

# Load sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

# Tea database by emotional tone
tea_by_mood = {
    "POSITIVE": [
        ("Chamomile", "Oh darling, you're glowing. Chamomile will gently hold your joy like warm sunlight in a cup."),
        ("Green Tea", "You're beaming, sweetie! A cup of green tea will carry that brightness with grace."),
        ("Jasmine", "The world blooms with you today. Jasmine tea will wrap you in fragrant celebration."),
        ("Elderflower", "You're radiant, love. Elderflower brings out the sparkle behind your smile."),
        ("Hibiscus", "You're alive with color. Hibiscus brings out your brightness with every sip."),
        ("Rose Tea", "Sweetheart, rose tea mirrors your warmth and grace—it's like sipping a compliment."),
        ("Peach Oolong", "Joyful and juicy—peach oolong is like laughter in a teacup."),
        ("Strawberry Green", "Bright and fruity, just like your energy today, dear."),
        ("Orange Blossom", "Citrusy and fragrant—let’s toast to this sunshine of yours."),
        ("Lemongrass", "Fresh and zesty, like your laughter echoing through a garden."),
        ("Ginger Peach", "Darling, your joy deserves something juicy and warm."),
        ("Mint Tulsi", "You shine with light—mint tulsi will mirror your inner spark."),
    ],
    "NEGATIVE": [
        ("Peppermint", "There, there dear. Let peppermint clear the fog and refresh your spirit."),
        ("Lemon Balm", "Come sit down, my love. Lemon balm will soothe your storm gently."),
        ("Lavender", "You’re safe here. Lavender will wrap your heart in calm and hold space for your tears."),
        ("Licorice Root", "Sweetheart, let something soft and sweet remind you you’re still whole."),
        ("Ginger", "When it aches, ginger brings a little fire back—kind and healing."),
        ("Turmeric Chai", "Let this golden blend warm your weariness like a soft blanket."),
        ("Ashwagandha Brew", "Gentle soul, breathe deep—this one is for quiet courage."),
        ("Fennel & Cinnamon", "A gentle warmth to ease your belly and your heart."),
        ("Holy Basil", "Earthy and wise, just like the comfort you need."),
        ("Valerian Root", "To quiet restless feelings, valerian offers deep calm."),
        ("Mullein Tea", "Soothing for a chest heavy with emotion."),
        ("Chaga Mushroom", "For strength, resilience, and quiet grounding."),
    ],
    "NEUTRAL": [
        ("Oolong", "A quiet day, hm? Oolong is steady and warm—like a hand resting gently on yours."),
        ("White Tea", "Stillness can be lovely. Let white tea carry you inward, one sip at a time."),
        ("Rooibos", "Let’s share a moment of peace. Rooibos is earthy and kind, like good company."),
        ("Genmaicha", "For thoughtful hearts and quiet moments, Genmaicha hums a gentle lullaby."),
        ("Darjeeling", "For minds in motion, Darjeeling offers clarity and calm."),
        ("Yerba Mate", "Gentle focus for a drifting mind—mate will keep you grounded."),
        ("Chai Spice", "Balance and spice in every sip—perfect for a thoughtful afternoon."),
        ("Spearmint & Nettle", "Clean and clear, like a breeze in early spring."),
        ("Ceylon", "A classic warmth for steady days."),
        ("Honeybush", "Subtle and naturally sweet—good for gentle reflection."),
        ("Cornflower Herbal", "Mellow and soft, with a whisper of blue skies."),
        ("Blueberry Rooibos", "For slow afternoons and quiet thoughts.")
    ]
}

# Stories from grandma TeaGPT
stories = [
    "Oh, back in the war, tea was all we had to keep warm. I remember steeping chamomile with just rainwater and a smile.",
    "My dear old cat, Mister Whiskers, used to nap beside the kettle. I swear he knew when the tea was ready.",
    "Once, I fell in love over a shared cup of jasmine tea. He had the kindest eyes, and smelled like cinnamon.",
    "There was a storm once so loud it rattled the kettle off the stove! But my lemon balm didn’t spill a drop.",
    "I used to host a little book club every Thursday. We’d sip rooibos and argue gently about Austen. Heaven, really.",
    "The first time I ever tasted mint tea, I was barefoot in Morocco. I still dream about that breeze.",
    "Oh, my kettle and I have been through it all—breakups, blackouts, and burnt toast. She still whistles sweetly for me.",
    "Did I ever tell you about the time I spilled oolong on a love letter? He still wrote back anyway.",
    "I kept my grandmother’s teacups in a glass cabinet. Sometimes I talk to them when the house is quiet.",
    "A boy once brought me hibiscus flowers after a spelling bee. I was twelve. I’ve loved the tea ever since.",
    "When I was younger, I’d sneak into the garden with a thermos of chai and a radio. Felt like magic.",
    "There’s something about steeping tea in silence, just listening to the leaves unfold. It’s how I found peace after she passed.",
    "Oh, I once taught a parrot to say 'Tea time!' every day at 4. Startled every guest. I miss that rascal.",
    "The first time I traveled alone, I packed four pairs of socks and twenty tea bags. One must have priorities.",
    "There was a winter so cold, the pipes froze—but the kettle still worked. We huddled and sipped ginger tea all night.",
    "I used to sing to my teapot while waiting. Don’t laugh—it always brewed better when I did.",
    "We had one radio channel growing up. They played violin concertos during tea hour. I still can’t hear one without tasting bergamot.",
    "My sister and I would have ‘pretend royal teas’ with lace curtains and lemonade in teacups. Still feels like nobility to me.",
    "You know, tea bags weren’t always a thing. We used to bundle herbs in handkerchiefs. That was my first invention, I suppose."
]

def classify_mood(text):
    result = classifier(text)[0]
    label = result['label'].upper()
    if "POSITIVE" in label:
        return "POSITIVE"
    elif "NEGATIVE" in label:
        return "NEGATIVE"
    else:
        return "NEUTRAL"

def recommend_tea(mood):
    return random.choice(tea_by_mood[mood])

def tell_story():
    print("\nLet me share something sweet while your tea steeps...")
    time.sleep(2)
    print(f"{random.choice(stories)}\n")
    print("Now then, enjoy your tea, sweetheart. You deserve this moment.")

def main():
    print("\n✨ TeaGPT — Hello, love. I'm so glad you stopped by. ✨\n")
    while True:
        print("Would you like a warm cup of tea for your soul?")
        user_input = input("Tell me how you're feeling, dear:")
        mood = classify_mood(user_input)

        satisfied = False
        while not satisfied:
            tea, message = recommend_tea(mood)
            print(f"\n☕ Tea: {tea}\n{message}\n")
            response = input("Does that sound just right for you, love? (yes/no)").strip().lower()
            if response.startswith("y"):
                satisfied = True
                hear_story = input("Would you like to hear a little story while it steeps? (yes/no)").strip().lower()
                if hear_story.startswith("y"):
                    tell_story()
                else:
                    print("Alright, sweetheart. Enjoy your tea. I’m here whenever you need me. 🌼\n")
            else:
                print("Let's try another, my dear.")

        again = input("Would you like another cup, love? (yes/no)").strip().lower()
        if not again.startswith("y"):
            print("Take care now, sugar. I'll be here with the kettle warm.")
            break

if __name__ == "__main__":
    main()
