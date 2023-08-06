# SBA

Untility functions for interaction classifcation.

# Installation

```bash
pip install SBAUtil
```

# Tutorial

```python
import SBA
```

Initalize the configuration file:
```python
SBA.initConfig('./',projectName = "newProject", experimenter = "Yiyang")
```

### dynamic cut

[SIMBA gives error](https://github.com/sgoldenlab/simba/blob/master/docs/FAQ.md#3-i-get-a-qhull-eg-qh6154-or-6013-error-when-extracting-the-features) if the h5file input from DLC contains a portion where there is only one mouse.  `SBA.batch_dynamic_cropVideo` will dynamically crop out this portion based on the given h5file from DLC. 

```python
SBA.batch_dynamic_cropVideo(config_path,videos,h5files,fps,videoType="avi")
```


### Post SIMBA processing

```python
SBA.finalizeSimBaOutput(config, simbaFiles, classifier ,destDir = None)
```

TODO: a more detailed tutorial; better interface;
  
