import ics
import datetime
from xml.etree.ElementTree import Element, SubElement, tostring

# Load the ICS file
with open('calendar.ics', 'r') as f:
    calendar = ics.Calendar(f.read())

# Create an RSS feed XML structure
rss = Element("rss", version="2.0")
channel = SubElement(rss, "channel")

title = SubElement(channel, "title")
title.text = "Calendar Events"

description = SubElement(channel, "description")
description.text = "Upcoming events from the calendar."

for event in calendar.events:
    item = SubElement(channel, "item")

    event_title = SubElement(item, "title")
    event_title.text = event.name

    event_description = SubElement(item, "description")
    event_description.text = event.description

    event_date = SubElement(item, "pubDate")
    event_date.text = event.begin.format("ddd, DD MMM YYYY HH:mm:ss ZZ")

# Convert the XML structure to a string
rss_feed_str = tostring(rss, encoding="utf-8").decode("utf-8")

# Write the RSS feed to a file
with open('rss_feed.xml', 'w') as rss_file:
    rss_file.write(rss_feed_str)

print("RSS feed generated successfully.")
