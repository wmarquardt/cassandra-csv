# Cassandra CSV
Python package to export cassandra query result to CSV format.
Cassandra `COPY` function does not export data with **WHERE** condition. If you need to export cassandra query result to CSV format, just read the documentation below.

## Install
```shell
    $ pip install cassandra-csv
```

## Usage
```python
     from cassandracsv import CassandraCsv
	 result = cassandra_cluster.execute("SELECT foo FROM bar WHERE foobar=2")
	
	 CassandraCsv.export(
		result,
     )
```

## Options
|Parameter| type | description |
|--|--|--|
|  |  |  |
