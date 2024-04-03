import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Read the comments from the CSV file
comments_df = pd.read_csv('comments.csv')

# Define the thresholds for each emotion category
anger_threshold = -0.4
trust_threshold = 0.4
surprise_threshold = 0.2
sadness_threshold = -0.2
joy_threshold = 0.2
fear_threshold = -0.1
disgust_threshold = -0.3
anticipation_threshold = 0.1

# Create an empty list to store the emotion category of each comment
emotions = []

# Perform sentiment analysis on each comment and classify into emotion categories
for comment in comments_df['Comment']:
    if type(comment) != str:
        emotions.append('')
        continue
    blob = TextBlob(comment)
    sentiment = blob.sentiment.polarity
    if sentiment <= anger_threshold:
        emotions.append('Anger')
    elif sentiment >= trust_threshold:
        emotions.append('Trust')
    elif sentiment >= surprise_threshold:
        emotions.append('Surprise')
    elif sentiment <= sadness_threshold:
        emotions.append('Sadness')
    elif sentiment >= joy_threshold:
        emotions.append('Joy')
    elif sentiment <= fear_threshold:
        emotions.append('Fear')
    elif sentiment <= disgust_threshold:
        emotions.append('Disgust')
    elif sentiment >= anticipation_threshold:
        emotions.append('Anticipation')
    else:
        emotions.append('')

# Create a new dataframe with the comments and their associated emotion categories
emotion_df = pd.DataFrame({'Comment': comments_df['Comment'], 'Emotion': emotions})

# Save the dataframe as a CSV file
emotion_df.to_csv('emotion.csv', index=False)

# Generate a pie chart of the emotion categories
emotion_counts = emotion_df['Emotion'].value_counts()
labels = emotion_counts.index.tolist()
sizes = emotion_counts.values.tolist()
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'orange', 'red', 'purple', 'blue']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Emotion Categories of Comments')
plt.savefig('emotion_piechart.png')
plt.show()
