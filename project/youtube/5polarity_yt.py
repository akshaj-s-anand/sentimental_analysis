import csv
import matplotlib.pyplot as plt
from textblob import TextBlob

# Load comments from CSV file
comments = []
with open('comments.csv', 'r', encoding='utf-8') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        comments.append(row[0])

# Perform sentiment analysis on each comment and write to a new CSV file
positive_count, negative_count, neutral_count = 0, 0, 0
with open('sentiments.csv', 'w', newline='', encoding='utf-8') as f:
    csv_writer = csv.writer(f)
    for comment in comments:
        blob = TextBlob(comment)
        sentiment = blob.sentiment.polarity
        if sentiment > 0:
            csv_writer.writerow([comment, 'Positive'])
            positive_count += 1
        elif sentiment < 0:
            csv_writer.writerow([comment, 'Negative'])
            negative_count += 1
        else:
            csv_writer.writerow([comment, 'Neutral'])
            neutral_count += 1

# Create a pie chart
labels = ['Positive', 'Negative', 'Neutral']
sizes = [positive_count, negative_count, neutral_count]
colors = ['green', 'red', 'gray']
plt.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')

# Save the pie chart to the new CSV file
plt.savefig('sentiments_piechart.png', bbox_inches='tight')
with open('sentiments.csv', 'a', newline='', encoding='utf-8') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['Sentiment Analysis Results'])
    csv_writer.writerow(['Positive', positive_count])
    csv_writer.writerow(['Negative', negative_count])
    csv_writer.writerow(['Neutral', neutral_count])
    csv_writer.writerow([''])
    csv_writer.writerow(['Sentiment Analysis Pie Chart'])
    csv_writer.writerow(['', '', 'sentiments_piechart.png'])
