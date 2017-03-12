## [The New York Times Bestsellers List is stupid.](https://github.com/emw1687/metis_projects/blob/master/luther/presentation.pdf)
### Can data from the NYT Bestseller List help us to predict something useful about a book?

#### Summary
An author of bestselling books himself, [Seth Godin](http://www.sethgodin.com/sg/) has argued that there is no mainstream “cultural radar” today but rather many niche sectors. Due to this phenomenon, lists such as the New York Times (NYT) Bestseller List are not actually a reflection of what’s popular in the culture at large, but rather a reflection of what’s popular in several niche subcultures.

For my second project at Metis, I used web scraping and linear regression to try to find out: is Seth Godin right?

Based on the results of my model, he just might be.

![Mean rating](https://emw1687.github.io/images/rmse.png?raw=true)


#### Tools
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
* [Goodreads API](https://www.goodreads.com/api)
* [Pandas](http://pandas.pydata.org/)
* [Seaborn](http://seaborn.pydata.org/index.html)
* [Statsmodel](http://statsmodels.sourceforge.net/)

#### Pipeline
1. [Scrape](https://github.com/emw1687/metis_projects/blob/master/luther/notebooks/01_wikipedia_scraping.ipynb) and [clean](https://github.com/emw1687/metis_projects/blob/master/luther/notebooks/02_wikipedia_cleaning.ipynb) data from wikipedia pages listing NYT #1 bestsellers from 1942-2016
2. [Retrieve](https://github.com/emw1687/metis_projects/blob/master/luther/notebooks/03_goodreads_api.ipynb) and [clean](https://github.com/emw1687/metis_projects/blob/master/luther/notebooks/04_goodreads_cleaning.ipynb) data about each NYT #1 bestseller using the goodreads API
3. [Explore and visualize the data set](https://github.com/emw1687/metis_projects/blob/master/luther/notebooks/05_nyt_eda.ipynb)
4. [Create linear regression model to predict average book rating ](https://github.com/emw1687/metis_projects/blob/master/luther/notebooks/06_nyt_models_back_to_basics.ipynb)
