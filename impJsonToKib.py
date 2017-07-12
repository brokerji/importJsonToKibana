import json
import sys
from datetime import datetime

def timestamp_datetime(timestamp):
    dt=datetime.fromtimestamp(timestamp / 1000.0)
    dt1=datetime.isoformat(dt)
    return dt1

if __name__ == "__main__":
    filename = sys.argv[1]
    outputfile = sys.argv[2]
    with open(filename) as f:
        pop_data = json.load(f)
        for i in range(0,len(pop_data['allItems'])):
           # print(pop_data['allItems'][i])
            s = pop_data['allItems'][i]
            #print(type(s))
            #   print("s")
            f = open (outputfile,'a')
            if ('highlight' in s.keys()) and ('start_time' in s.keys()) and ('end_time' in s.keys()):
                #print(type(s['highlight']))
                #print(s['highlight'])
                del s['highlight']
                print (type(s['start_time']))
                s['start_time'] = timestamp_datetime(s['start_time'])
                s['end_time'] = timestamp_datetime(s['end_time'])
               # print(s)
                jsObj=json.dumps(s)
                f.write('{"index":{"_index":"report","_type":"data","_id":')
                f.write(str(i))
                f.write("}}")
                f.write("\n")
                f.write(jsObj)
                f.write("\n")
            else :
                jsObj=json.dumps(s)
                #f.write('{"index":{"_index":"report","_type":"data","_id":')
                #f.write(str(i))
                #f.write("}}")
                #f.write("\n")
                #f.write(jsObj)
                #f.write("\n")
        f.close()



