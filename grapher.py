# python grapher.py [--logdir <logdir>] [--x-axis time|gen]

import sys
import os
import re
import json
import matplotlib.pyplot as plt
from random import randint

if '--logdir' in sys.argv:
	logdir = sys.argv[sys.argv.index('--logdir')+1]
else:
	logdir = 'log'
if '--x-axis' in sys.argv:
	(xaxis_name, xaxis_i) = {
		'time': ('time (s)', 1),
		'gen': ('# of generations', 0)
	}[sys.argv[sys.argv.index('--x-axis')+1]]
else:
	(xaxis_name, xaxis_i) = ('time (s)', 1)

filelist = os.listdir(logdir)
filelist.sort()

#ver = re.findall("[0-9]+\.[0-9]+",filelist[0])[0]

def get_and_plot_models_xaxis_bscore(logdir):
    models={}
    def get_xaxis_bscore(fn):
        xaxis_bscore={}
        with open(logdir+"/"+fn) as f:
            for line in json.load(f):
                xaxis_bscore[line[xaxis_i]] = line[4]
        return xaxis_bscore
    fig = None
    for fn in filelist:
        if "hist" not in fn:
            continue
        (model,algo)=[fn.split(".")[i] for i in (0,1)]
        print((model,algo))
        if model not in models:
            print(model)
            models[model] = {}
            colors=[0x00ffff, 0xff00ff, 0xffff00, 0x0000ff, 0x00ff00, 0xff0000]
            if fig is not None:
                plt.legend()
                plt.show()
            fig = plt.figure()
            figstuff = fig.add_subplot(111)
            plt.xlabel(xaxis_name)
            plt.ylabel("score")
            plt.title(model)

        xaxis_bscore = get_xaxis_bscore(fn)
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
        models[model][algo] = {'fn':fn, 'algo':algo, 'perf':xaxis_bscore, 'color':color}
        figstuff.scatter(xaxis_bscore.keys(), xaxis_bscore.values(), c=color, label=algo)
    plt.legend()
    plt.show()
    return models
models = get_and_plot_models_xaxis_bscore(logdir)

