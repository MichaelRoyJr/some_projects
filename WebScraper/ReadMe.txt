Description
    This project is a web scraper taht pulls baseball statistics from a newspaper's web site and 
    displays them in the console.  Specifically, the author's favorite team, the Chicago Cubs, are 
    used and the stats are pulled from HTML on the website of the Detroit Free Press.

    This is written in Python and multiple libraries are used to accomplish this  task easily.  
    These include requests, to facilitate easy http requests, BeautifulSoup, for parsing html, 
    and PrettyTable, to display results neatly.

    The majority of effort consisted of studying the code of the web page to navigate to the 
    correct page and the pertinent information.  

Highlights
    -http requests, in this case 'GET'
    -website analysis
    -data scraping

How To Run
    The .py file is intended to run in a console window, and output will display there.  A number 
    of dependencies must be present.  requests should be included with most python installations.  
    Both BeautifulSoup and Prettytablemust be installed, if not previously done.  The following 
    commands should accomplish this:  
        pip install bs4
        pip install prettytable
 