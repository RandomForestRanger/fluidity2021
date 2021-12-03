from flask import Flask, render_template, request, url_for, send_file, make_response
#import io
#from base64 import b64encode
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import json
#import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

############
# Set up flask
app = Flask(__name__)

@app.route('/')
def do_plot():
    fig = go.Figure(
        data=[
            go.Sankey(
                node=dict(
                    pad=30,
                    thickness=20,
                    line=dict(color='black', width=0.2),
                    label=[
                        'Too young','Did not vote','Other parties','VF+','DA','ANC','EFF','IFP',
                        'Too young','Did not vote','Other parties','VF+','DA','ANC','EFF','IFP',
                        'Too young','Did not vote','Other parties','VF+','DA','ANC','EFF','IFP',
                    ],
                ),
                link=dict(
                #flow source node index
                    source=[0, 0, 0, 0, 0, 0, 0, 1,  1,  1,  1,  1,  1,  1,  1,  2,  2,  2,  2,  2,  2,  2, 2,  3,  3,  3,  3,  3,  3,  3,  4,  4,  4,  4,  4,  4,  4,  5,  5,  5,  5,  5,  5,  5,  6,  6,  6,  6,  6,  6,  6,  7,  7,  7,  7, 8, 8, 8, 8, 8, 8, 8, 8, 9,  9,  9,  9,  9,  9,  9,  9, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 15  ],
                #flow target node index
                    target=[8, 9,10,11,12,13,14, 8,  9, 10, 11, 12, 13, 14, 15,  8,  9, 10, 11, 12, 13, 14,15,  9, 10, 11, 12, 13, 14, 15,  9, 10, 11, 12, 13, 14, 15,  9, 10, 11, 12, 13, 14, 15,  9, 10, 11, 12, 13, 14, 15, 12, 13, 14, 15,16,17,18,19,20,21,22,23,16, 17, 18, 19, 20, 21, 22, 23, 16, 17, 18, 19, 20, 21, 22, 23, 17, 18, 19, 20, 21, 22, 23, 17, 18, 19, 20, 21, 22, 23, 17, 18, 19, 20, 21, 22, 23, 17, 18, 19, 20, 21, 22, 23, 17, 18, 19, 20, 21, 22, 23  ],
                #flow quantity for each source/target pair
                    value =[30,16,3, 0, 2, 2, 0, 0,469, 20,  3, 47, 88, 22,  2,  0, 14,129,  0, 33,  7, 14, 0,  0,  1,  6,  1,  0,  0,  0, 16, 20,  7,554, 30,  9,  3, 56, 25,  0, 42,993, 73,  3,  4,  2,  0,  4, 14, 73,  0,  2,  6,  1, 14, 0,16, 0, 0, 3, 5, 1, 2, 0,413, 19,  0, 29, 44,  3,  9,  0, 79, 36,  0, 16, 20,  2,  0,  4,  1,  7,  3,  0,  0,  0,164, 81,  3,365, 18,  3,  3,365, 83,  0, 59,501, 38, 18, 56, 22,  0,  4, 11, 47,  2,  5,  2,  0,  2,  3,  1,  9  ],
                ),
            )
        ]
    )
    color_for_nodes = ['aquamarine',"plum","moccasin",'green','dodgerblue','lightgreen',"crimson","gold",'aquamarine',"plum","moccasin",'green','dodgerblue','lightgreen',"crimson","gold",'aquamarine',"plum","moccasin",'green','dodgerblue','lightgreen',"crimson","gold"]
    fig.update_traces(node_color = color_for_nodes)
    color_for_edges = [ 'rgba(0,255,191,0.5)', 'rgba(0,255,191,0.5)','rgba(0,255,191,0.5)','rgba(0,255,191,0.5)','rgba(0,255,191,0.5)','rgba(0,255,191,0.5)','rgba(142,69,133, 0.4)','rgba(142,69,133,0.4)','rgba(142,69,133,0.4)','rgba(142,69,133,0.4)','rgba(142,69,133,0.4)','rgba(142,69,133,0.4)','rgba(142,69,133,0.4)','rgba(142,69,133,0.4)','rgba(142,69,133,0.4)','rgba(177,155,115,0.4)','rgba(177,155,115,0.4)','rgba(177,155,115,0.4)','rgba(177,155,115,0.4)','rgba(177,155,115,0.4)','rgba(177,155,115,0.4)','rgba(177,155,115,0.4)','rgba(0,128,0,0.5)','rgba(0,128,0,0.5)','rgba(0,128,0,0.5)','rgba(0,128,0,0.5)','rgba(0,128,0,0.5)','rgba(0,90,156,0.5)', 'rgba(0,90,156,0.5)','rgba(0,90,156,0.5)','rgba(0,90,156,0.5)','rgba(0,90,156,0.5)','rgba(0,90,156,0.5)','rgba(0,90,156,0.5)','rgba(0,90,156,0.5)','rgba(0,90,156,0.5)','rgba(0,90,156,0.5)','rgba(144,238,144,0.5)','rgba(144,238,144,0.5)','rgba(144,238,144,0.5)','rgba(144,238,144,0.5)','rgba(144,238,144,0.5)','rgba(144,238,144,0.5)','rgba(144,238,144,0.5)','rgba(220,20,60,0.4)','rgba(220,20,60,0.4)','rgba(220,20,60,0.4)','rgba(220,20,60,0.4)','rgba(220,20,60,0.4)','rgba(220,20,60,0.4)','rgba(255,215,10,0.8)','rgba(255,215,10,0.8)','rgba(255,215,10,0.8)','rgba(255,215,10,0.8)','rgba(255,215,10,0.8)','rgba(255,215,10,0.8)','rgba(0, 255, 191, 0.5)', 'rgba(0,255,191,0.5)','rgba(0,255,191,0.5)','rgba(0, 255, 191, 0.5)','rgba(0, 255, 191, 0.5)','rgba(0,255,191,0.5)','rgba(0,255,191,0.5)','rgba(0, 255, 191, 0.5)','rgba(142,69,133,0.4)','rgba(142,69,133,0.4)','rgba(142,69,133,0.4)','rgba(142,69,133,0.4)','rgba(142,69,133,0.4)','rgba(142,69,133,0.4)','rgba(142,69,133,0.4)','rgba(142,69,133,0.4)','rgba(177,155,115,0.4)','rgba(177,155,115,0.4)','rgba(177,155,115,0.4)','rgba(177,155,115,0.4)','rgba(177,155,115,0.4)','rgba(177,155,115,0.4)','green','green','green','green','green','rgba(0,90,156,0.5)','rgba(0,90,156,0.5)','rgba(0,90,156,0.5)','rgba(0,90,156,0.5)','rgba(0,90,156,0.5)','rgba(0,90,156,0.5)','rgba(0,90,156,0.5)', 'rgba(0,90,156,0.5)', 'rgba(0,90,156,0.5)', 'rgba(0,90,156,0.5)', 'rgba(144,238,144,0.5)','rgba(144,238,144,0.5)','rgba(144,238,144,0.5)','rgba(144,238,144,0.5)','rgba(144,238,144,0.5)', 'rgba(144,238,144,0.5)','rgba(144,238,144,0.5)','rgba(220,20,60,0.4)','rgba(220,20,60,0.4)','rgba(220,20,60,0.4)','rgba(220,20,60,0.4)','rgba(220,20,60,0.4)','rgba(220,20,60,0.4)','rgba(220,20,60,0.4)','rgba(255,215,10,0.8)','rgba(255,215,10,0.8)','rgba(255,215,10,0.8)','rgba(255,215,10,0.8)','rgba(255,215,10,0.8)','rgba(255,215,10,0.8)','rgba(255,215,10,0.8)','rgba(255,215,10,0.8)' ]
    fig.update_traces(link_color = color_for_edges)

    fig.update_layout(title='SA Voter fluidity 2016-2021 <br>Source: Centre for Social Change, UJ 2021 <br>2016 LGE                                                                                     2019 National Election                                                                                       2021 LGE')
    fig.update_layout(width=1520, height=960, plot_bgcolor='white', paper_bgcolor='rgba(255, 218, 185, 0.2 )')
    fig = fig.show()


    # Save ythe figure into a bytes object so that I can pass it to html
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('plot.html', graphJSON=graphJSON)  #send_file(obj, attachment_filename='plot.png', mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)


# For virutal environment
#   virtualenv env
#   source env/bin/activate
# For heroku deployment, go to minute 42 on https://www.youtube.com/watch?v=Z1RJmh_OqeA

# To deploy to Heroku. Remaining in the virtual env:
#  heroku login
#  git init
#  git add .
#  git commit -m "updated numpy"
#  heroku create cviewza
#  git remote -v
#  git push heroku master
