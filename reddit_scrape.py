import praw
import pandas as pd
import re
import json
import time
import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from geopy.geocoders import Nominatim
from geotext import GeoText

# Download NLTK data
nltk.download('stopwords')
nltk.download('punkt')

# Load SpaCy NLP Model for Named Entity Recognition (NER)
print("🔄 Loading SpaCy NLP Model...")
nlp = spacy.load("en_core_web_sm")
print("✅ SpaCy Model Loaded!")

# Reddit API credentials
REDDIT_CLIENT_ID = "Iy13An6NK5db56fqkuFWEg"
REDDIT_CLIENT_SECRET = "wC2GTtHKEJcNr0CvTG5H2K_r-s-Fiw"
REDDIT_USER_AGENT = "script_test v1.0 by /u/OldDevelopment8085"

# Authenticate with Reddit API
print("🔄 Authenticating with Reddit API...")
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)
print("✅ Reddit Authentication Successful!")

# Keywords for mental health & crisis detection
keywords = [
    "depressed", "addiction help", "overwhelmed", "suicidal", "mental health",
    "therapy", "self-harm", "anxiety", "stress", "burnout",
    "substance abuse", "panic attack", "alcohol addiction", "drug abuse", "crisis support"
]

# Targeted subreddits
subreddits = ["depression", "mentalhealth", "Anxiety", "SuicideWatch", "stopdrinking", "addiction"]

# Increase dataset size to 5,000 posts
total_posts = 8000
posts_per_keyword = total_posts // len(keywords)

# Initialize geocoder
geolocator = Nominatim(user_agent="geo_locator", timeout=10)

# Function to clean text
def clean_text(text):
    text = re.sub(r'http\S+|www\S+', '', text)  # Remove URLs
    text = re.sub(r'[^A-Za-z0-9 ]+', '', text)  # Remove special characters & emojis
    words = word_tokenize(text.lower())  # Tokenize & convert to lowercase
    words = [word for word in words if word not in stopwords.words('english')]  # Remove stopwords
    return " ".join(words)

# Function to extract location using multiple methods
def extract_location(text):
    if pd.isna(text) or not isinstance(text, str):
        return None  # Ensure valid input

    # Method 1: Named Entity Recognition (NER) using SpaCy
    doc = nlp(text)
    ner_locations = [ent.text for ent in doc.ents if ent.label_ in ["GPE", "LOC"]]  # Extract locations
    if ner_locations:
        return ner_locations[0]  # Return the first detected location

    # Method 2: Regex-based location extraction
    location_match = re.search(r"(live in|from|located in|born in) ([A-Za-z\s]+)", text, re.IGNORECASE)
    if location_match:
        return location_match.group(2).strip()  # Extract location from sentence

    # Method 3: GeoText (City Name Recognition)
    places = GeoText(text).cities
    if places:
        return places[0]  # Return first city found

    return None  # Return None if no location is found

# Function to get latitude & longitude of a location
def get_lat_lon(location):
    if pd.isna(location) or not isinstance(location, str):  # Ensure valid input
        return None, None
    try:
        geo = geolocator.geocode(location, timeout=10)
        if geo:
            return geo.latitude, geo.longitude
    except Exception as e:
        print(f"⚠ Geocoding failed for '{location}': {e}")
    return None, None  # Always return two values

# Extract Reddit posts with improved location handling
def extract_reddit_posts():
    data = []
    total_extracted = 0  # Counter to track progress
    print("🔄 Starting Reddit data extraction...\n")

    for keyword in keywords:
        for subreddit in subreddits:
            print(f"🔍 Searching for '{keyword}' in r/{subreddit}...")

            try:
                for submission in reddit.subreddit(subreddit).search(keyword, limit=posts_per_keyword):
                    cleaned_text = clean_text(submission.title + " " + submission.selftext)
                    location = extract_location(submission.title + " " + submission.selftext)  # Extract location
                    lat, lon = get_lat_lon(location) if location else (None, None)  # Get lat/lon

                    data.append({
                        "post_id": submission.id,
                        "timestamp": submission.created_utc,
                        "subreddit": subreddit,
                        "keyword": keyword,
                        "content": cleaned_text,
                        "upvotes": submission.score,
                        "comments": submission.num_comments,
                        "location": location,
                        "latitude": lat,
                        "longitude": lon
                    })

                    total_extracted += 1  # Increment counter
                    if total_extracted % 100 == 0:  # Print progress every 100 posts
                        print(f"✅ Extracted {total_extracted} posts so far...")

                time.sleep(1)  # Avoid API rate limit
            except Exception as e:
                print(f"❌ Error fetching data from r/{subreddit} for '{keyword}': {e}")

    print(f"\n✅ Reddit data extraction complete! Total posts extracted: {total_extracted}")
    return data

# Run extraction and save data
reddit_data = extract_reddit_posts()

# Save as JSON
print("\n💾 Writing data to JSON file...")
with open("reddit_data_location.json", "w") as f:
    json.dump(reddit_data, f, indent=4)
print("✅ JSON file saved: reddit_data_location.json")

# Save as CSV
print("\n💾 Writing data to CSV file...")
df = pd.DataFrame(reddit_data)
df.to_csv("reddit_data_location.csv", index=False)
print("✅ CSV file saved: reddit_data_location.csv")

print("\n🎉 Reddit data extraction with location details **COMPLETE!** 🚀")
