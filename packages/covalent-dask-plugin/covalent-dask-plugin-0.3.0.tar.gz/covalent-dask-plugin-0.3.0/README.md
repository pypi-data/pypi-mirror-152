&nbsp;

<div align="center">

<img src="https://raw.githubusercontent.com/AgnostiqHQ/covalent/master/doc/source/_static/covalent_readme_banner.svg" width=150%>

&nbsp;

</div>

## Covalent Dask Plugin

Covalent is a Pythonic workflow tool used to execute tasks on advanced computing hardware. The way in which workflows and tasks interface with the hardware is through executor plugins, such as the local executor packaged with core Covalent. The Dask executor plugin interfaces with a running [Dask Cluster](https://docs.dask.org/en/latest/deploying.html). Users can deploy tasks to the cluster by providing the scheduler address to the executor object. For more information about how to get started with Covalent, check out the project [homepage](https://github.com/AgnostiqHQ/covalent) and the official [documentation](https://covalent.readthedocs.io/en/latest/).

To install this plugin with Covalent

* Using `pip`:

```bash
pip install covalent-dask-plugin
```

* Using this repo for development purposes:

```bash
git clone https://github.com/AgnostiqHQ/covalent-dask-plugin.git

cd covalent-dask-plugin

pip install -e .
```

After this package has been installed, run the following to start a Dask cluster with Python and retrieve the scheduler address:

```python
from dask.distributed import LocalCluster

cluster = LocalCluster()
print(cluster.scheduler_address)
```

The address will look like `tcp://127.0.0.1:55564` when running locally. Note that the Dask cluster does not persist when the process terminates.

This cluster can be used with Covalent by providing the scheduler address:

```python
import covalent as ct

dask_executor = ct.executor.DaskExecutor(
                    scheduler_address="tcp://127.0.0.1:55564"
                )

@ct.electron(executor=dask_executor)
def my_custom_task(x, y):
    return x + y

...
```

For more information about how to get started with Covalent, check out the project [homepage](https://github.com/AgnostiqHQ/covalent) and the official [documentation](https://covalent.readthedocs.io/en/latest/).

## Release Notes

Release notes are available in the [Changelog](https://github.com/AgnostiqHQ/covalent-dask-plugin/blob/develop/CHANGELOG.md).

## Citation

Please use the following citation in any publications:

> W. J. Cunningham, S. K. Radha, F. Hasan, J. Kanem, S. W. Neagle, and S. Sanand.
> *Covalent.* Zenodo, 2022. https://doi.org/10.5281/zenodo.5903364

## License

Covalent is licensed under the GNU Affero GPL 3.0 License. Covalent may be distributed under other licenses upon request. See the [LICENSE](https://github.com/AgnostiqHQ/covalent-dask-plugin/blob/develop/LICENSE) file or contact the [support team](mailto:support@agnostiq.ai) for more details.
