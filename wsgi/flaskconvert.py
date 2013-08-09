#!/usr/bin/env python2
# coding=utf-8
# py-convert 0.1
# https://github.com/sadsfae/
# simple temperature and conversion wsgi app for my own selfish reasons
# converts F <-> C and CZK <-> USD

from flask import Flask, request, redirect, render_template, url_for
from flaskext.htmlbuilder import html, render

app = Flask(__name__)

import os
import sys

# render default HTML index
@app.route("/")
def index():
    return render_template('index.html')

#### F <-> C temperature conversion
# 1°F = 0.556°C
# 1°C = 1.8°F
# °F to °C  Deduct 32, then multiply by 5, then divide by 9
# °C to °F  Multiply by 9, then divide by 5, then add 32

# convert Celcius to Farenheit
def C2F(temp):
    "convert celcius to farenheit"
    return (temp * 9.0) / 5.0 + 32

# convert Farenheit to Celcius
def F2C(temp):
    "convert farenheit to celcius"
    return (temp - 32) * 5.0 / 9.0

# take the results of temperature and post them
@app.route("/post_temp_convert", methods=["POST"])
def tempconvert():
    "post input for temperature"
    temptype = request.form['temptype']
    temp = float(request.form['temp'])

    if temptype == 'C':
        txt = render([
            html.doctype('html'),
            html.html(lang='en')(
                html.head(
                    html.title('celcius to farenheit')
                ),
                html.body(
                    str(C2F(temp))
                    )
            )
        ])
    elif temptype == 'F':
        txt = render ([
            html.doctype('html'),
            html.html(lang='en')(
                html.head(
                    html.title('farenheit to celcius')
                    ),
                html.body(
                    str(F2C(temp))
                    )
                )
            ])
    else:
        txt = 'Not valid input'

    return txt

#### CZK to USD currency ####
# 1 czk = .051 USD
# 1 USD = 19.30 czk

# current conversion rate
def czktousd(currencyamount):
    "convert czk to usd"
    return (currencyamount * 0.051)

def usdtoczk(currencyamount):
    "convert usd to czk"
    return (currencyamount * 19.30)

# take the results of currency and post them
@app.route("/post_currency_convert", methods=["POST"])
def currencyconvert():
    "post input for currency"
    currencytype = request.form['currencytype']
    currencyamount = float(request.form['currencyamount'])

    if currencytype == 'USD':
        txt = render([
            html.doctype('html'),
            html.html(lang='en')(
                html.head(
                    html.title('USD -> CZK')
                    ),
                html.body(
                    str(usdtoczk(currencyamount))
                    )
                )
            ])

    elif currencytype == 'CZK':
        txt = render ([
            html.doctype('html'),
            html.html(lang='en')(
                html.head(
                    html.title('CZK -> USD')
                    ),
                html.body(
                    str(czktousd(currencyamount))
                    )
                )
            ])
    else:
        txt = 'not valid input'

    return txt

if __name__ == '__main__':
    app.run
