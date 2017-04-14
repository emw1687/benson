## [What is the Pilsen of New York?](https://github.com/emw1687/metis_projects/blob/master/05_kojak/presentation.pdf)
### Recommending neighborhoods using topic modeling

#### Tools
* [geopandas](http://geopandas.org/)
* [pyproj](https://pypi.python.org/pypi/pyproj?)
* [geopy](https://github.com/geopy/geopy)
* [nltk](http://www.nltk.org/)
* [Pandas](http://pandas.pydata.org/)
* [Seaborn](http://seaborn.pydata.org/index.html)
* [Scikit-learn](http://scikit-learn.org/stable/)
* [d3](https://d3js.org/)
* [Flask](http://flask.pocoo.org/)

#### Data Sources
* [Inside Airbnb](http://insideairbnb.com/get-the-data.html)
* [Zillow](https://www.zillow.com/howto/api/neighborhood-boundaries.htm)

#### Pipeline
1. [Assign neighborhoods to listings based on lat/long](https://github.com/emw1687/metis_projects/blob/master/05_kojak/notebooks/01_assign_neighborhoods.ipynb)
2. [Clean data](https://github.com/emw1687/metis_projects/blob/master/05_kojak/notebooks/02_cleaning.ipynb) and [complete EDA](https://github.com/emw1687/metis_projects/blob/master/05_kojak/notebooks/03_eda.ipynb)
3. [Preprocess neighborhood descrptions for NLP](https://github.com/emw1687/metis_projects/blob/master/05_kojak/notebooks/04_nlp_preprocessing.ipynb)
4. Try different clustering methods:
  * [NMF/LDA](https://github.com/emw1687/metis_projects/blob/master/05_kojak/notebooks/05a_nmf_lda.ipynb) (visualize LDA clusters using [pyLDAvis](https://github.com/emw1687/metis_projects/blob/master/05_kojak/notebooks/06_pyldavis.ipynb))
  * [PCA](https://github.com/emw1687/metis_projects/blob/master/05_kojak/notebooks/05b_pca_clustering.ipynb)
  * [Neighborhood amenity scores](https://github.com/emw1687/metis_projects/blob/master/05_kojak/notebooks/05c_scores.ipynb)
5. Try different regression methods for hyperlocal modeling:
  * [Linear Regression](https://github.com/emw1687/metis_projects/blob/master/05_kojak/notebooks/07a_linear_regression.ipynb)
  * [Random Forest Regression](https://github.com/emw1687/metis_projects/blob/master/05_kojak/notebooks/07b_random_forest_regression.ipynb)
6. Create recommendation systems:
  * [Based on features of listings](https://github.com/emw1687/metis_projects/blob/master/05_kojak/notebooks/08a_rec_system_features.ipynb)
  * [Based on neighborhood descriptions](https://github.com/emw1687/metis_projects/blob/master/05_kojak/notebooks/08b_rec_system_nlp.ipynb)
