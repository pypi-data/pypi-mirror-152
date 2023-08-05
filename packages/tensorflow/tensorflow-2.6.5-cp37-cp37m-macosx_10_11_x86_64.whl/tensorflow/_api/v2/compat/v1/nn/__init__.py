# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""Primitive Neural Net (NN) Operations.

## Notes on padding

Several neural network operations, such as `tf.nn.conv2d` and
`tf.nn.max_pool2d`, take a `padding` parameter, which controls how the input is
padded before running the operation. The input is padded by inserting values
(typically zeros) before and after the tensor in each spatial dimension. The
`padding` parameter can either be the string `'VALID'`, which means use no
padding, or `'SAME'` which adds padding according to a formula which is
described below. Certain ops also allow the amount of padding per dimension to
be explicitly specified by passing a list to `padding`.

In the case of convolutions, the input is padded with zeros. In case of pools,
the padded input values are ignored. For example, in a max pool, the sliding
window ignores padded values, which is equivalent to the padded values being
`-infinity`.

### `'VALID'` padding

Passing `padding='VALID'` to an op causes no padding to be used. This causes the
output size to typically be smaller than the input size, even when the stride is
one. In the 2D case, the output size is computed as:

```
out_height = ceil((in_height - filter_height + 1) / stride_height)
out_width  = ceil((in_width - filter_width + 1) / stride_width)
```

The 1D and 3D cases are similar. Note `filter_height` and `filter_width` refer
to the filter size after dilations (if any) for convolutions, and refer to the
window size for pools.

### `'SAME'` padding

With `'SAME'` padding, padding is applied to each spatial dimension. When the
strides are 1, the input is padded such that the output size is the same as the
input size. In the 2D case, the output size is computed as:

```
out_height = ceil(in_height / stride_height)
out_width  = ceil(in_width / stride_width)
```

The amount of padding used is the smallest amount that results in the output
size. The formula for the total amount of padding per dimension is:

```
if (in_height % strides[1] == 0):
  pad_along_height = max(filter_height - stride_height, 0)
else:
  pad_along_height = max(filter_height - (in_height % stride_height), 0)
if (in_width % strides[2] == 0):
  pad_along_width = max(filter_width - stride_width, 0)
else:
  pad_along_width = max(filter_width - (in_width % stride_width), 0)
```

Finally, the padding on the top, bottom, left and right are:

```
pad_top = pad_along_height // 2
pad_bottom = pad_along_height - pad_top
pad_left = pad_along_width // 2
pad_right = pad_along_width - pad_left
```

Note that the division by 2 means that there might be cases when the padding on
both sides (top vs bottom, right vs left) are off by one. In this case, the
bottom and right sides always get the one additional padded pixel. For example,
when pad_along_height is 5, we pad 2 pixels at the top and 3 pixels at the
bottom. Note that this is different from existing libraries such as PyTorch and
Caffe, which explicitly specify the number of padded pixels and always pad the
same number of pixels on both sides.

Here is an example of `'SAME'` padding:

>>> in_height = 5
>>> filter_height = 3
>>> stride_height = 2
>>>
>>> in_width = 2
>>> filter_width = 2
>>> stride_width = 1
>>>
>>> inp = tf.ones((2, in_height, in_width, 2))
>>> filter = tf.ones((filter_height, filter_width, 2, 2))
>>> strides = [stride_height, stride_width]
>>> output = tf.nn.conv2d(inp, filter, strides, padding='SAME')
>>> output.shape[1]  # output_height: ceil(5 / 2)
3
>>> output.shape[2] # output_width: ceil(2 / 1)
2

### Explicit padding

Certain ops, like `tf.nn.conv2d`, also allow a list of explicit padding amounts
to be passed to the `padding` parameter. This list is in the same format as what
is passed to `tf.pad`, except the padding must be a nested list, not a tensor.
For example, in the 2D case, the list is in the format `[[0, 0], [pad_top,
pad_bottom], [pad_left, pad_right], [0, 0]]` when `data_format` is its default
value of `'NHWC'`. The two `[0, 0]` pairs  indicate the batch and channel
dimensions have no padding, which is required, as only spatial dimensions can
have padding.

For example:

>>> inp = tf.ones((1, 3, 3, 1))
>>> filter = tf.ones((2, 2, 1, 1))
>>> strides = [1, 1]
>>> padding = [[0, 0], [1, 2], [0, 1], [0, 0]]
>>> output = tf.nn.conv2d(inp, filter, strides, padding=padding)
>>> tuple(output.shape)
(1, 5, 3, 1)
>>> # Equivalently, tf.pad can be used, since convolutions pad with zeros.
>>> inp = tf.pad(inp, padding)
>>> # 'VALID' means to use no padding in conv2d (we already padded inp)
>>> output2 = tf.nn.conv2d(inp, filter, strides, padding='VALID')
>>> tf.debugging.assert_equal(output, output2)

"""

from __future__ import print_function as _print_function

import sys as _sys

from . import rnn_cell
from tensorflow.python.ops.array_ops import depth_to_space
from tensorflow.python.ops.array_ops import space_to_batch
from tensorflow.python.ops.array_ops import space_to_depth
from tensorflow.python.ops.candidate_sampling_ops import all_candidate_sampler
from tensorflow.python.ops.candidate_sampling_ops import compute_accidental_hits
from tensorflow.python.ops.candidate_sampling_ops import fixed_unigram_candidate_sampler
from tensorflow.python.ops.candidate_sampling_ops import learned_unigram_candidate_sampler
from tensorflow.python.ops.candidate_sampling_ops import log_uniform_candidate_sampler
from tensorflow.python.ops.candidate_sampling_ops import uniform_candidate_sampler
from tensorflow.python.ops.ctc_ops import collapse_repeated
from tensorflow.python.ops.ctc_ops import ctc_beam_search_decoder
from tensorflow.python.ops.ctc_ops import ctc_beam_search_decoder_v2
from tensorflow.python.ops.ctc_ops import ctc_greedy_decoder
from tensorflow.python.ops.ctc_ops import ctc_loss
from tensorflow.python.ops.ctc_ops import ctc_loss_v2
from tensorflow.python.ops.ctc_ops import ctc_unique_labels
from tensorflow.python.ops.embedding_ops import embedding_lookup
from tensorflow.python.ops.embedding_ops import embedding_lookup_sparse
from tensorflow.python.ops.embedding_ops import safe_embedding_lookup_sparse
from tensorflow.python.ops.gen_math_ops import tanh
from tensorflow.python.ops.gen_nn_ops import conv3d_backprop_filter_v2
from tensorflow.python.ops.gen_nn_ops import conv3d_backprop_filter_v2 as conv3d_backprop_filter
from tensorflow.python.ops.gen_nn_ops import elu
from tensorflow.python.ops.gen_nn_ops import l2_loss
from tensorflow.python.ops.gen_nn_ops import lrn
from tensorflow.python.ops.gen_nn_ops import lrn as local_response_normalization
from tensorflow.python.ops.gen_nn_ops import quantized_avg_pool
from tensorflow.python.ops.gen_nn_ops import quantized_conv2d
from tensorflow.python.ops.gen_nn_ops import quantized_max_pool
from tensorflow.python.ops.gen_nn_ops import quantized_relu_x
from tensorflow.python.ops.gen_nn_ops import relu
from tensorflow.python.ops.gen_nn_ops import selu
from tensorflow.python.ops.gen_nn_ops import softsign
from tensorflow.python.ops.math_ops import sigmoid
from tensorflow.python.ops.math_ops import softplus
from tensorflow.python.ops.nn_impl import batch_norm_with_global_normalization
from tensorflow.python.ops.nn_impl import batch_normalization
from tensorflow.python.ops.nn_impl import compute_average_loss
from tensorflow.python.ops.nn_impl import depthwise_conv2d
from tensorflow.python.ops.nn_impl import fused_batch_norm
from tensorflow.python.ops.nn_impl import l2_normalize
from tensorflow.python.ops.nn_impl import log_poisson_loss
from tensorflow.python.ops.nn_impl import moments
from tensorflow.python.ops.nn_impl import nce_loss
from tensorflow.python.ops.nn_impl import normalize_moments
from tensorflow.python.ops.nn_impl import relu_layer
from tensorflow.python.ops.nn_impl import sampled_softmax_loss
from tensorflow.python.ops.nn_impl import scale_regularization_loss
from tensorflow.python.ops.nn_impl import separable_conv2d
from tensorflow.python.ops.nn_impl import sigmoid_cross_entropy_with_logits
from tensorflow.python.ops.nn_impl import sufficient_statistics
from tensorflow.python.ops.nn_impl import swish
from tensorflow.python.ops.nn_impl import swish as silu
from tensorflow.python.ops.nn_impl import weighted_cross_entropy_with_logits
from tensorflow.python.ops.nn_impl import weighted_moments
from tensorflow.python.ops.nn_impl import zero_fraction
from tensorflow.python.ops.nn_ops import atrous_conv2d
from tensorflow.python.ops.nn_ops import atrous_conv2d_transpose
from tensorflow.python.ops.nn_ops import avg_pool
from tensorflow.python.ops.nn_ops import avg_pool as avg_pool2d
from tensorflow.python.ops.nn_ops import avg_pool1d
from tensorflow.python.ops.nn_ops import avg_pool3d
from tensorflow.python.ops.nn_ops import avg_pool_v2
from tensorflow.python.ops.nn_ops import bias_add
from tensorflow.python.ops.nn_ops import conv1d
from tensorflow.python.ops.nn_ops import conv1d_transpose
from tensorflow.python.ops.nn_ops import conv2d
from tensorflow.python.ops.nn_ops import conv2d_backprop_filter
from tensorflow.python.ops.nn_ops import conv2d_backprop_input
from tensorflow.python.ops.nn_ops import conv2d_transpose
from tensorflow.python.ops.nn_ops import conv3d_transpose
from tensorflow.python.ops.nn_ops import conv3d_v1 as conv3d
from tensorflow.python.ops.nn_ops import conv_transpose
from tensorflow.python.ops.nn_ops import convolution
from tensorflow.python.ops.nn_ops import crelu
from tensorflow.python.ops.nn_ops import depthwise_conv2d_native
from tensorflow.python.ops.nn_ops import depthwise_conv2d_native_backprop_filter
from tensorflow.python.ops.nn_ops import depthwise_conv2d_native_backprop_filter as depthwise_conv2d_backprop_filter
from tensorflow.python.ops.nn_ops import depthwise_conv2d_native_backprop_input
from tensorflow.python.ops.nn_ops import depthwise_conv2d_native_backprop_input as depthwise_conv2d_backprop_input
from tensorflow.python.ops.nn_ops import dilation2d_v1 as dilation2d
from tensorflow.python.ops.nn_ops import dropout
from tensorflow.python.ops.nn_ops import erosion2d
from tensorflow.python.ops.nn_ops import fractional_avg_pool
from tensorflow.python.ops.nn_ops import fractional_max_pool
from tensorflow.python.ops.nn_ops import in_top_k
from tensorflow.python.ops.nn_ops import leaky_relu
from tensorflow.python.ops.nn_ops import log_softmax
from tensorflow.python.ops.nn_ops import max_pool
from tensorflow.python.ops.nn_ops import max_pool1d
from tensorflow.python.ops.nn_ops import max_pool2d
from tensorflow.python.ops.nn_ops import max_pool3d
from tensorflow.python.ops.nn_ops import max_pool_v2
from tensorflow.python.ops.nn_ops import max_pool_with_argmax_v1 as max_pool_with_argmax
from tensorflow.python.ops.nn_ops import pool
from tensorflow.python.ops.nn_ops import relu6
from tensorflow.python.ops.nn_ops import softmax
from tensorflow.python.ops.nn_ops import softmax_cross_entropy_with_logits
from tensorflow.python.ops.nn_ops import softmax_cross_entropy_with_logits_v2_helper as softmax_cross_entropy_with_logits_v2
from tensorflow.python.ops.nn_ops import sparse_softmax_cross_entropy_with_logits
from tensorflow.python.ops.nn_ops import top_k
from tensorflow.python.ops.nn_ops import with_space_to_batch
from tensorflow.python.ops.nn_ops import xw_plus_b
from tensorflow.python.ops.rnn import bidirectional_dynamic_rnn
from tensorflow.python.ops.rnn import dynamic_rnn
from tensorflow.python.ops.rnn import raw_rnn
from tensorflow.python.ops.rnn import static_bidirectional_rnn
from tensorflow.python.ops.rnn import static_rnn
from tensorflow.python.ops.rnn import static_state_saving_rnn

del _print_function
