## [Don't Poison Our Kids](https://github.com/emw1687/metis_projects/blob/master/03_mcnulty/presentation.pdf)
### Flint: A Cautionary Tale

#### Summary
In April 2014, the City of Flint switched their water source from the Detroit water system to the Flint River. A year and a half later, the City switched the source back, but by that time, residents had been exposed to dangerous levels of lead and other contaminants in their drinking water.

As an environmental engineer by training and practice as well as a former AmeriCorps member and public servant, I was very interested in piecing together how this could have happened: my hypothesis is that Flint was at the center of a perfect storm of aging physical infrastructure, mismanagement of the public water supply, and socio-economic characteristics.

Because the Massachusetts Department of Environmental Protection has initiated an assistance program with public schools, drinking water quality data from schools across the state is available. With the Flint framework in mind, I built models to explore the relationship between physical infrastructure, public water supply management indicators, socio-economic characteristics, and drinking water quality in Massachusetts public schools.

Thankfully, in Massachusetts, physical infrastructure is most influential factor in predicting water quality.

![Random Forest Features](https://emw1687.github.io/images/rf_features.png?raw=true)

#### Tools
* [QGIS](http://www.qgis.org/en/site/)
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
* [Pandas](http://pandas.pydata.org/)
* [Seaborn](http://seaborn.pydata.org/index.html)
* [Scikit-learn](http://scikit-learn.org/stable/)

#### Data Sources
[MassDEP](http://www.mass.gov/eea/agencies/massdep/)
* [Lead & Copper Rule - Public Water Systems 90th Percentile Lead Sampling Results](http://www.mass.gov/eea/agencies/massdep/water/drinking/public-water-systems-lead-90th-lead-sampling-results.html)
* [Lead and Copper in School Drinking Water Sampling Results](http://www.mass.gov/eea/agencies/massdep/water/drinking/lead-and-copper-in-school-drinking-water-sampling-results.html)
* [Lead and Copper Rule (LCR) Survey Results](http://www.mass.gov/eea/agencies/massdep/water/drinking/lead-in-drinking-water.html)
* [MA Public Water Supplier Contacts Sorted by Town](http://www.mass.gov/eea/agencies/massdep/water/drinking/public-water-systems-lead-90th-lead-sampling-results.html)

[MassGIS](http://www.mass.gov/anf/research-and-tech/it-serv-and-support/application-serv/office-of-geographic-information-massgis/)
* [Public Water Supplies](http://www.mass.gov/anf/research-and-tech/it-serv-and-support/application-serv/office-of-geographic-information-massgis/datalayers/pws.html)
* [Level 3 Assessors’ Parcel Mapping](http://www.mass.gov/anf/research-and-tech/it-serv-and-support/application-serv/office-of-geographic-information-massgis/datalayers/l3parcels.html)
* [Schools (Pre-K through High School)](http://www.mass.gov/anf/research-and-tech/it-serv-and-support/application-serv/office-of-geographic-information-massgis/datalayers/schools.html)
* [2010 U.S. Census - Environmental Justice Populations](http://www.mass.gov/anf/research-and-tech/it-serv-and-support/application-serv/office-of-geographic-information-massgis/datalayers/cen2010ej.html)
* [MassDEP Hydrography (1:25,000)](http://www.mass.gov/anf/research-and-tech/it-serv-and-support/application-serv/office-of-geographic-information-massgis/datalayers/hd.html)

#### Pipeline
1. Use QGIS to merge schools data with parcels data
2. [Clean MassDEP School Drinking Water Sampling Results and merge with school building and environmental justice data](https://github.com/emw1687/metis_projects/blob/master/mcnulty/notebooks/01_MassDEP_School_Sampling_cleaning.ipynb)
3. [Scrape and clean](https://github.com/emw1687/metis_projects/blob/master/mcnulty/notebooks/02_MWRA_scraping_and_cleaning.ipynb) [MWRA data](http://www.mwra.state.ma.us/02org/html/whatis.htm)
4. [Create management indicators and merge with consolidated public water supply data](https://github.com/emw1687/metis_projects/blob/master/mcnulty/notebooks/03_PWS_Cleaning.ipynb)
5. [Preprocesses features and target for modeling](https://github.com/emw1687/metis_projects/blob/master/mcnulty/notebooks/04_Make_features_target.ipynb)
6. [Create models and tune parameters](https://github.com/emw1687/metis_projects/blob/master/mcnulty/notebooks/05_MassDEP_School_Sampling_models.ipynb)
