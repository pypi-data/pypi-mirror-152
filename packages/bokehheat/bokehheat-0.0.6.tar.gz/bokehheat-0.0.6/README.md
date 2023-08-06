# BokehHeat


## Example Results

For the real interactive experience please clone or download this repository
history/theclusterbar_0.0.6.html and history/theclustermap_0.0.6.html files
with your favorite web browser
(we recommend [FireFox](https://www.mozilla.org/en-US/firefox/developer/))
or install bokehheat and run this tutorial.

![heat.clusterbar image](bokehheat_0.0.6.png)

**Figure 1:** This figure shows the static png output from heat.clusterbar and heat.clustermap.
The plots were generated with the tutorial below.


## Abstract

Bokehheat provides a python3, bokeh based, interactive
boolean data, categorical data, numerical data, dendrogram, and heatmap plotting implementation.

+ Minimal requirement: python >= 3.6, bokeh >= 1.1
+ Dependencies: bokeh, matplotlib, pandas, scipy, selenium, phantomjs
+ Programmer: bue, jenny
+ Date origin: 2018-08
+ License: >= GPLv3
+ User manual: this README file
+ Source code: [https://gitlab.com/biotransistor/bokehheat](https://gitlab.com/biotransistor/bokehheat)

Available bokehheat heat plots are:

+ heat.cdendro: an interactive categorical dendrogram plot implementation.
+ heat.bbar: an interactive boolean bar plot implementation.
+ heat.cbar: an interactive categorical bar plot implementation.
+ heat.qbar: an interactive quantitative bar plot implementation.
+ heat.stackedbar: an interactive quantitative stacked bar plot implementation.
+ heat.heatmap: an interactive heatmap implementation.
+ heat.clusterbar (this is your working horse):
  an interactive cluster stackedbar implementation which combines
  heat.cdendro, heat.bbar, heat.cbar, heat.qbar and heat.stackbar under the hood.
+ heat.clustermap (this is your working horse):
  an interactive cluster heatmap implementation which combines
  heat.cdendro, heat.bbar, heat.cbar, heat.qbar and heat.heatmap under the hood.

Available bokehheat jheat plots are:

+ jheat.jdendro: javatreeview compatible dendrogram gtr, atr file output.
+ jheat.jheatmap: javatreeview compatible heatmap cdt file output.
+ jheat.jclustermap: javatreeview compatible heatmap cdt, gtr and atr file output,
  which runs jheat.jdendro and jheat.jheatmap under the hood.


## HowTo Guide

How to install bokehheat?
```bash
pip3 install bokehheat
```

How to load the bokehheat library?
```python
from bokehheat import heat
from bokehheat import jheat
```

How to get reference information about how to use each bokehheat module?
```python
from bokehheat import heat

help(heat.cdendro)
help(heat.bbar)
help(heat.cbar)
help(heat.qbar)
help(heat.stackedbar)
help(heat.clusterbar)
help(heat.heatmap)
help(heat.clustermap)
```

How to get reference information about how to use each javatreeview compatible module?
```python
from bokehheat import jheat

help(jheat.jdendro)
help(jheat.jheatmap)
help(jheat.jclustermap)
```

How to integrate bokehheat plots into [Jupyter](https://jupyter.org/) Notebook and Lab?

Please, have a look at this
[page from the official bokeh documentaion](https://docs.bokeh.org/en/latest/docs/user_guide/jupyter.html#userguide-jupyter).


How to integrate bokehheat plots into [pweave](https://github.com/mpastell/Pweave)
documents?
```python
from pweave.bokeh import output_pweave, show

output_pweave()
o_clustermap, ls_xaxis, ls_yaxis = heat.clustermap(...)
show(o_clustermap)
```

## Tutorial
This tutorial guides you through a cluster bar and cluster heatmap generation process.

1. Load libraries needed for this tutorial:
    ```python
    # library
    from bokehheat import heat, jheat
    from bokeh import io # show
    from bokeh import palettes # Reds9, RdBu11, YlGn8, Colorblind8
    import numpy as np
    import pandas as pd
    ```

1. Prepare data:
    ```python
    ls_observation = ['sample_A','sample_B','sample_C','sample_D','sample_E','sample_F','sample_G','sample_H']
    ls_variable = ['gene_A','gene_B','gene_C','gene_D','gene_E','gene_F','gene_G','gene_H', 'gene_I']

    # generate test data for heatmap
    ar_z = np.random.rand(9,8)
    df_matrix_map = pd.DataFrame((ar_z - 0.5) * 2)
    df_matrix_map.index = ls_variable
    df_matrix_map.columns = ls_observation
    df_matrix_map.index.name = 'y'  # note: this name is necessary to match annotation bars.
    df_matrix_map.columns.name = 'x'  # note: this name is necessary to match annotation bars.

    # generate test data for stacked barplot
    a_matrix_bar = np.array([
        [1/45, 2/45, 3/45, 4/45, 5/45, 6/45, 7/45, 9/45],
        [2/45, 3/45, 4/45, 5/45, 6/45, 7/45, 8/45, 1/45],
        [3/45, 4/45, 5/45, 6/45, 7/45, 8/45, 9/45, 2/45],
        [4/45, 5/45, 6/45, 7/45, 8/45, 9/45, 1/45, 3/45],
        [5/45, 6/45, 7/45, 8/45, 9/45, 1/45, 2/45, 4/45],
        [6/45, 7/45, 8/45, 9/45, 1/45, 2/45, 3/45, 5/45],
        [7/45, 8/45, 9/45, 1/45, 2/45, 3/45, 4/45, 6/45],
        [8/45, 9/45, 1/45, 2/45, 3/45, 4/45, 5/45, 7/45],
        [9/45, 1/45, 2/45, 3/45, 4/45, 5/45, 6/45, 8/45],
    ])
    df_matrix_bar = pd.DataFrame(a_matrix_bar, index=ls_variable, columns=ls_observation)

    # generate gene color dictionary for stacked barplot
    ds_stack_color = {
        # gene
        'gene_A': 'yellow',
        'gene_B': 'olive',
        'gene_C': 'lime',
        'gene_D': 'green',
        'gene_E': 'teal',
        'gene_F': 'cyan',
        'gene_G': 'blue',
        'gene_H': 'navy',
        'gene_I': 'purple',
    }

    # generate some gene annotation for heatmap
    df_variable = pd.DataFrame({
        'y': ls_variable,  # note: this column lable have to match either the df_matrix_map.index.name or df_matrix_map.columns.name
        'genereal': list(np.random.random(9) * 2 - 1),
        'genetype': ['Ligand','Ligand','Ligand','Ligand','Ligand','Ligand','Receptor','Receptor','Receptor'],
        'genetype_color': ['Cyan','Cyan','Cyan','Cyan','Cyan','Cyan','Cornflowerblue','Cornflowerblue','Cornflowerblue'],
        'geneboole': [False, False, False, True, True, True, False, False, False],
    })
    df_variable.index = df_variable.y  # note:

    # generate some sample annotation for heatmap and stacked barplot
    df_observation = pd.DataFrame({
        'x': ls_observation,  # note: this column lable have to match either the df_matrix_map.index.name or df_matrix_map.columns.name
        'age_year': list(np.random.randint(0,101, 8)),
        'sampletype': ['LumA','LumA','LumA','LumB','LumB','Basal','Basal','Basal'],
        'sampletype_color': ['Purple','Purple','Purple','Magenta','Magenta','Orange','Orange','Orange'],
        'sampleboole': [False, False, True, True, True, True, False, False],
    })
    df_observation.index = df_observation.x  # note:
    ```

1. Generate categorical and quantitative sample and gene
    annotation tuple of tuples:
    ```python
    t_yboole = (df_variable, ['geneboole'],'Red','Maroon') # True, False
    t_ycat = (df_variable, ['genetype'], ['genetype_color'])
    t_yquant = (df_variable, ['genereal'], [-1], [1], [palettes.Colorblind8][::-1])

    t_xboole = (df_observation, ['sampleboole'],'Red','Maroon') # True, False
    t_xcat = (df_observation, ['sampletype'], ['sampletype_color'])
    t_xquant = (df_observation, ['age_year'], [0], [128], [palettes.YlGn8][::-1])

    tt_boolecatquant_bar = (t_xquant, t_xcat, t_xboole)
    tt_boolecatquant_map = (t_yboole, t_ycat, t_yquant, t_xboole, t_xcat, t_xquant)
    ```

1. Generate the cluster bar:
    ```python
    s_file = "theclusterbar.html"  # or "theclusterbar.png"
    o_clusterbar, ls_axis = heat.clusterbar(
        df_matrix = df_matrix_bar,
        ds_stack_color = ds_stack_color,
        b_sum_to_1 = True,
        tt_axis_annot = tt_boolecatquant_bar,
        b_dendro = True,
        #s_method = 'average',
        #s_metric = 'euclidean',
        #b_optimal_ordering = False,
        #i_px = 64,
        #i_height = 12,
        #i_width = 12,
        #i_min_border_px = 128,
        s_filename = s_file,
        s_filetitel = 'the Clusterbar',
    )
    ```

1. Display the cluster bar result:
    ```python
    print(f"check out: {s_file}")
    print(f"axis is: {ls_axis}")

    io.show(o_clusterbar)
    ```

1. Generate the cluster heatmap:
    ```python
    s_file = "theclustermap.html"  # or "theclustermap.png"
    o_clustermap, ls_xaxis, ls_yaxis = heat.clustermap(
        df_matrix = df_matrix_map,
        ls_color_palette = heat.seismic256,  # heat.red256
        r_low = -1,
        r_high = 1,
        s_z = "log2",
        tt_axis_annot = tt_boolecatquant_map,
        b_ydendro = True,
        b_xdendro = True,
        #s_method='average',
        #s_metric='euclidean',
        #b_optimal_ordering=False,
        #i_px = 64,
        #i_height = 12,
        #i_width = 12,
        #i_min_border_px = 128,
        s_filename=s_file,
        s_filetitel="the Clustermap",
    )
    ```

1. Display the cluster heatmap result:
    ```python
    print(f"check out: {s_file}")
    print(f"y axis is: {ls_yaxis}")
    print(f"x axis is: {ls_xaxis}")

    io.show(o_clustermap)
    ```
    The resulting clustermap should look something like the example result
    in the section above.

1. Generate cdt, gtr, atr files to be able to study heatmap and clustering
    in the JavaTreeView and TreeView3 software.
    ```python
    t_out = jheat.jclustermap(
        df_matrix=df_matrix_map,
        tt_axis_annot = tt_boolecatquant_map,
        s_xcolor = "age_year",
        s_ycolor = "genetype",
        b_xdendro = True,
        b_ydendro = True,
        #s_method = 'average',
        #s_metric = 'euclidean',
        #b_optimal_ordering = True,
        s_filename = "jclustermap",
    )
    print(t_out)
    ```

## Discussion

In bioinformatics a clustered heatmap is a common plot to present
gene expression data from many patient samples.
There are well established open source clustering software kits like
[Cluster and TreeView](http://bonsai.hgc.jp/%7Emdehoon/software/cluster/index.html),
[JavaTreeView](http://jtreeview.sourceforge.net/),
and [TreeView3](https://bitbucket.org/TreeView3Dev/treeview3/src/master/)
for producing and investigating such heatmaps.

### Static cluster heaptmap implementations

There exist a wealth of
[R](https://cran.r-project.org/) and R/[bioconductor](https://www.bioconductor.org/)
packages with static cluster heatmaps functions (e.g. heatmap.2 from the gplots library),
each one with his own pros and cons.

In Python the static cluster heatmap landscape looks much more deserted.
There are some ancient [mathplotlib](https://matplotlib.org/) based implementations
like this [active state recipe](https://code.activestate.com/recipes/578175-hierarchical-clustering-heatmap-python/)
or the [heatmapcluster](https://github.com/WarrenWeckesser/heatmapcluster) library,
or the [hclustering](https://github.com/wwliao/hclustering) library.
There is the [seaborn clustermap](https://seaborn.pydata.org/generated/seaborn.clustermap.html) implementation,
which looks good but might need hours of tweaking to get an agreeable plot with all the needed information out.

So, static heatmaps are not really a tool for exploring data.

### Interactive cluster heatmap implementations

There exist d3heatmap a R/d3.js based interactive cluster heatmap packages.
And heatmaply, a R/plotly based package.
Or on a more basic level R/plotly based cluster heatmaps can be written
with the ggdendro and ggplot2 library.

But I have not found a full fledged python based interactive cluster heatmap library.
Neither Python/[plottly](https://plot.ly/) nor Python/[bokeh](https://bokeh.pydata.org/en/latest/) based.
The only Python/bokeh based cluster heatmap implementation I was really aware of was this
[listing](https://russodanielp.github.io/blog/plotting-a-heatmap-with-a-dendrogram-using-bokeh/)
from Daniel Russo.
Later on I found this bokeh based [bkheatmap](https://github.com/wwliao/bkheatmap) implementation
from Wen-Wei Liao.

### Synopsis

All in all, all of these implementations were not really what I was looking for.
That is why I rolled my own.
Bokehheat is a [Python3](https://www.python.org/)/[bokeh](https://bokeh.pydata.org/en/latest/)
based interactive cluster heatmap library.

The challenges this implementation tried to solve are,
the library should be:
+ easy to use with [pandas](https://pandas.pydata.org/) dataframes.
+ static output, this means there have to be an easy way to generate static png files as output.
+ interactive output, this means there have to be a easy way to generate hover and zoomable plots.
+ output should be stored in computer platform independent and easy accessible format,
  like png files or java script spiced up html file, which can be opened in any webbrowser.
+ possibility to add as many boolean, categorical, and quantitative y and x annotation bars as wished.
+ possibility to hierarchical cluster y and/or x axis.
+ snappy interactivity, even with big datasets with lot of samples and genes.
  (It turns out bokehheat is ok with hundreds of samples and genes but not with thousands.
  This is why the jheat.py extension was added, to be easily able to generate
  JavaTreeView and TreeView3 compatible output.)

#### Further directions

If you are interested in data visualization, check out Jake VanderPlas talk
[Python Visualization Landscape](https://www.youtube.com/watch?v=FytuB8nFHPQ)
from the PyCon 2017 in Portland Oregon (USA).

## Contributions

+ Implementation: Elmar Bucher
+ Documentation: Jennifer Eng, Elmar Bucher
+ Helpful discussion: Mark Dane, Daniel Derrick, Hongmei Zhang,
    Annette Kolodize, Koei Chin, Jim Korkola, Laura Heiser,
    Matt Melnicki, Bryan Van de Ven, and Daniele Procida.
