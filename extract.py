# Import necessary libraries
import requests  # For making HTTP requests
import xml.etree.ElementTree as ET  # For parsing XML data

# List of sitemap URLs to fetch vessel data
sitemap_links = [
    "https://www.balticshipping.com/sitemap-vessels-4.xml",
    "https://www.balticshipping.com/sitemap-vessels-3.xml",
    "https://www.balticshipping.com/sitemap-vessels-2.xml",
    "https://www.balticshipping.com/sitemap-vessels-1.xml",
    "https://www.balticshipping.com/sitemap-vessels.xml"
]

# Initialize an empty list to store the content of fetched sitemaps
sitemaps = []

# Loop through each URL in the list of sitemaps
for url in sitemap_links:
    response = requests.get(url)  # Make an HTTP GET request to fetch the sitemap
    if response.status_code == 200:  # Check if the request was successful
        sitemaps.append(response.text)  # Append the sitemap content (as text) to the list
    else:
        print(f"Failed to fetch {url}")  # Print an error message if the request fails

# Function to extract URLs from an XML sitemap
def extract_urls_from_sitemap(xml_data):
    """
    Parses the XML data from a sitemap and extracts all URLs.

    Args:
        xml_data (str): The XML content of the sitemap.

    Returns:
        list: A list of URLs extracted from the <loc> elements.
    """
    # Define the XML namespace used in the sitemap
    namespaces = {'': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    
    # Parse the XML content and get the root element
    root = ET.fromstring(xml_data)
    
    # Find all <loc> elements and extract their text content (URLs)
    urls = [url.text for url in root.findall('.//loc', namespaces)]
    
    return urls

# Initialize an empty list to store all extracted URLs
all_urls = []

# Loop through each sitemap and extract the URLs
for sitemap in sitemaps:
    all_urls.extend(extract_urls_from_sitemap(sitemap))  # Add the extracted URLs to the list

# Write all extracted URLs to a text file
with open('urls.txt', 'w') as f:
    for url in all_urls:
        f.write(url + '\n')  # Write each URL on a new line

# Print a message indicating the number of URLs saved
print(f"Saved {len(all_urls)} URLs to 'urls.txt'")
