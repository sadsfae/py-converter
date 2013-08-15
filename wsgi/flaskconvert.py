#!/usr/bin/env python
# coding=utf-8
# py-convert 0.2.1
# https://github.com/sadsfae/
# simple temperature, currency and distance conversion for my own selfish reasons
# converts F <-> C and CZK <-> USD and KM/M <-> Miles/Feet and kg <-> lbs

from flask import Flask, request, redirect, render_template, url_for
from flaskext.htmlbuilder import html, render

app = Flask(__name__)

import os
import sys

# render default HTML index
@app.route("/")
def index():
    return render_template('index.html')

#### F <-> C temp conversion ####
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
# 1 kuna (HRK)= 0.18 USD
# 1 USD = 5.68 kuna (HRK) 

# current conversion rate
def czktousd(currencyamount):
    "convert czk to usd"
    return (currencyamount * 0.051)

def usdtoczk(currencyamount):
    "convert usd to czk"
    return (currencyamount * 19.30)

def hrktousd(currencyamount):
    "convert kuna to USD"
    return (currencyamount * 0.18)

def usdtohrk(currencyamount):
    "convert USD to kuna"
    return (currencyamount * 5.68)

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

    elif currencytype == 'HRK':
        txt = render ([
            html.doctype('html'),
            html.html(lang='en')(
                html.head(
                    html.title('HRK -> USD')
                    ),
                html.body(
                    str(hrktousd(currencyamount))
                    )
                )
            ])

    elif currencytype == 'USD-H':
        txt = render ([
            html.doctype('html'),
            html.html(lang='en')(
                html.head(
                    html.title('USD -> HRK')
                    ),
                html.body(
                    str(usdtohrk(currencyamount))
                    )
                )
            ])

    else:
        txt = 'not valid input'

    return txt

#### distance conversion ####
# 1 meter = 3.28084 feet
# 1 kilometer = 0.621371 miles

# convert meters to feet
def M2F(distanceamount):
    "convert meters to feet"
    return (distanceamount * 3.28084)

# convert feet to meters
def F2M(distanceamount):
    "convert feet to meters"
    return (distanceamount / 3.28084)

# convert kilometers to miles
def K2M(distanceamount):
	"convert kilometers to miles"
	return (distanceamount * 0.621371)

# convert miles to kilometers
def M2K(distanceamount):
	"convert miles to kilometers"
	return (distanceamount / 0.621371)

# take the results of the distance and post them
@app.route("/post_distance_convert", methods=["POST"])
def distanceconvert():
    "post input for distance"
    distancetype = request.form['distancetype']
    distanceamount = float(request.form['distanceamount'])

    if distancetype == 'm':
        txt = render([
            html.doctype('html'),
            html.html(lang='en')(
                html.head(
                    html.title('meters -> feet')
                    ),
                html.body(
                    str(M2F(distanceamount))
                    )
                )
            ])
    elif distancetype == 'ft':
        txt = render ([
            html.doctype('html'),
            html.html(lang='en')(
                html.head(
                    html.title('feet -> meters')
                    ),
                html.body(
                    str(F2M(distanceamount))
                    )
                )
            ])
    elif distancetype == 'KM':
		txt = render ([
            html.doctype('html'),
            html.html(lang='en')(
                html.head(
                    html.title('kilometers -> miles')
                    ),
                html.body(
                    str(K2M(distanceamount))
                    )
                )
            ])
    elif distancetype == 'Miles':
		txt = render ([
            html.doctype('html'),
            html.html(lang='en')(
                html.head(
                    html.title('miles -> kilometers')
                    ),
                html.body(
                    str(M2K(distanceamount))
                    )
                )
            ])
    else:
		txt = 'Not valid input'
    return txt

#### KG <-> Lbs weight conversion ####
# 1kg = 2.20462 lbs
# 1LB = 0.453592 kg

# convert kilograms to lbs
def K2P(weight):
    "convert kilograms to pounds"
    return (weight * 2.20462) 

# convert lbs to kilograms
def P2K(weight):
    "convert pounds to kilograms"
    return (weight * 0.453592)

# take the results of temperature and post them
@app.route("/post_weight_convert", methods=["POST"])
def weightconvert():
    "post input for weight"
    masstype = request.form['masstype']
    weight = float(request.form['weight'])

    if masstype == 'kg':
        txt = render([
            html.doctype('html'),
            html.html(lang='en')(
                html.head(
                    html.title('kilograms -> lbs')
                ),
                html.body(
                    str(K2P(weight))
                    )
            )
        ])
    elif masstype == 'lb':
        txt = render ([
            html.doctype('html'),
            html.html(lang='en')(
                html.head(
                    html.title('lbs -> kilograms')
                    ),
                html.body(
                    str(P2K(weight))
                    )
                )
            ])
    else:
        txt = 'Not valid input'
    
    return txt

if __name__ == '__main__':
    app.run
