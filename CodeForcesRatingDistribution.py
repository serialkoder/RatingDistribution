# Script to generate a histogram of Codeforces rating distribution

import json
import urllib.request

import matplotlib.pyplot as plt


def getRatingWiseCount():
    r = urllib.request.urlopen("http://codeforces.com/api/user.ratedList?activeOnly=true").read()
    y = json.loads(r)
    x = y["result"]
    rating = []
    for i in x:
        rating.append(i['rating'])
    return rating


print("Generating histogram")
rating = getRatingWiseCount()
print(len(rating))
# generate histogram of rating in intervals of 100 with different colors.
plt.hist(rating, bins=range(0, 4000, 100), color='green', edgecolor='black', linewidth=1.2)
# Add labels to the plot x axes for every 100 interval
plt.xticks(range(0, 4000, 200))
plt.title("Codeforces Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of users")
plt.show()
