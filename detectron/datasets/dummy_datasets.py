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
        '__background__', '24',
 '19',
 '129',
 '127',
 '133',
 '135',
 '104',
 '105',
 '67',
 '20',
 '131',
 '134',
 '95',
 '5',
 '98',
 '132',
 '123',
 '121',
 '88',
 '87',
 '63',
 '62',
 '106',
 '128',
 '73',
 '75',
 '12',
 '82',
 '26',
 '32',
 '79',
 '74',
 '90',
 '92',
 '93',
 '16',
 '13',
 '34',
 '39',
 '70',
 '68',
 '29',
 '31',
 '49',
 '53',
 '81',
 '25',
 '59',
 '58',
 '10',
 '9',
 '7',
 '3',
 '119',
 '28',
 '56',
 '44',
 '61',
 '41',
 '4',
 '112',
 '116',
 '117',
 '118',
 '122',
 '78',
 '17',
 '21',
 '108',
 '110',
 '54',
 '96',
 '77',
 '2',
 '18',
 '22',
 '43',
 '52',
 '47',
 '97',
 '109',
 '120',
 '45',
 '33',
 '60',
 '6',
 '80',
 '65',
 '99',
 '100',
 '72',
 '66',
 '71',
 '83',
 '48',
 '36',
 '8',
 '30',
 '76',
 '51',
 '15',
 '27',
 '107',
 '14',
 '85',
 '55',
 '50',
 '1',
 '35',
 '37',
 '23',
 '64',
 '42',
 '57',
 '91',
 '89',
 '86',
 '94',
 '38',
 '111',
 '69',
 '46',
 '113',
 '115',
 '124',
 '114',
 '11',
 '103',
 '102',
 '101']
    ds.classes = {i: name for i, name in enumerate(classes)}
    return ds
