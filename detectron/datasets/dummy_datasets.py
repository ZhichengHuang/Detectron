# Copyright (c) 2017-present, Facebook, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##############################################################################
"""Provide stub objects that can act as stand-in "dummy" datasets for simple use
cases, like getting all classes in a dataset. This exists so that demos can be
run without requiring users to download/install datasets first.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from detectron.utils.collections import AttrDict


def get_coco_dataset():
    """A dummy COCO dataset that includes only the 'classes' field."""
    ds = AttrDict()
    classes = [
        '__background__', '110',
 '71',
 '127',
 '134',
 '132',
 '30',
 '120',
 '121',
 '28',
 '1',
 '128',
 '129',
 '2',
 '3',
 '87',
 '23',
 '7',
 '14',
 '92',
 '4',
 '123',
 '76',
 '66',
 '98',
 '22',
 '50',
 '6',
 '74',
 '51',
 '81',
 '53',
 '95',
 '114',
 '72',
 '133',
 '17',
 '15',
 '41',
 '131',
 '122',
 '11',
 '47',
 '75',
 '54',
 '58',
 '78',
 '137',
 '35',
 '38',
 '85',
 '65',
 '79',
 '49',
 '20',
 '52',
 '33',
 '139',
 '24',
 '138',
 '140',
 '68',
 '57',
 '13',
 '141',
 '25',
 '105',
 '48',
 '64',
 '5',
 '73',
 '86',
 '19',
 '34',
 '12',
 '89',
 '62',
 '67',
 '63',
 '61',
 '60',
 '45',
 '107',
 '77',
 '115',
 '82',
 '9',
 '142',
 '104',
 '16',
 '135']
    ds.classes = {i: name for i, name in enumerate(classes)}
    return ds
