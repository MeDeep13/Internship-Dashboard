 # END-TO-END DATA-PIPELINE FOR INTERNSHIP INSIGHTS

### Overview 📌

This Project is an end-to-end data analytics solution built using Python, NLP(NLTK), BeautifulSoup, Power BI, and Task Scheduler for automation. It scrapes over 6,500 live internship listings from more than 140 pages, cleans and processes the data, automates daily refreshes, and visualizes internship trends across India's various locations using an interactive Power BI dashboard.

### Why did I build it? 🤔

* It is mainly built for students who are looking for internships by **role** and **location**, and **compare** the **Stipend** offered as per different roles and locations.
* It helps find an estimate of the average stipend offered and understand what a **Competitive Stipend** should look like.
* It can also help recruiters/companies to decide the stipend as per the market trends.

## Tech Stack 🛠️

* **Python** - Data scraping, preprocessing, and automation
* **BeautifulSoup** - Web scrapping internship listings
* **NLP(NLTK)** - Used NLTK to extract data
* **Pandas** - Data manipulation and cleaning
* **Power BI** - Interactive dashboard and analytics
* **Window Task Scheduler** - Automating data scraping and cleaning on log in once per day at a 15-minute delay.
  
## Data scraping part 📄
* I scraped over 140 pages and a total of around 6500 internships, with headers and a random sleep of 1 or 2 seconds between each iteration to not extract data recklessly
* The data I scraped included 1) role, 2) location, 3) duration, 4) stipend, 5) time posted, 6) skills, 7) number of applicants
* I used a nested for loop for data collection ( because I need to access each of the internships' links to access the required skills and number of applicants
  
## Data Cleaning part 🧹
* Data cleaning was done along with EDA
* Many internships have more than one location, so I exploded the locations and broke one row into many with 1 location each.
* Created new columns of skill_match using NLP's NLTK library
* Major data cleaning included- removing duplicates, standardization, many roles fell into the same category, but had different names, so unification of names was also done.
* Converting the data types of columns
* The range of stipend was converted into the average stipend.
## NLP
* Parsed skills from the resume and found % match of the candidate for each of the roles.
* 
* I included the NLP part in the Data Cleaning script itself.
  
## Power BI part 📊
*
## Automation part 🤖

# A few example insights
* Most of the Technical Internships are WFH.
* Most of the **Talent acquisition** and **Recruitment** roles are on-site.
* **Architecture** and **Event Management** roles beat WFH over on-site roles.
* **Delhi** has more **SEO** roles than **Mumbai**
* **Mumbai** beats WFH in **Consultant** roles
* 75% **Subject Matter Expert** internships are 3 months long
* 72% of **Volunteering** roles are 1 month long
* **Gurgoan** has most on-site **Game Dev** roles
* 3 and 6-month internships are most common(around 38% each) followed by 2 months of internship

## Future Improvements 🔮
* ~~Resume parsing + skill gap analysis~~ ✅
* Use of advanced libraries like Spacy in place of NLTK
* NLP-based role clustering 
* ~~Internship recommender system~~ ✅

## Contributions 🤝
 Feel free to fork this repo and submit PRs if you'd like to

