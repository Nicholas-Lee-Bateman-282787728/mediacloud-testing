## Standard imports
import matplotlib.pyplot as plt
import pandas 
from datetime import datetime
import glob
from os.path import basename
import re
import csv
import mediacloud, json, datetime
import sys
import pathlib 
import time

def main(topic, n_samples):
    mc = mediacloud.api.MediaCloud('7e5510da993cd51097818a48374dff44495cb251f859ec01d61aaae59284fb6c')

    topic_to_query = {'immigration': '+(immigra* OR migrat* OR migrant*) AND +(US OR "united states") and timespans_id:93598',
    'ebola':'ebola and timespans_id:150307',
    'vaccines':'vaccin* and timespans_id:9596',
    'us_election': '+( fiorina ( scott and walker ) ( ben and carson ) trump ( cruz and -victor ) kasich rubio (jeb and bush) clinton sanders ) AND timespans_id:80252',
    'deep_state': '("deep state") NOT (erdogan or turk* or egypt* or morsi or syria* or pakistan* or shock or depression) AND timespans_id:186103',
    'community_policing': '"Community policing" OR "community-oriented policing" OR "neighborhood policing" OR "Safer Neighbourhood Team*" AND timespans_id:180716',
    'gun_violence':'gun* AND (shoot* OR violence OR death* OR dead OR control OR "bear arms" OR "second amendment") AND timespans_id=183049',
    'teen_pregnancy':'( sentence: ( "babies having babies" "kids having kids" "children having children" "teen mother" "teen mothers" "teen father" "teen fathers" "teen parent" "teen parents" "adolescent mother" "adolescent mothers" "adolescent father" "adolescent fathers" "adolescent parent" "adolescent parents" ( ( /teen(ager)?s?/ adolescent students? "high school" "junior school" "middle school" "jr school" ) and -( /(grad(uate)?|doctoral|law|medical)/ and /students?/ ) and ( pregnant pregnancy "birth rate" births ) ) ) or title: ( "kids having kids" "children having children" "teen mother" "teen mothers" "teen father" "teen fathers" "teen parent" "teen parents" "adolescent mother" "adolescent mothers" "adolescent father" "adolescent fathers" "adolescent parent" "adolescent parents" ( ( /teen(ager)?s?/ adolescent students? "high school" "junior school" "middle school" "jr school" ) and -( /(grad(uate)?|doctoral|law|medical)/ and /students?/ ) and ( pregnant pregnancy "birth rate" births ) ) ) ) AND timespans_id=8938',
    'network_neutrality':'+((net OR network) AND neutrality) AND timespans_id=17212',
    'climate_change':'"climate change" OR "global warming" AND timespans_id=149406'
    }


    q = topic_to_query[topic]

    # Make directory if it doesn't exist
    pathlib.Path('../data/sampling/' + topic).mkdir(parents=True, exist_ok=True) 

    start = time.time()

    for N in [1000, 10000, 100000]:
         print("\n\n","N",N)
         pathlib.Path('../data/sampling/' + topic + '/' + str(N)).mkdir(parents=True, exist_ok=True) 

         for m in range(int(n_samples)):
             print("SAMPLE: ", str(m))
             start_s = time.time()
             sample = mc.wordCount(q, sample_size=N, random_seed=m)
             print("TIME FOR API: ", str(time.time() - start_s), " SEC")
             path = '../data/sampling/'+ topic + "/" + str(N) + "/sample" + str(m) + ".csv"
             print(path)
             pandas.read_json(json.dumps(sample), orient='records').to_csv(path)
            
    # print("TOTAL TIME FOR TOPIC: ", time.time() - start)
    # print(sys.argv[1])
    print(q)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])


