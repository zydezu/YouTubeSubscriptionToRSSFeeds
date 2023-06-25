import time

rssFeeds = []
baseLink = "https://www.youtube.com/feeds/videos.xml?channel_id="

#read supplied subscriptions.csv file
with open('subscriptions.csv', 'r', encoding="utf8") as f:
    subscriptions = f.readlines()

#loop through all csv values
for i in range(len(subscriptions)):
    if i>0 and len(subscriptions[i])>5: #avoid first line and blank lines 
        channelID = subscriptions[i].split(',')[0]
        rssFeeds.append(baseLink + channelID + '\n') #\n is for the file output
        print(baseLink + channelID)

#write file
with open('rssfeeds.txt', 'w', encoding="utf8") as f:
    f.writelines(rssFeeds)

print("Written feeds to rssfeeds.txt\nDone!")
time.sleep(1)