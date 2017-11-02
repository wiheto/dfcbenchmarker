# dfcbenchmarker

Simulations for testing covariance tracking. Accompanies the article by Thompson et al (preprint) [A simulation and comparison of dynamic functional connectivity methods](https://www.biorxiv.org/content/early/2017/11/01/212241)

##Install

You can install dfcbenchmarker through pip ([What is pip?](http://www.pythonforbeginners.com/basics/how-to-use-pip-and-pypi/)), simply type:

```
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

## Run all simulations

To run all simulations, used `dfcbenchmarker.run_simulations()`

```
import dfcbenchmarker
dfcbenchmarker.run_simulations()
```

The default will take the latest simulation routine and it uses the precalculated data included with the package (both simulations and DFC estimates). The statistics gets recalculated each time (this may be included in a later version).

If you want to calculate everything from the start.

```
dfc.run_simulations(usesaved=False)
```

When there are additional routines (e.g. additional simulations) you can specify the version number to specify which version you want to run:

```
dfc.run_simulations(routine_version=1.0,usesaved=False)
```

The default will be the latest simulation routine.

`rountine_version` can also be a path to a json file that contains a custom parameter file (see below).

```
dfc.run_simulations(routine_version='./my/simulation/parameter.json',usesaved=False)
```

Note: DFC estimates are calculated with teneto (Requirement says v0.2.1). At the moment (although it shouldn't) it writes a ./report file which contains a html report of DFC derivation (and overwrites this for each method) --- This directory can be ignored. Teneto v0.2.2 and above will fix this.

## Add new method

dfcbenchmarker tests 5 different methods.

Let us say that, for some reason a think $(x_1 + x_2)^3$ is a good estimate for the relationship between $x_1$ and $x_2$. This will be the method we benchmark against everything else.

```
import numpy as np
def power3(x1,x2,params):
return np.power(x1*x2,3)
```

*This is to be completed soon*

## Send method

*This is to be completed soon*

There are then a couple of questions, such as email address, name, DOIs/pmids of relevant publications which should be cited when reporting the method etc.  Then there are a number of questions to approve (e.g. everything is sent via a Google form). If you do not want to approve of things going via Google, you can just send it to me over Github/email (see article). You also have to approve that dfcbenchmarker can use the code in future version. You can also decide if you want your code to be included in [teneto](github.com/wiheto/teneto) (which is my python package for temporal network/dynamic connectivity).  

Once I've looked at the code, I will send you an email and confirm it works. If I've not sent an email after 1-2 weeks, please let me know (just in case something may break with the Google form method).

## Custom parameter file

*This is to be completed soon*

## Problems/comments?

Leave an issue here.
