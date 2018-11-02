# Names
Since 1910, the Social Security Administration has published a record of people born in each state by year and gender. I provide tools to analyze this data, including measuring the geographical variation and change in popularity over time.

Database
--
The total database is 150 MB in size. Because of this, it is too large to upload to Github. I am creating a condensed version of the database which only includes the top 2000 names or so (as opposed to 30000). 

Functions
--
- Geography

One functionality to determine who regional a name is is calculated by the coefficient of variation with respect to the percent of people born in that state with that given name (geography2). Regionality can be called with either

```
geoMeasure1(name, gender)
geoMeasure2(name, gender)
```
I calculate geographical variation with another metric, geography2, which uses the area of the top 5 states, however this wasn't as useful. 
- "Spikiness"

Spikiness is the measure of how consistent, or not, a name is. Names like Alonzo have remained between 100 and 500 for the last 100 years, whereas names like Sheena see an extreme spike. This can be called with
```
variation(name, gender=None, ... )
```
- Ages of Names

Names like Harper are very young. 99% of people named Harper are under the age of 14. In order to calculate the percentile of a name, you can call 
```
percentileName(name, gender, percentile)
```
