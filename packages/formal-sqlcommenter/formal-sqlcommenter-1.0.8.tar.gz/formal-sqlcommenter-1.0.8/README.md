![PyPI - Python Version](https://img.shields.io/pypi/pyversions/formal-sqlcommenter)

# Formal sqlcommenter

Formal sqlcommenter is a plugin that enables your ORMs to augment SQL statement before execution, with a comment containing the end-user id of a request.
Sqlcommenter is typically useful for back-office application that needs to implement role access management.

 * [Psycopg2](#psycopg2)
 * [Django](#django)

## Local Install

```shell
pip3 install --user formal-sqlcommenter
```

## Usage

### Psycopg2

Use the provided cursor factory to generate database cursors. All queries executed with such cursors will have the SQL comment prepended to them.

```python
import psycopg2
from formal.sqlcommenter.psycopg2.extension import CommenterCursorFactory

cursor_factory = CommenterCursorFactory()
conn = psycopg2.connect(..., cursor_factory=cursor_factory)
cursor = conn.cursor()
cursor.execute('SELECT * from ...', '1234') # comment will be added before execution
```

which will produce a backend log such as when viewed on Postgresql
```shell
2019-05-28 02:33:25.287 PDT [57302] LOG:  statement: /*formal_role_id:1234*/ SELECT * FROM
polls_question 
```


### Django

Add the provided Django middleware to your Django project's settings. All database queries executed by authenticated users within the standard request→response cycle will have a SQL comment prepended to them. The comment will inform Formal systems that the querying user has the External ID with a value of `request.user.email`, or if that does not exist, `request.user.id`.

```python
MIDDLEWARE = [
+  'formal.sqlcommenter.django.databaseInstrumentation.FormalSqlCommenter',
  ...
]
```

