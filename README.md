# ipy-viz

Some fun experiments with new visualization libraries in (I)Python.

## Notebooks & Scripts

### 01-mrinteract.ipynb

A comparison of IPython's interact & Jake van der Plas' [ipywidgets](https://github.com/jakevdp/ipywidgets)

[View in NBViewer](http://nbviewer.ipython.org/github/sburns/ipy-viz/blob/master/01-mrinteract.ipynb) 

(takes a while for NBViewer to load it...)

### 02-bokeh.ipynb

Quick overview of [Bokeh](http://bokeh.pydata.org) with chloropleth plots of 2009 Unemployment data (included in bokeh).

[View in NBViewer](http://nbviewer.ipython.org/github/sburns/ipy-viz/blob/master/02-bokeh.ipynb) (but there isn't much to see)

### 03-bokeh-server.ipynb

Using the bokeh-server as a backend, animate moving through my brain.

[View in NBViewer](http://nbviewer.ipython.org/github/sburns/ipy-viz/blob/master/03-bokeh-server.ipynb)

Also not much to see...

### 04-bokeh-flask.py

Tiny [Flask](http://flask.pocoo.org) app to display my brain using the bokeh plot server backend. Pretty cool, not hard to extend to lightweight status pages, recent site activity, etc.


### 05-vincent.ipynb

[Vincent](http://vincent.readthedocs.org/en/latest/) lets us produce [Vega visualizations](http://trifacta.github.io/vega/) in python.

Vincent speaks DataFrames naturally. This notebook uses Vincent to produce some stacked plots of my processed brain image.

[View in NBViewer](http://nbviewer.ipython.org/github/sburns/ipy-viz/blob/master/05-vincent.ipynb)

## Notes

Install into an environment with `pip install -r requirements.txt`. Might want to use conda for some of this (matplotlib, looking at you).

For 03 & 04, you'll need a redis server (bokeh-server's broker). Make sure a instance of bokeh-server is running or the notebook & script will fail fast & hard.
