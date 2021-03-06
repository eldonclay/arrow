# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# flake8: noqa

from pkg_resources import get_distribution, DistributionNotFound
try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
   # package is not installed
   pass


from pyarrow.lib import cpu_count, set_cpu_count
from pyarrow.lib import (null, bool_,
                         int8, int16, int32, int64,
                         uint8, uint16, uint32, uint64,
                         time32, time64, timestamp, date32, date64,
                         float16, float32, float64,
                         binary, string, decimal,
                         list_, struct, dictionary, field,
                         Field,
                         Schema,
                         schema,
                         Array, Tensor,
                         array,
                         from_numpy_dtype,
                         NullArray,
                         NumericArray, IntegerArray, FloatingPointArray,
                         BooleanArray,
                         Int8Array, UInt8Array,
                         Int16Array, UInt16Array,
                         Int32Array, UInt32Array,
                         Int64Array, UInt64Array,
                         ListArray,
                         BinaryArray, StringArray,
                         FixedSizeBinaryArray,
                         DictionaryArray,
                         Date32Array, Date64Array,
                         TimestampArray, Time32Array, Time64Array,
                         DecimalArray, StructArray,
                         ArrayValue, Scalar, NA,
                         BooleanValue,
                         Int8Value, Int16Value, Int32Value, Int64Value,
                         UInt8Value, UInt16Value, UInt32Value, UInt64Value,
                         FloatValue, DoubleValue, ListValue,
                         BinaryValue, StringValue, FixedSizeBinaryValue,
                         DecimalValue,
                         Date32Value, Date64Value, TimestampValue)

from pyarrow.lib import (HdfsFile, NativeFile, PythonFile,
                         Buffer, BufferReader, BufferOutputStream,
                         OSFile, MemoryMappedFile, memory_map,
                         frombuffer, read_tensor, write_tensor,
                         memory_map, create_memory_map,
                         get_record_batch_size, get_tensor_size,
                         have_libhdfs, have_libhdfs3)

from pyarrow.lib import (MemoryPool, total_allocated_bytes,
                         set_memory_pool, default_memory_pool)
from pyarrow.lib import (ChunkedArray, Column, RecordBatch, Table,
                         concat_tables)
from pyarrow.lib import (ArrowException,
                         ArrowKeyError,
                         ArrowInvalid,
                         ArrowIOError,
                         ArrowMemoryError,
                         ArrowNotImplementedError,
                         ArrowTypeError)


from pyarrow.filesystem import Filesystem, HdfsClient, LocalFilesystem

from pyarrow.ipc import (RecordBatchFileReader, RecordBatchFileWriter,
                         RecordBatchStreamReader, RecordBatchStreamWriter,
                         open_stream,
                         open_file,
                         serialize_pandas, deserialize_pandas)


localfs = LocalFilesystem.get_instance()


# ----------------------------------------------------------------------
# 0.4.0 deprecations

import warnings

def _deprecate_class(old_name, new_name, klass, next_version='0.5.0'):
    msg = ('pyarrow.{0} has been renamed to '
           '{1}, will be removed in {2}'
           .format(old_name, new_name, next_version))
    def deprecated_factory(*args, **kwargs):
        warnings.warn(msg, FutureWarning)
        return klass(*args)
    return deprecated_factory

FileReader = _deprecate_class('FileReader',
                              'RecordBatchFileReader',
                              RecordBatchFileReader, '0.5.0')

FileWriter = _deprecate_class('FileWriter',
                              'RecordBatchFileWriter',
                              RecordBatchFileWriter, '0.5.0')

StreamReader = _deprecate_class('StreamReader',
                                'RecordBatchStreamReader',
                                RecordBatchStreamReader, '0.5.0')

StreamWriter = _deprecate_class('StreamWriter',
                                'RecordBatchStreamWriter',
                                RecordBatchStreamWriter, '0.5.0')

InMemoryOutputStream = _deprecate_class('InMemoryOutputStream',
                                        'BufferOutputStream',
                                        BufferOutputStream, '0.5.0')
