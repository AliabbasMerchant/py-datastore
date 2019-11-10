"""
datastore is a generic layer of abstraction for data store and database access.
It is a **simple** API with the aim to enable application development in a
datastore-agnostic way, allowing datastores to be swapped seamlessly without
changing application code. Thus, one can leverage different datastores with
different strengths without committing the application to one datastore
throughout its lifetime.
"""

__version__ = '0.3.6'
__author__ = 'Juan Batiz-Benet, Alexander Schlarb'
__email__ = 'juan@benet.ai, alexander@ninetailed.ninja'

# import key
from .key import Key
from .key import Namespace

# import basic
from .basic import Datastore
from .basic import NullDatastore
from .basic import DictDatastore

from .basic import ShimDatastore
from .basic import LoggingDatastore
from .basic import KeyTransformDatastore
from .basic import LowercaseKeyDatastore
from .basic import NamespaceDatastore
from .basic import NestedPathDatastore
from .basic import DirectoryTreeDatastore
from .basic import DirectoryDatastore

from .basic import DatastoreCollection
from .basic import ShardedDatastore
from .basic import TieredDatastore

# import query
from .query import Query
from .query import Cursor

# import serialize
from .serialize import SerializerShimDatastore
