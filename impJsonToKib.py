import json
import sys
from datetime import datetime

def timestamp_datetime(timestamp):
    dt=datetime.fromtimestamp(timestamp / 1000.0)
    dt_format=datetime.isoformat(dt)
    return dt_format

if __name__ == "__main__":
    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    fo = open (outputfile,'a')
    with open(inputfile) as fi:
        pop_data = json.load(fi)
        for i in range(0,len(pop_data['allItems'])):
            s = pop_data['allItems'][i]          
            if ('highlight' in s.keys()) and ('start_time' in s.keys()) and ('end_time' in s.keys()):         
                del s['highlight']
                print (type(s['start_time']))
                s['start_time'] = timestamp_datetime(s['start_time'])
                s['end_time'] = timestamp_datetime(s['end_time'])
                jsObj=json.dumps(s)
                fo.write('{"index":{"_index":"report","_type":"data","_id":')
                fo.write(str(i))
                fo.write("}}")
                fo.write("\n")
                fo.write(jsObj)
                fo.write("\n")
            else :
                jsObj=json.dumps(s)
        fo.close()



