#!/usr/bin/env python
# coding=utf-8
# py-convert 0.2.4
# https://github.com/sadsfae/
# simple temperature, currency and distance conversion for my own selfish reasons
# converts F <-> C and CZK/EU/HRK/BAHT <-> USD and KM/M <-> Miles/Feet and kg <-> lbs
# and liters/ounces/gallons between each other

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

#### currency ####
# 1 czk = .051 USD
# 1 USD = 19.30 czk
# 1 kuna (HRK)= 0.18 USD
# 1 USD = 5.68 kuna (HRK) 
# 1 USD = 0.75 EU
# 1 EU = 1.34 USD
# 1 EU = 25.68 CZK
# 1 CZK = 0.039 EU
# 1 baht = 0.030 USD
# 1 USD = 33.02 baht
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

def usdtoeu(currencyamount):
    "convert usd to eu"
    return (currencyamount * 0.75)

def eutousd(currencyamount):
    "convert eu to usd"
    return (currencyamount * 1.34)

def czktoeu(currencyamount):
    "convert czk to eu"
    return (currencyamount * 0.039)

def eutoczk(currencyamount):
    "convert eu to czk"
    return (currencyamount * 25.68)

def bhtousd(currencyamount):
    "convert baht to usd"
    return (currencyamount * 0.030)

def usdtobh(currencyamount):
    "convert usd to baht"
    return (currencyamount * 33.02)

#take the results of currency and post them
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

    elif currencytype == 'USD-E':
        txt = render ([
            html.doctype('html'),
            html.html(lang='en')(
                html.head(
                    html.title('USD -> EU')
                    ),
                html.body(
                    str(usdtoeu(currencyamount))
                    )
                )
            ])

    elif currencytype == 'E-USD':
        txt = render ([
            html.doctype('html'),
            html.html(lang='en')(
                html.head(
                    html.title('EU -> USD')
                    ),
                html.body(
                    str(eutousd(currencyamount))
                    )
                )
            ])

    elif currencytype == 'CZK-E':
        txt = render ([
            html.doctype('html'),
            html.html(lang='en')(
                html.head(
                    html.title('CZK -> EU')
                    ),
                html.body(
                    str(czktoeu(currencyamount))
                    )
                )
            ])

    elif currencytype == 'E-CZK':
        txt = render ([
            html.doctype('html'),
            html.html(lang='en')(
                html.head(
                    html.title('EU -> CZK')
                    ),
                html.body(
                    str(eutoczk(currencyamount))
                    )
                )
            ])

    elif currencytype == 'B-USD':
        txt = render ([
            html.doctype('html'),
            html.html(lang='en')(
                html.head(
                    html.title('BAHT -> USD')
                    ),
                html.body(
                    str(bhtousd(currencyamount))
                    )
                )
            ])

    elif currencytype == 'USD-B':
        txt = render ([
            html.doctype('html'),
            html.html(lang='en')(
                html.head(
                    html.title('BAHT -> USD')
                    ),
                html.body(
                    str(usdtobh(currencyamount))
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
def k2p(weight):
    "convert kilograms to pounds"
    return (weight * 2.20462) 

# convert lbs to kilograms
def p2k(weight):
    "convert pounds to kilograms"
    return (weight * 0.453592)

# take the results of temperature and post them
@app.route("/post_weight_convert", methods=["post"])
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
                    str(k2p(weight))
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
                    str(p2k(weight))
                    )
                )
            ])
    else:
        txt = 'not valid input'
    
    return txt

### Liquid calculation ###
# 1 L = 0.264172 gallons
# 1 L = 33.814 ounces
# 1 ounce = 0.0295735 liter
# 1 gallon = 3.78541178 liter

# convert liters to gallons
def l2g(liquid):
    "convert liters to gallons"
    return (liquid * 0.264172)

# convert gallons to liters
def g2l(liquid):
    "convert gallons to liters"
    return (liquid * 3.78541178)

# convert ounces to liters
def o2l(liquid):
    "convert ounces to liters"
    return (liquid * 0.0295735)

# convert liters to ounces
def l2o(liquid):
    "convert liters to ounces"
    return (liquid * 33.814)

# take the results of liquid and post them
@app.route("/post_liquid_convert", methods=["post"])
def liquidconvert():
    "post input for liquid"
    liquidtype = request.form['liquidtype']
    liquid = float(request.form['liquid'])

    if liquidtype == 'L':
        txt = render([
            html.doctype('html'),
            html.html(lang='en')(
                html.head(
                    html.title('liters -> gallons')
                ),
                html.body(
                    str(l2g(liquid))
                    )
            )
        ])
    elif liquidtype == 'G':
        txt = render ([
            html.doctype('html'),
            html.html(lang='en')(
                html.head(
                    html.title('gallons -> liters')
                    ),
                html.body(
                    str(g2l(liquid))
                    )
                )
            ])
    elif liquidtype == 'l':
        txt = render ([
            html.doctype('html'),
            html.html(lang='en')(
                html.head(
                    html.title('liters -> ounces')
                    ),
                html.body(
                    str(l2o(liquid))
                    )
                )
            ]) 

    elif liquidtype == 'o':
        txt = render ([
            html.doctype('html'),
            html.html(lang='en')(
                html.head(
                    html.title('ounces -> liters')
                    ),
                html.body(
                    str(o2l(liquid))
                    )
                )
            ])   

    else:
        txt = 'not valid input'
    
    return txt

if __name__ == '__main__':
