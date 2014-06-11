# ipy-viz

Some fun experiments with new visualization libraries in (I)Python.

## Notebooks & Scripts

### 01-mrinteract.ipynb

A comparison of IPython's interact & Jake van der Plas' [eipywidgets](https://github.com/jakevdp/ipywidgets)

### 02-bokeh.ipynb

Quick overview of [Bokeh](http://bokeh.pydata.org) with chloropleth plots of 2009 Unemployment data (included in bokeh).

### 03-bokeh-server.ipynb

Using the bokeh-server as a backend, animate moving through my brain.

### 04-bokeh-flask.py

Tiny [Flask](http://flask.pocoo.org) app to display my brain using the bokeh plot server backend. Pretty cool, not hard to extend to lightweight status pages, recent site activity, etc.

### 05-vincent.ipynb

WIP


## Notes

Install into an environment with `pip install -r requirements.txt`. Might want to use conda for some of this (matplotlib, looking at you).

For 03 & 04, you'll need a redis server (bokeh-server's broker). Make sure a instance of bokeh-server is running or the notebook & script will fail fast & hard.