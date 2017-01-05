# Data Visualization with D3
## D3 Mapping: Create a Traffic Map of Riyadh

For the PSET this week, we are going to create an interactive map using Riyadh congestion data. This will build off of the examples created during the in-class exercise.

We would like you to recreate the following map showing traffic congestion around Riyadh during the course of a typical day. In the **Riyadh_Data_for_class** folder on Dropbox you will find a file for your use in the **PSET8_data** folder named **riyadh_traffic_voc.json**. Use this JSON for your visualization.

The JSON was created from the **Riyadh Road Network (Old)** road dataset and flows found in the **Routing Results (Congestion)** folder. Flows represented are morning, midday, evening, and rest of the day.

You can take some liberty with your design, but should atleast include the following.

![Riyadh PM Traffic][timeseries]

[timeseries]: http://duspviz.mit.edu/_assets/img/pm.png "Riyadh PM Traffic"

#### Requirements

1. Show VOC capacity data at four intervals (AM, MD, PM, and RD)
2. Use a Range Slider to navigate between these four times of the day.
3. Change the thickness of the line depending on the VOC value at the respective time of the day.
4. Add an informative title and supplemental information to your visualization.

### Help and Hints

Fields of relevance in **riyadh_traffic_voc.json** are:
	
* voc_am - volume over capacity in morning hours
* voc_md - volume over capacity at midday
* voc_pm - volume over capacity in evening hours
* voc_rd - volumn over capacity for rest of the day

You can refer to the slider example made in class for this exercise.

* [Slider Map Example - Mike Foster](http://duspviz.mit.edu/d3-workshop/examples/session4/boston-slider-map.html)

* Documentation on the range slider and what it returns are located here:

[http://www.w3schools.com/jsref/dom_obj_range.asp](http://www.w3schools.com/jsref/dom_obj_range.asp)
*Use console.log to see what values are being returned by the range slider.*

* View the following gif to get an idea of each time of day.

[http://duspviz.mit.edu/_assets/img/riyadh_timeseries.gif](http://duspviz.mit.edu/_assets/img/riyadh_timeseries.gif)

<hr>

### In-class Exercise

In-class exercise for this week located at:
[http://duspviz.mit.edu/d3-workshop/mapping-data-with-d3/](http://duspviz.mit.edu/d3-workshop/mapping-data-with-d3/)



If you have trouble, please remember to use Piazza!