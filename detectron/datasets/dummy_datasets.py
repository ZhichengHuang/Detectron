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
        '__background__', '24', '133',  '67',   '134',  '123',  '135',  '129',  '128',  '127',  '88',   '92',   '16',   '87',   '34',  '82',  '26',  '7',   '98',   '44',   '61',   '41',   '117',   '62',  '75',  '74',  '9',   '17',   '49',   '108',  '54',  '96',  '2',   '18',  '43',  '29',  '3',   '120',  '45',  '33',
  '6',   '110',  '80',   '65',   '66',   '83',   '32',   '71',   '68',   '78',   '51',   '93',   '58', '25',  '104',  '106',  '21',  '12',  '14',  '79',  '77',  '31',
  '91',  '4',   '132',  '89',  '8',   '20',   '73',   '38',   '37',   '70',   '95',   '35',   '52',   '48',   '105',
  '57',   '53',   '19',   '23',   '112',  '55',   '63',   '64',   '30',   '28',   '13',   '56',   '69',   '131',  '94',   '119',  '42',   '15',   '86',   '39',   '118',  '72',  '5',   '124',  '115',  '10',   '81',   '90',  '47', '60', '116',  '76',   '121',  '122',  '22',   '11',   '113',  '46',   '36',   '99',   '107',  '97',   '114',  '27',   '85',   '100',   '109', '59', '50', '103', '111', '101']
    ds.classes = {i: name for i, name in enumerate(classes)}
    return ds
