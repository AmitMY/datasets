# coding=utf-8
# Copyright 2020 The HuggingFace Datasets Authors and the current dataset script contributor.
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
"""Precision metric."""

from sklearn.metrics import precision_score

import datasets


_DESCRIPTION = """
Precision is the fraction of the true examples among the predicted examples. It can be computed with:
Precision = TP / (TP + FP)
TP: True positive
FP: False positive
"""

_KWARGS_DESCRIPTION = """
Args:
    predictions: Ground truth labels.
    references: Predicted labels, as returned by a model.
    labels: The set of labels to include when average != 'binary', and
        their order if average is None. Labels present in the data can
        be excluded, for example to calculate a multiclass average ignoring
        a majority negative class, while labels not present in the data will
        result in 0 components in a macro average. For multilabel targets,
        labels are column indices. By default, all labels in y_true and
        y_pred are used in sorted order.
    average: This parameter is required for multiclass/multilabel targets.
        If None, the scores for each class are returned. Otherwise, this
        determines the type of averaging performed on the data:
            binary: Only report results for the class specified by pos_label.
                This is applicable only if targets (y_{true,pred}) are binary.
            micro: Calculate metrics globally by counting the total true positives,
                false negatives and false positives.
            macro: Calculate metrics for each label, and find their unweighted mean.
                This does not take label imbalance into account.
            weighted: Calculate metrics for each label, and find their average
                weighted by support (the number of true instances for each label).
                This alters ‘macro’ to account for label imbalance; it can result
                in an F-score that is not between precision and recall.
            samples: Calculate metrics for each instance, and find their average
                (only meaningful for multilabel classification).
    sample_weight: Sample weights.
Returns:
    precision: Precision score.
"""


class Precision(datasets.Metric):
    def _info(self):
        return datasets.MetricInfo(
            description=_DESCRIPTION,
            inputs_description=_KWARGS_DESCRIPTION,
            features=datasets.Features(
                {
                    "predictions": datasets.Value("int"),
                    "references": datasets.Value("int"),
                }
            ),
            reference_urls=["https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html"],
        )

    def _compute(self, predictions, references, labels=None, pos_label=1, average="binary", sample_weight=None):
        return {
            "precision": precision_score(references, predictions, labels, pos_label, average, sample_weight),
        }
