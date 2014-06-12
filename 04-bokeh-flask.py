#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 04-bokeh-flask.py

Little experiment in embedding Bokeh plots in a Flask app

Hat tip to https://github.com/rpazyaquian/bokeh-flask-tutorial/wiki/Rendering-Bokeh-plots-in-Flask
"""
__author__ = 'Scott Burns <scott.s.burns@gmail.com>'

from flask import Flask, render_template
from bokeh.plotting import image, output_server
output_server('brain-flask', url='default')

from nibabel import load
data = load('data/brain.nii.gz').get_data()

app = Flask(__name__)


def build_plot(slice=None):
    if not slice:
        slice = data.shape[0] / 2
    sliced = data[slice, :, :].T
    p = image(image=[sliced],
          x=list(range(0, sliced.shape[0])),
          y=list(range(0, sliced.shape[1])),
          dw=[sliced.shape[1]],
          dh=[sliced.shape[0]],
          palette=['Greys-9'],
          dilate=True)
    return p.create_html_snippet(server=True)

@app.route('/<int:slice>')
def index(slice):
    plot_tag = build_plot(slice)
    return render_template('index.html', plot=plot_tag)

if __name__ == '__main__':
    app.run(debug=True)