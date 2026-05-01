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


#2.# Fake News Detector

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
