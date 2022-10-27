# Color Maps

D3 provides a numbre of pre-defined color schemes.

* **Ordinal** scales are used for categorical data.
* **Linear** scales are sequential scales that use manually-defined colors.
* **Sequential** scales use pre-defined color palettes provided by D3.

You can also use **quantile**, **quantize**, **threshold** scales to bin or segment ordered data items into bins, where each bin gets its own color band. Here are some good links for applying color scales:

* [d3-scale](https://github.com/d3/d3-scale/blob/master/README.md#quantile-scales) (general documentation for D3 scales)
* [d3-scale-chromatic](https://github.com/d3/d3-scale-chromatic)
* [Quantile, quantize, threshold scales](https://observablehq.com/@d3/quantile-quantize-and-threshold-scales)
* [Managing colors in D3](https://www.d3-graph-gallery.com/graph/custom_color.html)
* [Color scale examples - Jonathan Soma](http://jonathansoma.com/tutorials/d3/color-scale-examples/) (Uses D3 v4)

# Layouts

D3 has a number of layouts for implementing visualizations that require more advanced positioning and styling of marks and channels. For example, a a stacked bar chart layout will compute the position of the individual bars within a stacked relative to ach other, as opposed to explicitly computing and defining the [x, y] coordinates. 

D3 layout methods have no direct visual output. Like scales, line generators, and map projections, layouts are D3 functions that are given some set of data items (and potentially constraints), and they re-map or otherwise transform the data, geneerating a new set of derived data items that are convenient for the specific task or visualization encoding you want to do. 

Here are some of the layouts available in D3:
* [Bin](https://github.com/d3/d3-array/blob/v2.8.0/README.md#bins) (histograms)
* [Chord](https://github.com/d3/d3-chord)
* [Cluster](https://github.com/d3/d3-hierarchy#cluster)
* [Force](https://github.com/d3/d3-force)
* [Hierarchy](https://github.com/d3/d3-hierarchy)
* [Pack](https://github.com/d3/d3-hierarchy#pack)
* [Partition](https://github.com/d3/d3-hierarchy#partition)
* [Pie](https://github.com/d3/d3-shape#pies) and [Arc](https://github.com/d3/d3-shape#arcs)
* [Stack](https://github.com/d3/d3-shape#stacks)
* [Tree](https://github.com/d3/d3-hierarchy#tree)
* [Treemap](https://github.com/d3/d3-hierarchy#treemap)



As an example, `d3.histogram()` creates a histogram generator that groups data items into a desired set of bins. Similar to other D3 layouts, you can use accessor functions to customize the layout.

```
let xScale = d3.scaleLinear()
                .range([0, width])
                .domain([0, d3.max(data)]); // data = [ 1, 115, 5, 80, 20, 75, 25, 30]

let histogram = d3.histgoram()
                  .domain(xScale.domain())
                  .thresholds(xScale.ticks(4));  // 4 bins

const bins = histogram(bins); // assign data points to bins
```

The best way - if you want to implement a specific type of chart that uses a layout - is to review the D3 documentation and examples of the layout in action. The [D3 Graph Gallery](https://www.d3-graph-gallery.com/index.html) has many many examples and combos of layouts, including stacked bar charts, spider/radar charts, parallel coordinates, radial charts, pie charts, stacked area charts, circle packing, treemaps, networks, chord diagrams, and more.

The general approach is that you start with the raw data and _derive_ a modified dataset that is appropriate for as input for the specific layout you want to use. This derived dataset will likely contain additional attributes. For example, when creating pie/donut charts, data items are given attributes like `index`, `startAngle`, `endAngle`, and `padAngle`, which are used by a `d3.arc()` generator (similar to a `d3.line()` call, only it creates arcs instead of lines).