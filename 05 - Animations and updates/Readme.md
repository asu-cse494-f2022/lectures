# Animation Examples

Transitions are how D3 handles animating elements in the DOM. Transitions are invoked using `<selection>.transition()`.

There are a couple of animation-specific methods to be aware of:
* `<selection>.transition()`: schedule a transition for the current selection of elements.
* `transition.duration()`: specify the duration of the animation in milliseconds.
* `transition.delay()`: specify the delay in milliseconds before starting the transition.
* `transition.ease()`: specify an [easing function](https://bl.ocks.org/d3noob/39e8263efd3db34c3bde486f9067a961) (linear, elastic, bounce, etc.).


You can combine multiple animation-specific functions in a transition, and even chain transitions together, as shown in the code examples. Once you call a transition, you then specify the `attr`s or `style`s you wan to update. In your transition is not working, you can check:

* The order of the animation-specific methods, which can be important.
* Does your selection contain the elements you want to update?
* Are you actually updating the correct `attr` or `style` elements? A common mistake is, for example, originally setting something like `.style('fill','blue')` on an element, but then calling a transiition like `.attr('fill','green')`, which won't work.


Here are some good references for transitions:
* https://www.tutorialsteacher.com/d3js/animation-with-d3js
* *https://www.d3-graph-gallery.com/graph/interactivity_transition.html

# D3 Joins

D3's old way to control data and elements in the browser was via the **enter, update, exit** pattern, where data fell into one of three buckets based on whether it should be inserted (**enter**), updated (**update**), or deleted (**exit**). This article describs the idea: [Thinking with Joins](https://bost.ocks.org/mike/join/). 

I highly recommend reading over it simply to see how things were done for several years, and to understand how D3 interprets data while adding it to the SVG.

D3 v5.8 introduced the `<selection>.join` functionality as an alternative. This simplifies the process of entering, updating, and exiting data. These two links give a nice description:

* https://observablehq.com/@d3/selection-join
* https://observablehq.com/@thetylerwolf/day-18-join-enter-update-exit

So far, we've used the following pattern to add and position elements to the SVG based on some data:

`d3.selectAll('whatever')``.data( data ).enter().append('whatever')`

You can also do the same with joins:

`d3.selectAll('whatever').data( data ).join('whatever')`

Using join is powerful because as items are added to, removed from, or updated within a data array, these changes can be applied to the visualization. By combining joins with animations, you can dynamically add, update, and remove items in an animated way that is very intuitive for the user.
