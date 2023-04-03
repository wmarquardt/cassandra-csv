[![code-style](https://img.shields.io/badge/codestyle-black-black)](https://github.com/psf/black)

# Cassandra CSV
Python package to export cassandra query result to CSV format.
Cassandra `COPY` function does not export data with **WHERE** clause. If you need to export cassandra query result to CSV format, just read the documentation below.

## Install
```shell
$ pip install cassandra-csv
```

## Usage
```python
from cassandra.cluster import Cluster
from cassandracsv import CassandraCsv

cluster = Cluster()
cassandra_cluster = cluster.connect('database')

result = cassandra_cluster.execute("""SELECT foo FROM bar WHERE foobar=2""")


CassandraCsv.export(
    result,
    [options]
)
```

## Options
|Name| Type | Default |  Description |
|--|--|--|--|
| **max_file_size** | int | 0 | max CSV file size (lines) the file will be splitted until complete entire resultset. Use 0 to export all result to just one file |
| **output_dir** | string | /tmp | full output path
| **filename** | string | export_file | file name (without extension)
| **separator** | string | , | string separator
| **with_header** | boolean | True | show file header (field name or alias, added direct on select using `as`)
| **create_subfolder** | boolean | False | create sulfolder to store files.
