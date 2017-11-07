# dfcbenchmarker

Simulations for testing covariance tracking. Accompanies the article by Thompson et al (preprint) [A simulation and comparison of dynamic functional connectivity methods](https://www.biorxiv.org/content/early/2017/11/01/212241)

## Contents 

- Install dfcbenchmarker 

- What you can do with dfcbenchmarker 

- What you cannot do with dfcbenchmarker 

- Run all simulations with default parameters

- Add new method

- Send the method 

- Custom parameter dictionary 

##Install

You can install dfcbenchmarker through pip ([What is pip?](http://www.pythonforbeginners.com/basics/how-to-use-pip-and-pypi/)), simply type:

```bash
pip install dfcbenchmarker
```

It is tested only on Python 3 but, in principle, should work on Python 2.

__(note this only applies once this README is complete (i.e. when the "*This is to be completed soon*" are filled in)). Until then, manual install. Download the repo (`git clone http://github.com/wiheto/dfcbenchmarker`) and type pip install /path/to/repo__

## What you can do with dfcbenchmarker

- Rerun the entire code.
- Add new methods that get benchmarked in the same way as the other methods.
- Send the new method within dfcbenchmarker so it gets added in future reports.
- Change the parameters of different simulations. Multiple parameters can be specified for (nearly) all parameters.

## What you cannot do with dfcbenchmarker

- Make new simulation scenarios within dfcbenchmarker  (i.e. the structure of the 4 simulations cannot be changed, just the parameters within each simulation)
- Test methods that rely on frequency-specific properties (e.g. phase correlations).

## Run all simulations with default parameters

To run all simulations, used `dfcbenchmarker.run_simulations()`

```python
import dfcbenchmarker
dfcbenchmarker.run_simulations()
```

The default will take the latest simulation routine and it uses the precalculated data included with the package (both simulations and DFC estimates). The statistics gets recalculated each time (this may be included in a later version).

If you want to calculate everything from the start.

```python
dfcbenchmarker.run_simulations(usesaved=False)
```

When there are additional routines (e.g. additional simulations) you can specify the version number to specify which version you want to run:

```python
dfcbenchmarker.run_simulations(routine_version=1.0,usesaved=False)
```

The default will be the latest simulation routine.

`rountine_version` can also be a path to a json file that contains a custom parameter file (see below).

```python
dfcbenchmarker.run_simulations(routine_version='./my/simulation/parameter.json',usesaved=False)
```

Note: DFC estimates are calculated with teneto (Requirement says v0.2.1). At the moment (although it shouldn't) it writes a ./report file which contains a html report of DFC derivation (and overwrites this for each method) --- This directory can be ignored. Teneto v0.2.2 and above will fix this.

## Add new method

dfcbenchmarker tests 5 different methods.

Let us say that, for some reason a think $(x_1 + x_2)^3$ is a good estimate for the relationship between $x_1$ and $x_2$. This will be the method we benchmark against everything else.

```python
import numpy as np
def power3(x1,x2,params):
return np.power(x1*x2,3)
```

*This is to be completed soon*

## Send method

*This is to be completed soon*

There are then a couple of questions, such as email address, name, DOIs/pmids of relevant publications which should be cited when reporting the method etc.  Then there are a number of questions to approve (e.g. everything is sent via a Google form). If you do not want to approve of things going via Google, you can just send it to me over Github/email (see article). You also have to approve that dfcbenchmarker can use the code in future version. You can also decide if you want your code to be included in [teneto](github.com/wiheto/teneto) (which is my python package for temporal network/dynamic connectivity).  

Once I've looked at the code, I will send you an email and confirm it works. If I've not sent an email after 1-2 weeks, please let me know (just in case something may break with the Google form method).

## Custom parameter dictionary 

The parameters for each simulation are driven by a parameter dictionary. 

### Parameter dictionary for a single simulation.

To do this there are two ways. Either using `gen_data` or using the simulation specific functions (`gen_data_sim1()`, `gen_data_sim2()`, `gen_data_sim3()`, `gen_data_sim4()`).

Say we want to generate data from simulation 2, we can do the following. 

```python
sim_2_params = {
    "covar_mu": 0.2, 
    "var": 1, 
    "n_samples": 1000, 
    "mu": [0, 0],
    "alpha": 0.2,
    "covar_sigma": 0.1, 
    "randomseed": 2017
}
```

The entire pipline can be grouped together. 

`sim2_data = dfcbenchmarker.gen_data_sim2(sim_2_params,mi=None)`

The `mi`parameter is for which parameters should be looped over (see below).  

This type of parameter dictionary works with `gen_data_sim1()`, `gen_data_sim2()`, `gen_data_sim3()`, `gen_data_sim4()` --- see each function's documentation for their respective parameters needed. 

There is a higher level way to generate data using the funciton `gen_data()`. Using this function the above simulation specific. This allows for the mi property to be included in the parameter file. This dictionary must include three items, `name` (a string), `multi_index` (a list), and 

```python
gen_sim_2_params = {
    'name': 'sim-2',
    'multi_index': [],
    'params': sim_2_params
}
```

Where `sim_2_params` is equal to the dictionary already defined above. Then to run this, `dfcbenchmarker.gen_data` can be run.  

`sim2_data = dfcbenchmarker.gen_data(gen_data_params)`

### Parameter dictionary for multiple simulations. 

`dfcbenchmarker.run_simulations()` runs the entire simulation procedure: generates data, calculates the DFC and performs the statistics, and plots the output. Calling the function as is, or with an integer, uses a predefined parameter dictionary, but you can make one yourself. 

Here we pass a dictionary like for a single simulation, but now contains additional levels in the dictionary. 

The highest level of the parameter dictionary must include the following three items:

```python
pipeline_params = {
    'simulation':{},
    'dfc':{},
    'stats':{}
}
```

The next level of the `simulation` and ` dfc` dictionaries state the simulation or method. Start at 0 and work your way up. 

Let us say we want to perform only a single simulation this way, and a single DFC method. 

```python
pipeline_params = {
    'simulation':{0:{}},
    'dfc':{0:{}},
    'stats': {}
}
```

If we wanted to add multiple 3 simulations and 3 methods, simply type: 

```python
pipeline_params_3 = {
    'simulation':{0:{},1:{},2:{}},
    'dfc':{0:{},1:{},2:{}},
    'stats': {}
}
``` 

Each simulation index can be defined as previous for single simulations:

```python
pipeline_params['simulation'][0] = gen_sim_2_params
```

In the `dfc` dictionary this consists of three items:

```python
pipeline_params['dfc'][0] = {
    'name': ''
    'method': ''
    'params': {}
}
```

The `method` is either; 'SW', 'TSW', 'TD', 'JC', or 'SD' (See section on adding a new method below, if you want to add a new method).

The `name` can whatever you want (used in plotting and table creation). So let us say you have a sliding window with window size 20, and another 120, you may want the names to be 'SW-20' and 'SW-120'. 

The 'params' are the parameters required for each method. See documentation of dfcbenchmarker.dfc_calc. An example of the `dfc` dictionary can then be: 

```python
pipeline_params['dfc'][0] = {
    'name': 'SD',
    'method': 'SD',
    'params': {
        'sd_distance': 'euclidean'
    }
}
```

The final pipeline dictionary alongside the `simulation` and `dfc` dictionaries is the `stats` dictionary. Here you can specify of how many samples should be generated from the MCMC (to be included in the posterior + the number discardeed). Burn is the number discarded. 

```python
pipeline_params['stats'] = {
    "burn": 500,
    "trace": {"samples": 5500}
}
```

These numbers can be changed if the MCMC chains are not converging (see trace plots that are generated in the stats folder). There may be some additional parameters implemented in the future if, for example, different distributions of the DFC estimates are used in the stats model.


This can then be run with `dfc.run_simulations()`

```python
dfcbenchmarker.run_simulations(pipeline_params,usesaved=False,output_dir='my_pipeline')
``` 

Here we also specify which directory the output should be (this is good to do when not using a default routine version.)

Lets put it all together. Here we will define 2 simulations and 3 DFC methods in one dictionary at once: 

```python
pipeline_params_3 = {
    'simulation':{
        0:{
            'name': 'sim-1',
            'multi_index': ['alpha'],
            'params': {
                "mu": [0,0], 
                "sigma": [[1,0.5],[0.5,1]], 
                "n_samples": 10000, 
                "alpha": [0.2,0.8],
                "randomseed": 2017  
            }
        },
        1:{
            'name': 'sim-2',
            'multi_index': ['alpha'],
            'params': {
                "covar_mu": 0.2, 
                "var": 1, 
                "n_samples": 10000, 
                "mu": [0,0],
                "alpha": [0.2,0.8],
                "covar_sigma": 0.1, 
                "randomseed": 2017        
            }
        },
    },
    'dfc':{
        0:{
            'name': 'SW-25',
            'method': 'SW',
            'params': {
                'sw_window': 25
    }
        },
        1:{    
            'name': 'SW-125',
            'method': 'SW',
            'params': {
                'sw_window': 125
    }},
        2:{
            'name': 'JC',
            'method': 'JC',
            'params': {
                'sd_distance': {}
            }
        }
    },
    'stats':{
        "burn": 500,
        "trace": {
            "samples": 5500}
    }
}
```

The above can also be saved as a json. 

What the above code will do is generate data for 2 simulations (sim 1 and sim 2. Sim 1 loops over the `alpha` and `mu` parameters and sim 2 only loops over `alpha`) and uses 3 DFC methods (SW with 20 window size, SW with 120 as window size and Jackknife coorelation). 

Using this dictionary with `dfcbenchmarker.run_simulations(pipeline_params,usesaved=False,output_dir='test-simulations')`

Should run both these simulations, perform the statistics and create plots for each simulaiton in ./test-simulations/

*While aiming to be flexible, sometimes errors can be met * 

## Problems/comments?

Leave an issue here.
