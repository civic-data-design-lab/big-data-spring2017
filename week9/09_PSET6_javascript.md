# Front End Environments
## HTML/CSS/JavaScript: Problem Set

The data you need for this exercise can be found on [bl.ocks](http://bl.ocks.org/mbostock/3306362) and in the data folder. To complete the exercise, you will need data in **health_care_2014.csv**.

### Instructions

For this Problem Set:

One of the best ways to learn a new library is to read through code and customize it to get started. In this Problem Set, take the [Choropleth Map of US Counties](http://bl.ocks.org/mbostock/3306362) by Mike Bostock, which currently shows unemployment in 2008, and customize it by changing the data shown to **percent without health coverage by county**.

The health coverage data is from American Community Survey, 2014 Five-Year Estimates. Please include a citation in your map.

With the new data, the webpage containing your map should contain:

* The Counties Basemap
* Data colored according to the Health Care Data (see hints!)
* A map title with the name of the map.
* A legend. You can put it anywhere on your webpage.
* Credits and attribution.

Hints:
* The data is in a [CSV](https://github.com/mbostock/d3/wiki/CSV), not a TSV. You will have to change this to load the data.
* Adjust the ranges by adjusting the [linear scale domain and range](https://github.com/mbostock/d3/wiki/Quantitative-Scales#linear_domain). Manually set breaks, and you can do this by eye, no need for a scientific method at this point. If you want, you can visualize the data in Excel to see the spread.
* Get your own colors from [ColorBrewer](http://colorbrewer2.org/). Use a sequential scheme and copy and paste the hex colors.
* Use the HTML and CSS code for the legend [from this page on Legends with HTML and CSS](https://www.mapbox.com/tilemill/docs/guides/advanced-legends/).


### Bonus Exercise!

Explore the [Bl.ocks](http://bl.ocks.org/) website. Locate and find one additional Bl.ock that you can set up on your site and customize. Perhaps find one that is relevant to your project. **The Bl.ock you use doesn't have to be from the Bl.ock homepage (although it can be), feel free to search other Bl.ocks that you might find relevant to your project on Google and stand one up if you want.**

Stand up the Bl.ock you find on your website.

