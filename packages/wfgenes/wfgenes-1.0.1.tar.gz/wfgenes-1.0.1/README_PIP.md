

<img src="fig/wfgenes_logo.png" width="200">

### Preparing pip package:

Install a project in editable mode (i.e. setuptools "develop mode") from a local project path or a VCS url. In order to complete the first step and prepare local pip package, the setup.cfg file is needed [1].   

    pip install --use-feature=in-tree-build e .



Afterwards, steps in [2] should be completed to prepare and publish the package. 





[1]: https://setuptools.pypa.io/en/latest/userguide/declarative_config.html
[2]: https://packaging.python.org/en/latest/tutorials/packaging-projects/
[3]: https://jwodder.github.io/kbits/posts/pypkg-data/