# hive-udf

Hive UDF (user-defined functions) in Python.

This package provides a single function `make_udf` for
working with Hive UDF written in Python.

Some test code is included, along with several example UDF modules, which are used in the tests. The user is recommended to run these tests in their Hive setup to confirm that things work as expected.

## Status

Production ready and stable (hardly needs any changes).

## Quick start

Install `hive-udf` via `pip`:

```
$ pip install hive-udf
```

Suppose you have a Hive UDF as Python module `mypackage.udfs.udf`,
then insert this UDF into your HiveQL statement as follows

```
from hive_udf import make_udf
import mypackage.udfs.udf

s = make_udf(mypackage.udfs.udf)

sql = f"""
    SELECT
        TRANSFORM ( ...input_columns... )
        USING '{s}'
        AS (...output_columns...)
    FROM {db_name}.{table_name}
    WHERE ...
```

Then use `sql` in your Hive client Python code. Some Hive client packages exist, including [PyHive](https://github.com/dropbox/PyHive), [pyodbc](https://github.com/mkleehammer/pyodbc), [turbodbc](https://github.com/blue-yonder/turbodbc), and [impyla](https://github.com/cloudera/impyla).

Please see the source code for documentation.

[This blog post](https://zpz.github.io/blog/hive-udf/) describes how the code arrived at the current shape after addressing multiple very tricky problems. If you want to understand the code, please read this post.
