import sys
import os
import re
import json
import matplotlib.pyplot as plt
from random import randint
if len(sys.argv) <= 1:
    logdir = "log"
else:
    logdir = sys.argv[1]

filelist = os.listdir(logdir)

#ver = re.findall("[0-9]+\.[0-9]+",filelist[0])[0]

def get_models_time_bscore(logdir):

    models={}
    def get_time_bscore(fn):
        time_bscore={}
        with open(logdir+"/"+fn) as f:
            for line in json.load(f):
                time_bscore[line[1]] = line[4]
        return time_bscore
    fig = None
    for fn in filelist:
        if "hist" not in fn:
            continue
        (model,algo)=[fn.split(".")[i] for i in (0,1)]
        if model not in models:
            print(model)
            models[model] = {}
            colors=[0x00ffff, 0xff00ff, 0xffff00, 0x0000ff, 0x00ff00, 0xff0000]
            if fig is not None:
                plt.show()
            fig = plt.figure()
            figstuff = fig.add_subplot(111)
            plt.legend(loc='upper left')
            plt.xlabel("time (s)")
            plt.ylabel("score")
            plt.title(model)

        time_bscore = get_time_bscore(fn)
        try:
            color = colors.pop()
        except IndexError:
            print("Warning: not enough colors defined, randomizing.")
            color = randint(1,0xffffff)
        color=hex(color)[2:]

        while(len(color)<6):
            color='0'+color
        color='#'+color
        print(algo)
        models[model][algo] = {'fn':fn, 'algo':algo, 'perf':time_bscore, 'color':color}
        figstuff.scatter(time_bscore.keys(), time_bscore.values(), c=color, label=algo)
    plt.show()
    return models
models = get_models_time_bscore(logdir)





print(models)
