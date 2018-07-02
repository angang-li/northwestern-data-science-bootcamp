# A Flask API based on the hawaii database

# Dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import matplotlib.dates as mdates
import pprint
from flask import Flask, jsonify
import numpy as np


# Create engine connection
engine = create_engine("sqlite:///hawaii.sqlite", connect_args={'check_same_thread':False})
#conn = engine.connect()

# Declare a Base using `automap_base()`
Base = automap_base()

# Use the Base class to reflect the database tables
Base.prepare(engine, reflect=True)

# Assign the classes to variables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session
session = Session(engine)

# Find the latest date of record
latest = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]

# Date 12 months before the last date of record
date_start_query = (latest - dt.timedelta(days=365))

# Flask Setup
app = Flask(__name__)


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/&ltstart&gt, for example, /api/v1.0/2017-01-01<br/>"
        f"/api/v1.0/&ltstart&gt/&ltend&gt, for example, /api/v1.0/2017-01-01/2017-01-04"
    )

# Route /api/v1.0/precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
    
    """
    Return dates and precipitation observations from the last year
    """
    
    results = session.query(Measurement.date, func.avg(Measurement.prcp)).filter(Measurement.date>=date_start_query).group_by(Measurement.date).all()

    results_list = []
    for date, prcp in results:
        results_list.append({str(date): prcp})
    return jsonify(results_list)

# Route /api/v1.0/stations
@app.route("/api/v1.0/stations")
def station():
    
    """
    Return stations
    """
    
    results = session.query(Station.station).all()
    results_list = list(np.ravel(results))

    return jsonify(results_list)

# Route /api/v1.0/tobs
@app.route("/api/v1.0/tobs")
def tobs():
    
    """
    Return dates and temperature observations from the last year
    """
    
    results = session.query(Measurement.date, func.avg(Measurement.tobs)). \
                filter(Measurement.date>=date_start_query). \
                group_by(Measurement.date).all()

    results_list = []
    for date, temp in results:
        results_list.append({str(date): temp})
    return jsonify(results_list)

# Route /api/v1.0/<start>
# Route /api/v1.0/<start>/<end>
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end=latest):

    '''
    Return the minimum temperature, the average temperature, and the max temperature for a given start or start-end range
    '''

    start_date_dt = dt.datetime.strptime(start, '%Y-%m-%d')
    if end == latest:
        end_date_dt = end
    else:
        end_date_dt = dt.datetime.strptime(end, '%Y-%m-%d')

    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    temps = session.query(*sel). \
                filter(Measurement.date>=start_date_dt). \
                filter(Measurement.date<=end_date_dt).all()[0]
    
    results_list = [{"temp_min": temps[0]}, 
                    {"temp_avg": temps[1]}, 
                    {"temp_max": temps[2]}]
    return jsonify(results_list)

if __name__ == '__main__':
    app.run(debug=True)