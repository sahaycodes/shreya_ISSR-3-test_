ISSR 3 Test – Prerequisite Task for GSoC 2025 (Human AI)
Introduction

Hi, I’m Shreya Sahay, and this repository contains my work for the ISSR 3 Test, a prerequisite task for Google Summer of Code (GSoC) 2025 – Human AI , Project - AI-Powered Behavioral Analysis for Suicide Prevention, Substance Use, and Mental Health Crisis Detection with Longitudinal Geospatial Crisis Trend Analysis. 

This project showcases my ability to extract, analyze, and visualize crisis-related discussions from social media using Natural Language Processing (NLP), sentiment analysis, and geospatial mapping.
Repository Structure

This repository includes:

📁 .idea/ – Project configuration files.
📁 .lightning_studio/ – Environment settings for the project.
📁 .vscode/ – VS Code workspace settings.
📁 nltk_data/ – Required NLTK datasets for NLP.
📄 README.md – This documentation file.
📄 crisis_heatmap.html – Interactive visualization of crisis-related trends.
📄 geotagging.ipynb – Notebook for location extraction and mapping.
📄 main.py – Main script for data processing and analysis.
📄 reddit_data_classified.csv – Classified dataset of social media posts.
📄 reddit_data_location.csv – Location-tagged dataset.
📄 reddit_data_location.json – JSON-formatted dataset for location data.
📄 reddit_scrape.py – Python script for extracting Reddit posts.
📄 risk_level_distribution.png – Visualization of crisis risk levels.
📄 sentiment.ipynb – Notebook for sentiment analysis.
📄 sentiment_distribution.png – Graph of sentiment classification.
📄 top_crisis_locations.png – Map of the highest crisis discussion regions.
What I Achieved
✅ Task 1: Social Media Data Extraction & Preprocessing

    Used the Reddit API to extract posts related to mental health distress, substance use, and suicidality.
    Applied keyword filtering (e.g., "depressed," "addiction help," "overwhelmed," "suicidal") to identify relevant discussions.
    Structured the dataset with Post ID, Timestamp, Content, and Engagement Metrics (likes, comments, shares).
    Preprocessed the text by removing stopwords, emojis, and special characters for NLP analysis.
    📌 Deliverable: A Python script for social media data extraction and preprocessing.

✅ Task 2: Sentiment & Crisis Risk Classification

    Applied VADER (for Twitter) and TextBlob for sentiment classification (Positive, Neutral, Negative).
    Used TF-IDF and Word Embeddings (BERT, Word2Vec) to detect high-risk crisis terms.
    Classified posts into three crisis risk levels:
        🔴 High-Risk: Direct crisis language (e.g., "I don’t want to be here anymore").
        🟡 Moderate Concern: Seeking help, discussing struggles (e.g., "I feel lost lately").
        🟢 Low Concern: General discussions about mental health.
    📌 Deliverable:
        A Python script that performs sentiment and risk classification.
        A visual distribution of posts categorized by sentiment and risk level.

✅ Task 3: Crisis Geolocation & Mapping

    Extracted location metadata from geotagged posts and NLP-based place recognition.
    Implemented geocoding to map place mentions (e.g., "Need help in Austin" → Austin, TX).
    Developed heatmaps to visualize crisis-related trends using Folium & Plotly.
    Identified the top 5 locations with the highest crisis-related discussions.
    📌 Deliverable:
        A Python script for geotagging and heatmap generation.
        A visualization of regional distress patterns.

Conclusion

Through this project, I demonstrated my ability to work with data-driven crisis detection using machine learning, NLP, and geospatial analysis. The insights generated from social media discussions provide valuable tools for assessing mental health risks and developing better intervention strategies.

🚀 This project is part of my preparation for contributing to GSoC 2025 – Human AI, and I am excited to build on this experience!
