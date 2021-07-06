# ex3_dsp

This is a implementation of algorithms which solve Densest Subgraph Problem(DSP). I implemented 

CLUCB was proposed by Chen et al (2014), and Exact-ExpGap was proposed by Chen, Gupta and Li (2016).

I experiment with graphical matroid, so these algorithms return the maximum spanning tree of Graph $G$. I tried the following two cases.

## data

All datasets are from http://datasets.syr.edu/pages/datasets.html and http://snap.stanford.edu/data/index.html. 

## src

1. convert_graph.py

Input should be .txt or .csv file. In these files, each row has the number of two nodes which are connected, and they should be separeted by space or tab. 

Output will be a binary file which represents the list representation of a graph.

2. exact_dinic.py

Solve DSP with max-flow based algorithm.

3. charikar_greedy.py

Solve DSP with Charikar's greedy peeling algorithm. The output graph of this algorithm has at least 1/2 as dence as the densest subgraph.

4. greedy_pp.py 

Solve DSP with GREEDY++. The output of the first iteration is same as Charikar's greedy peeling algorithm.

5. jaccard.py

Calculate jaccard similarity coefficient(simirality of two sets).

6. for_test.py

Wrapper function.
