#!/bin/bash

set -e

conda create -n binf690 python=3.6 -y
conda activate binf690

cd $(dirname $0)
pip install -r requirements.txt
pip install -e .
