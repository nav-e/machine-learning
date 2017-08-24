import os
import sys
import h5py
import numpy
path = os.environ.get('TAXI_PATH', '/home/saumya/Downloads/gsoc/route_prediction/data')
Polyline = h5py.special_dtype(vlen=numpy.float32)
stands_size = 64
taxi_id_size = 448 
train_gps_mean = numpy.array([41.1573, -8.61612], dtype=numpy.float32)
train_gps_std = numpy.sqrt(numpy.array([0.00549598, 0.00333233], dtype=numpy.float32))
tvt = '--tvt' in sys.argv
if tvt:
    test_size = 19770
    valid_size = 19427
    train_size = 1671473
    origin_call_size = 57106
    origin_call_train_size = 57106
    valid_set = 'valid'
    valid_ds = 'tvt.hdf5'
    traintest_ds = 'tvt.hdf5'
else:
    test_size = 320 
    train_size = 1710670 
    origin_call_size = 57125
    origin_call_train_size = 57106
    if '--largevalid' in sys.argv:
        valid_set = 'cuts/large_cut'
    else:
        valid_set = 'cuts/test0'
    valid_ds = 'valid.hdf5'
    traintest_ds = 'data.hdf5'
