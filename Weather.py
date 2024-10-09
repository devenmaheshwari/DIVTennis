import datetime as dt
import meteomatics.api as api

username = 'uc3m_maheshwari_deven'
password = 'a74iVINjM9'

coordinates = [(47.11, 11.47)]
parameters = ['t_2m:C', 'precip_1h:mm', 'wind_speed_10m:ms']
model = 'mix'
startdate = dt.datetime.utcnow().replace(minute=0, second=0, microsecond=0)
enddate = startdate + dt.timedelta(days=1)
interval = dt.timedelta(hours=1)

df = api.query_time_series(coordinates, startdate, enddate, interval, parameters, username, password, model=model)

print(df)