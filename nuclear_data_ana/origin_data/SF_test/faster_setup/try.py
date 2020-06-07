from datetime import datetime
datestr=['19-12-2019 00:28:36','20-12-2019 09:14:37']
new_date=[datetime.strptime(d,'%d-%m-%Y %H:%M:%S') for d in datestr]
y=(new_date[1]-new_date[0])
print('{:.2f}'.format(y.total_seconds()/3600))