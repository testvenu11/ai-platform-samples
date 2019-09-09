# Copyright 2019 Google LLC. All Rights Reserved.
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
# ==============================================================================

"""Dataset metadata."""

# If the input CSV file has a header row, then set CSV_COLUMNS to None.
# Otherwise, set CSV_COLUMNS to a list of target and feature names:
CSV_COLUMNS = None

# Target name
TARGET_NAME = 'tip'

# The features to be used for training.
# If FEATURE_NAMES is None, then all the available columns will be
# used as features, except for the target column.
FEATURE_NAMES = None

# If the model is serialized using joblib
# then use 'model.joblib' for the model name
MODEL_FILE_NAME = 'model.joblib'

# Set to True if you want to tune some hyperparameters
HYPERPARAMTER_TUNING = False

# Used only if the dataset is to be read from BigQuery
BASE_QUERY = '''
    SELECT
      *
    FROM
      `{table}`
  '''
