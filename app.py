import numpy as np

import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
measurement = Base.classes.measurement

station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f'Available Routes: <br/>'
        f'/api/v1.0/precipitation <br/>'
        f'/api/v1.0/stations <br/>'
        f'/api/v1.0/tobs <br/>'
        f'/api/v1.0/temp/start_date  <br/>'
        f'/api/v1.0/temp/start_date/end_date <br/>'
        f'Note start_date and end_date must be in yyyy-mm-dd format <br/>'
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return Last 12 months of precipitation data"""
    
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    results = session.query(measurement.date, measurement.prcp).\
        filter(measurement.date >= query_date).all()

    session.close()

    # Convert list of tuples into normal list
    precp = list(np.ravel(results))
    return jsonify(precp)

@app.route('/api/v1.0/stations')
def stations():

    # Create session (link) from Python to the DB
    session = Session(engine)
    
    """Return list of stations"""
    results = session.query(station.station).all()

    session.close()
    
    stations_list = list(np.ravel(results))
    return jsonify(stations_list)

@app.route('/api/v1.0/tobs')
def tobs():
    # Create session (link) from Python to the DB
    session = Session(engine)

    """Temperature observations of the most active station for the past year"""

    query_date = dt.date(2017,8,23) - dt.timedelta(days=365)

    results = session.query(measurement.date, measurement.tobs).\
    filter(measurement.station =='USC00519281').\
    filter(measurement.date >= query_date).all()

    session.close()

    year_data = list(np.ravel(results))
    return jsonify(year_data)

@app.route('/api/v1.0/temp/<start_date>')
@app.route('/api/v1.0/temp/<start_date>/<end_date>')
def start(start_date=None, end_date=None):
    session = Session(engine)
    
    results = []

    if not end_date:
        results = session.query(func.min(measurement.tobs),
              func.max(measurement.tobs),
              func.avg(measurement.tobs)).\
              filter((measurement.date) >= start_date).all()
        print(f'if condition {results}')

           
    else:
        results = session.query(func.min(measurement.tobs),
              func.max(measurement.tobs),
              func.avg(measurement.tobs)).\
              filter((measurement.date) >= start_date).\
              filter((measurement.date) <= end_date).all()
        print(f'else condition {results}')

    session.close()

   

    stats_list = []
    for min, max, avg in results:
        stat_dict = {}
        stat_dict["TMIN"] = min
        stat_dict["TMAX"] = max
        stat_dict["TAVG"] = avg
        stats_list.append(stat_dict)

    #print results or error message
    if stats_list: 
        return jsonify(stats_list)
    else:
        return jsonify({"error": f"check format or date not found"}), 404
    

if __name__ == '__main__':
    app.run(debug=True)