import subprocess
from calc import cdf

users = {}

p1 = subprocess.Popen(['awk', '-f', 'get_flows_start_between_timestamp.awk', 'flow.dat'], stdout=subprocess.PIPE)

output = p1.communicate()[0]

for line in output.decode("utf-8").split('\n'):
    if len(line) > 0:
        spl_line = line.split()
        try:
            users[spl_line[0]] = users[spl_line[0]] + float(spl_line[1])
        except KeyError:
            users[spl_line[0]] = float(spl_line[1])

# for ip, size in users.items():
#	print(ip, size/(1024*1024))

numbers = [size / (1024 * 1024) for ip, size in users.items()]
numbers = sorted(numbers)

cdf(numbers)
