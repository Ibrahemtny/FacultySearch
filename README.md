# UIC Faculty Search - CS & Math Professors

A web scraping project to search for faculty members from the University of Illinois at Chicago (UIC) Computer Science and Mathematics departments. The application scrapes and collects publicly available data about faculty members including their names, titles, research interests, and contact information.

## Features
- **Web Scraping**: Collects data on professors from UIC’s Computer Science and Mathematics faculty pages.
- **Faculty Information**: Gathers details such as name, position, department, and research interests.
- **Data Storage**: The scraped data is saved in a JSON file for easy analysis and querying.

## Technologies Used
- **Python**: Main programming language used for scraping and processing data.
- **BeautifulSoup**: A Python library for parsing HTML and XML documents, used to extract professor details.
- **Requests**: Library to make HTTP requests and fetch data from UIC faculty web pages.
- **JSON**: Format for storing the scraped faculty data.
- **HTML & CSS**: Basic frontend for displaying the data (index.html & style.css).

## Files
- **main__4_.py**: Python script that performs the web scraping and stores the data in a JSON file.
- **index__2_.html**: Simple HTML page for displaying the faculty data.
- **style (1).css**: Styling for the HTML page.
- **Data (1).json**: Sample JSON file containing faculty information scraped from UIC.

## How to Run

1. Clone the repository to your local machine:
  
   git clone https://github.com/Ibrahemtny/FacultySearch.git



Copy
pip install requests beautifulsoup4
Run the Python script to start the web scraping process:


Copy
python main__4_.py
After the script runs, the scraped data will be stored in a JSON file (Data (1).json) for easy analysis.

Open the index__2_.html file in your browser to view the faculty data.


