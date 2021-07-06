# ex3_dsp

This is a implementation of algorithms which solve Densest Subgraph Problem(DSP). I implemented max-flow based algorithm presented by [Goldberg (1984)](https://www2.eecs.berkeley.edu/Pubs/TechRpts/1984/CSD-84-171.pdf), greedy peeling algorithm presented by [Charikar (2000)](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.121.1184&rep=rep1&type=pdf) and GREEDY++ presented by [Boob et al (2020)](https://arxiv.org/pdf/1910.07087.pdf).

Through some experiments, I tried to grasp the essence of GREEDY++. I found that the load of nodes which consists of the densest subgraph become heavier after enough iterations, and remained until other nodes are removed. I think all graphs will show same tendency, and this makes GREEDY++ work well. 

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
