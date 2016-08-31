import sys
import shelve
import json



def save_pretty_json( json_data, filename ):
    outfile = open( filename, "w")
    outfile.write( json.dumps(json_data, indent = 4, sort_keys = True ) )
    outfile.close()


if sys.version_info[0] > 2:
    print("please run with python 2")
    quit()

if len(sys.argv) < 2:
    print("specify shelve")
    quit()

src   = sys.argv[1]
input = shelve.open( src, writeback=False )
out   = {}

for key, value in input.iteritems():
    out[key] = value

save_pretty_json(out, src+".json")

print( src+".json created" )