import sys
import shelve
import json


def load_json( filename ):
    raw_data  = open( filename ).read()
    json_data = json.loads( raw_data )
    return json_data



if sys.version_info[0] < 3:
    print("please run with python 3")
    quit()

if len(sys.argv) < 2:
    print("specify jsonified shelve")
    quit()

src = sys.argv[1]
input = load_json( src )

out_name = src.replace('.json','')

out = shelve.open( src + ".p3.shelve", writeback=True )

for key, value in input.items():
    out[key] = value

out.close()

