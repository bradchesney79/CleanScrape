#!/usr/bin/env python

"""
This file defines the configuration settings for CleanScraper.py;
change them according to your environment.

"""

from string import Template

ENCODING = 'utf-8'
UA = "CleanScrape/1.0 +http://github.com/dpapathanasiou/CleanScrape"

# Define where the converted pdf files will reside
OUTPUT_FOLDER = '/tmp'

# Get and install wkhtmltopdf from:
# http://wkhtmltopdf.org/
# and update this path accordingly
WKHTMLTOX_PATH  = '/usr/local/bin'

# Set the pdf output page size
PDF_PAGE_SIZE = 'Letter'

# Define the html which frames the content to be converted
# into pdf format in this string template
HTML_FRAME = Template(u"""<html><head><meta charset="utf-8"><title>$title</title></head><body>
<div style="text-align:center"><div style="margin:0 auto;width:85%;text-align:left">
$content
</div></div>
<hr>
<p style="font-size:0.8em;font-weight:lighter;font-style:italic;font-family:sans-serif;color:#808080">Source: <a href="$url">$url</a><br />
Generated by <a href="https://github.com/dpapathanasiou/CleanScrape">CleanScrape</a></p>
</body></html>""") 

