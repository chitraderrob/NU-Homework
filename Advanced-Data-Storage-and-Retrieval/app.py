# Import Dependencies

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import datetime as dt
import numpy as np

from flask import Flask, jsonify


engine = create_engine("sqlite:///Resources/hawaii.sqlite?check_same_thread=False")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

# Use FLASK to create your routes.
app= Flask(__name__)


# /
# Home page.
# List all routes that are available.
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date<br/>"
        f"/api/v1.0/start_date/end_date<br/>"
    )

# /api/v1.0/precipitation
# Convert the query results to a Dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary.
@app.route("/api/v1.0/precipitation")
def precipitation():
    last_date = session.query(func.max(Measurement.date)).all()
    last_date_converted = dt.datetime.strptime(last_date[0][0], '%Y-%m-%d')
    first_date=last_date_converted - dt.timedelta(days=365)
    first_date=first_date.strftime('%Y-%m-%d')
    
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date>=first_date).order_by(Measurement.date).all()
   
    precipitation = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["value"] = prcp
        precipitation.append(prcp_dict)
    
    return jsonify(precipitation)

# /api/v1.0/stations
# Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations=list(np.ravel(results))
    
    return jsonify(stations)

# /api/v1.0/tobs
# query for the dates and temperature observations from a year from the last data point.
# Return a JSON list of Temperature Observations (tobs) for the previous year.
@app.route("/api/v1.0/tobs")
def tobs():
    last_date = session.query(func.max(Measurement.date)).all()
    last_date_converted = dt.datetime.strptime(last_date[0][0], '%Y-%m-%d')
    first_date=last_date_converted - dt.timedelta(days=365)
    first_date=first_date.strftime('%Y-%m-%d')

    results = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.date>=first_date).order_by(Measurement.date).all()
    
    tobs_list = []
    for date, tobs in results:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["value"] = tobs
        tobs_list.append(tobs_dict)
    
    return jsonify(tobs_list)

# /api/v1.0/<start> and /api/v1.0/<start>/<end>
# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
@app.route("/api/v1.0/<start>")
def start(start):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    results=session.query(*sel).filter(Measurement.date>=start).all()

    temps=list(np.ravel(results))

    return jsonify(temps)


@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    results=session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    temps1=list(np.ravel(results))

    return jsonify(temps1)


if __name__ == "__main__":
    app.run(debug=True)





