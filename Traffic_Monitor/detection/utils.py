import matplotlib
import matplotlib.pyplot as plt 
import numpy as np
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png', transparent=True)
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y,x2,y2, name):
    matplotlib.rc('axes',edgecolor='w')
    matplotlib.rc('xtick',color='w')
    matplotlib.rc('ytick',color='w')
    plt.switch_backend('AGG')
    plt.figure(figsize=(3.5,3))
    #plt.title(name)
    plt.xlim(0,24)
    # plt.ylim(0,10)
    plt.bar(x,y, width = .8, label = "Entries")
    plt.bar(x2,y2, width = .5, label = "Exits")
    plt.legend(loc="upper left")
    plt.xticks(rotation=45)
    plt.xlabel('Time (24 Hour)', color='white')
    # plt.ylabel('Occurances')
    plt.tight_layout()
    graph = get_graph()
    return graph
