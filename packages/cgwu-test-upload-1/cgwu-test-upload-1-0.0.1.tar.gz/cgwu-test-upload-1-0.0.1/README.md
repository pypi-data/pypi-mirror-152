# Aqueduct Python SDK
The Python SDK allows you to easily preview and register your workflows to the cluster.

## Installing the SDK
Python 3.8 or 3.9 is required.

Clone this repository and run `python3 setup.py install`. Note that if you
would like to install this library in your global Python packages, you will
need to run `sudo python3 setup.py install --prefix=/usr/local`. 

To develop locally run `python3 setup.py develop` in the root of the package.

## Example usage

The example below show how to connect to your Aqueduct Cluster using the
Aqueduct Python SDK.


```
import aqueduct
client = aqueduct.Client("<your_api_key>", "<your_server_address>")

postgres_integration = client.integration(name="aqueduct_demo")
sql_artifact = integration.sql(query="SELECT * from customers;")
fn_artifact = log_featurize(sql_artifact)
fn_artifact.save(postgres_integration.config(table='features', update_mode='replace'))

flow = client.create_flow(name="test", artifacts=[fn_artifact])
flow.test()

flow.publish(schedule=aqueduct.daily())
```

For a more full-featured example, you can see the [churn ensemble
workflow](https://github.com/aqueducthq/aqueduct-python/blob/main/examples/churn_prediction/ensemble-workflow.ipynb).
