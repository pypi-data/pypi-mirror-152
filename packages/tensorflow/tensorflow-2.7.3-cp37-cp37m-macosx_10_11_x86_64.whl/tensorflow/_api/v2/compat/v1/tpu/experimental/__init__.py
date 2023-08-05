# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""Public API for tf.tpu.experimental namespace.
"""

from __future__ import print_function as _print_function

import sys as _sys

from . import embedding
from tensorflow.python.tpu.device_assignment import DeviceAssignment
from tensorflow.python.tpu.feature_column_v2 import embedding_column_v2 as embedding_column
from tensorflow.python.tpu.feature_column_v2 import shared_embedding_columns_v2 as shared_embedding_columns
from tensorflow.python.tpu.topology import Topology
from tensorflow.python.tpu.tpu_embedding import AdagradParameters
from tensorflow.python.tpu.tpu_embedding import AdamParameters
from tensorflow.python.tpu.tpu_embedding import FtrlParameters
from tensorflow.python.tpu.tpu_embedding import StochasticGradientDescentParameters
from tensorflow.python.tpu.tpu_strategy_util import initialize_tpu_system
from tensorflow.python.tpu.tpu_strategy_util import shutdown_tpu_system
from tensorflow.python.tpu.tpu_system_metadata import TPUSystemMetadata

del _print_function
