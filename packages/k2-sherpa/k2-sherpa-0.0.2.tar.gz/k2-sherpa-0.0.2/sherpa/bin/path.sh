#!/usr/bin/env python3

export CUDA_VISIBLE_DEVICES="0,2"

icefall_path=/ceph-fj/fangjun/open-source-2/icefall-master-3
lhotse_path=/ceph-fj/fangjun/open-source-2/lhotse-master
k2_path=/ceph-fj/fangjun/open-source-2/k2-multi-22
ot_path=/ceph-fj/fangjun/open-source-2/optimized_transducer-rnnt-ali
kaldilm_path=/ceph-fj/fangjun/open-source-2/kaldilm_path
kaldifeat_path=/ceph-fj/fangjun/open-source-2/kaldifeat-2
sherpa_path=/ceph-fj/fangjun/open-source-2/sherpa

function add_path() {
  export PYTHONPATH="$1":${PYTHONPATH}
}

export PATH=$lhotse_path/lhotse/bin:$PATH
add_path $icefall_path
add_path $lhotse_path
add_path $k2_path/k2/python
add_path $k2_path/build-cuda/lib
add_path $ot_path/optimized_transducer/python
add_path $ot_path/build/lib
add_path $kaldilm_path/kaldilm/python
add_path $kaldilm_path/build

add_path $kaldifeat_path/kaldifeat/python
add_path $kaldifeat_path/b2/lib

add_path $sherpa_path/sherpa/python
add_path $sherpa_path/build/lib
