#1. Simple Smart Resume Keyword Matcher

resume = """
Python, Machine Learning, Data Analysis, Pandas, NumPy, SQL
"""

job_description = """
Looking for candidate with Python, Machine Learning, Deep Learning,
SQL, Data Visualization, Communication Skills
"""

stopwords = {"and", "or", "with", "for", "the", "a", "an", "to"}
def extract_keywords(text):
    words = text.lower().replace(",", "").split()
    keywords = [word for word in words if word not in stopwords]
    return set(keywords)

resume_keywords = extract_keywords(resume)
job_keywords = extract_keywords(job_description)
matched_keywords = resume_keywords.intersection(job_keywords)
match_percentage = (len(matched_keywords) / len(job_keywords)) * 100
missing_skills = job_keywords - resume_keywords
print("Resume Keywords:", resume_keywords)
print("Job Keywords:", job_keywords)
print("\nMatched Keywords:", matched_keywords)
print("Match Percentage: {:.2f}%".format(match_percentage))

print("\nMissing Skills:", missing_skills)


#2.Fake News Detector

clickbait_words = [
    "shocking", "you won't believe"]
def check_fake_news(headline):
    headline_lower = headline.lower()
    
    for word in clickbait_words:
        if word in headline_lower:
            return "Suspicious"
    
    return "Looks Normal"
headline = input("Enter news headline: ")
result = check_fake_news(headline)
print("Result:", result)

#3.Notification System

import datetime
def send_notification(message):
    print(" Notification:", message)
current_hour = datetime.datetime.now().hour
user_active = True     
priority = "high"     
if priority == "high":
    send_notification("High priority alert!")
elif user_active:
    send_notification("User is active - sending normal notification")
elif current_hour >= 9 and current_hour <= 21:
    send_notification("Daytime reminder")
else:
    print("⏸️ No notification (night time)")

#4. Smart Attendance System

students = [
    ("Arun", "08:55"),
    ("Bala", "09:03"),
    ("priya", "09:07"),
    ("David", "08:59")
]
limit_time = "09:05"
for name, time in students:
    if time <= limit_time:
        print(name, "- Present")
    else:
        print(name, "- Absent")

#5.E Commerce Discount Engine

price = float(input("Enter product price: ₹"))
if price > 5000:
    discount = 0.20
elif price >= 2000:
    discount = 0.10
else:
    discount = 0
final_price = price - (price * discount)
print("Final price after discount: ₹", final_price)

#6.Chat Message Analyser

messages = [
    "Hi 😊",
    "How are you?",
    "I am fine 😄",
    "What about you?",
    "Great 👍"
]
total = len(messages)
questions = 0
emojis = 0
for msg in messages:
    if "?" in msg:
        questions += 1
for char in msg:
        if char in "😊😄👍😂😍":
            emojis += 1
print("Total messages:", total)
print("Questions:", questions)
print("Emojis:", emojis)
