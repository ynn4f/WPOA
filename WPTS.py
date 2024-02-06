import argparse
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_last_modified(url):
    try:
        # Fetch the webpage
        response = requests.head(url)
        last_modified_header = response.headers.get('last-modified')
        
        if last_modified_header:
            # If last-modified header is present, return its value
            return last_modified_header
        
        # If last-modified header is not present, parse the HTML to find the date
        html_content = requests.get(url).content
        soup = BeautifulSoup(html_content, 'html.parser')
        meta_tags = soup.find_all('meta', {'name': 'date'})
        
        if meta_tags:
            # If meta tag with name 'date' is found, return its content
            return meta_tags[0]['content']
        
        # If neither last-modified header nor meta tag is found, return None
        return None
    
    except Exception as e:
        print(f"Error: {e}")
        return None

def format_time(timestamp):
    if timestamp:
        # Convert timestamp to datetime object
        last_modified_datetime = datetime.strptime(timestamp, '%a, %d %b %Y %H:%M:%S %Z')
        # Format datetime object into a human-readable string
        return last_modified_datetime.strftime('%Y-%m-%d %H:%M:%S')
    else:
        return "Unknown"

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Get last modified timestamp of a webpage.')
    parser.add_argument('-s', '--url', type=str, required=True, help='URL of the webpage')
    args = parser.parse_args()
    
    # Get the last modified timestamp
    last_modified = get_last_modified(args.url)
    
    # Format the timestamp into a readable format
    formatted_time = format_time(last_modified)
    
    if formatted_time:
        print(f"The webpage was last modified on: {formatted_time}")
    else:
        print("Unable to determine the last modified timestamp.")
