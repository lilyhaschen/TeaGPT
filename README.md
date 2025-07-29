# TeaGPT: Terminal Edition 

A cozy terminal companion that gently asks how you're feeling, recommends a tea to match your mood, and—if you'd like—tells a sweet little story while your tea steeps. Inspired by the warmth of a kind older woman who always knows just what to say.

---

## Features
- Sentiment-aware mood detection using Hugging Face Transformers
- Personalized tea recommendations for positive, neutral, or negative moods
- Over 35 lovingly described teas
- Optional storytime with soothing anecdotes from TeaGPT’s "life"
- Warm, conversational dialogue throughout

---

## Requirements
Python 3.7+ and the following packages:

```bash
pip install transformers torch
```

---

## Usage

1. Clone or download this repo
2. Run the script:

```bash
python main.py
```

3. When prompted, tell TeaGPT how you're feeling 
4. Receive a tea suggestion and a kind message 
5. Choose whether you'd like to hear a story 
6. Get a parting blessing to enjoy your tea 

---

##  Example Output
```
Welcome, dear heart. How are you feeling today?
> I'm feeling a little lost and tired.

Ah, sweet one. Based on what you’ve shared, I’ve steeped this just for you:
☕ Tea: Lemon Balm
"Let the lemon balm hold you like I would — gently, and without hurry."

Would you like to hear a little story while we wait for your tea to steep? (yes/no): yes

"Did I ever tell you about the time I spilled oolong on a love letter? He still wrote back anyway."

Your tea is ready, my dear. May it bring you warmth and a moment of peace. 🍃
```

## 📝 License
MIT License
