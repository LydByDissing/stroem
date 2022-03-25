#!/usr/local/bin/python3

import pandas as pd
import plotly.graph_objects as go
import sys, getopt
import os

def main(argv):
    inputfile = ''
    outputfile = ''
    headerStr = ''
    minSPL = 60
    maxSPL = 105
    try:
        opts, args = getopt.getopt(argv,"hi:o:c:m:n",["ifile=","ofile=","header=","min=","max="])
    except getopt.GetoptError:
        print ('test.py -i <inputfile> -o <outputfile> -c <header> [--min <min SPL>] [--max <max SPL>]')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <inputfile> -o <outputfile> -c <header> [--min <min SPL>] [--max <max SPL>]')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-c", "--header"):
            headerStr = arg
        elif opt in ("-n", "--min"):
            minSPL = arg
        elif opt in ("-m", "--max"):
            maxSPL = arg

    inputWithComments = open(inputfile, "r")
    # strip out comments
    comment_from_measurement = ''
    noCommentsFileName = '/tmp/no-comments-dataset.csv'
    no_comments = open(noCommentsFileName, 'w')
    ## Add header
    no_comments.write(headerStr + '\n')
    for i, line in enumerate(inputWithComments):
        if line.startswith('*'):
            comment_from_measurement = comment_from_measurement + line
        else:
            # Remove space
            no_comments.write(line.replace(" ", ""))
    no_comments.close()


    df = pd.read_csv(noCommentsFileName)
    header = headerStr.split(',')

    fig = go.Figure()
    fig.add_trace(go.Scatter(x = df[header[0]], y = df[header[1]], name='Frequency Reponse', mode='lines'))
    fig.add_trace(go.Scatter(x = df[header[0]], y = df[header[2]], name='Phase', mode='lines', yaxis='y2'))

    # Setting x-axis as log
    fig.update_xaxes(type="log")

   # Adding a title etc.
    fig.update_layout(title='Measure frequency reposnse; performed using REW',
                      plot_bgcolor='rgb(230, 230,230)',
                      showlegend=True,
                      xaxis=dict(
                        title='Frequency [Hz]',
                        constrain='range',
                        range=[1.69,4.31]
                      ),
                      yaxis=dict(
                        title=header[1],
                        titlefont=dict(
                            color="#1f77b4"
                        ),
                        tickfont=dict(
                            color="#1f77b4"
                        ),
                        constrain='range',
                        range=[minSPL,maxSPL]
                      ),
                      yaxis2=dict(
                        title=header[2],
                        titlefont=dict(
                            color="#ff7f0e"
                        ),
                        tickfont=dict(
                            color="#ff7f0e"
                        ),
                        constrain='range',
                        range=[-250,800],
                        anchor="x",
                        overlaying="y",
                        side="right"
                      )
                    )

    json_graph = open(outputfile, 'w')
    json_graph.write(fig.to_json())
    json_graph.close()

    # generate image
#    fig.write_image("graph.png")

if __name__ == "__main__":
    main(sys.argv[1:])
