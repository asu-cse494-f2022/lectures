# Force-directed layouts

`d3-force` is what D3 uses for implementing network layouts.  Here are some good links for using D3 force and drawing networks:

* [d3-force](https://github.com/d3/d3-force): The documentation for d3-force
* [Tom Roth's examples](https://tomroth.com.au/d3/): This page contains several examples showing how to modify force directed layouts for customized behavior, such as "sticky nodes" keeping the graph inside a bounding boxc, etc. This uses D3 v4 code, but these examples will work minimal (or no) modifications in v5.
* [d3-force testing ground](https://bl.ocks.org/steveharoz/8c3e2524079a8c440df60c1ab72b5d03): This page let's you play with several different force parameters.
* [Modifying a force-directed graph](https://observablehq.com/@d3/modifying-a-force-directed-graph): An example of updating a force-directed graph using `join`.
* [25 Days of D3: Force simulation](https://observablehq.com/@thetylerwolf/day-23-force-simulation): A nice tutorial on doing force-based simulation to place items along a horizontal line.
* [d3-force in Observable](https://observablehq.com/collection/@d3/d3-force): A list of Observable blocks using d3-force.
* [Hierarchical edge bundling](https://www.d3-graph-gallery.com/bundle.html): If you want to implement edge bundling, this page provides some links.
* [Networks on maps](https://www.d3-graph-gallery.com/connectionmap.html): For map data that uses projections, this page shows how to use `d3.geoPath()` to compute arc links.

# Hierarchical layouts

`d3-hierarchy` is used for hierarchical data, including trees, treemaps, circle packing, sunbursts, etc.

Here are some resources for drawing hierarchical data:
* [d3-hierarchy](https://github.com/d3/d3-hierarchy): The documentation for d3-hierarchy.
* [d3-hierarchy in Observable](https://observablehq.com/collection/@d3/d3-hierarchy) A list of Observable blocks using d3-hierarchy.
* [Making hierarchy layouts with D3.js
](https://medium.com/nightingale/making-hierarchy-layouts-with-d3-hierarchy-fdb36d0a9c56): This tutorials covers using `d3-group` and `d3-rollup` to transform "flat" CSV data into hierarchical data.


# Data Formats

Network data files are commonly formatted either as a pair of CSV files (one for nodes and one for links) or using a JSON file. Here's an example of each.

* [Star wars data using CSV files](https://github.com/pablobarbera/data-science-workshop/tree/master/sna/data)
* [Star wars data using JSON files](https://www.kaggle.com/ruchi798/star-wars?select=starwars-episode-1-interactions-allCharacters.json)

The `star-wars.html` file shows an example of creating a network using a JSON file.