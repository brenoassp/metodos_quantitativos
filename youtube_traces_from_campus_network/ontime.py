import matplotlib
import matplotlib.pyplot as plt
import subprocess
from datetime import datetime, timedelta

users = {}

p1 = subprocess.Popen(['awk', '-f', 'get_flows_start_between_timestamp_full.awk', 'flow.dat'], stdout=subprocess.PIPE)

output = p1.communicate()[0]

user_time = {}

for line in output.decode("utf-8").split('\n'):
	if len(line) > 0:
	    spl_line = line.split()
	    start_session = datetime.fromtimestamp(float(spl_line[8]))#.strftime("%H:%M:%S")
	    start_session = start_session.replace(microsecond=0)
	    end_session = datetime.fromtimestamp(float(spl_line[9]))
	    end_session = end_session.replace(microsecond=0)
	    session_duration_in_seconds = int((end_session - start_session).total_seconds())
	    try:
	    	user_time[start_session] += 1
	    except KeyError:
	    	user_time[start_session] = 1
	    for sec in range(session_duration_in_seconds):
	    	try:
	    		user_time[(start_session + timedelta(0, sec))] += 1
	    	except KeyError:
	    		user_time[(start_session + timedelta(0, sec))] = 1
	    #print(start_session)
	    #print(end_session)
	    
	    #import pdb;
	    #pdb.set_trace()
	    #break
axis_x = []
axis_y = []
for key, value in user_time.items():
	axis_x.append(key)
	axis_y.append(value)
plt.plot_date(axis_x, axis_y)
#plt.plot(axis_x,axis_y)
#plt.gcf().autofmt_xdate()
plt.show()