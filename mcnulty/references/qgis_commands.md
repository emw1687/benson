### Add parcel data to schools

```python
processing.runalg("qgis:joinattributesbylocation","/vsizip//Users/evaward/ds/metis/metisgh/metis_projects/mcnulty/data/external/schools.zip","/vsizip//Users/evaward/ds/metis/metisgh/metis_projects/mcnulty/data/external/parcels/L3_TAXPAR_POLY_ASSESS.zip",['intersects', 'within'],0,0,"sum,mean,min,max,median",1,"/Users/evaward/.qgis2//processing/outputs/schools_parcels")
```
