# Copyright 2019 Novartis Institutes for BioMedical Research Inc. Licensed
# under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License. You may obtain a copy
# of the License at http://www.apache.org/licenses/LICENSE-2.0. Unless
# required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for
# the specific language governing permissions and limitations under the License.

import os

from flask_api import status

from cellxgene_gateway import env
from cellxgene_gateway.cellxgene_exception import CellxgeneException

annotations_dirname = "annotations"
data_dirname = "data"
h5ad_suffix = ".h5ad"


def make_h5ad(el):
    el.replace(f"/{annotations_dirname}/", f"/{data_dirname}/", 1)

    return el + h5ad_suffix


def make_annotations(el):
    el.replace(f"/{data_dirname}/", f"/{annotations_dirname}/", 1)

    return el[: -len(h5ad_suffix)]


def ensure_dir_exists(file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)
