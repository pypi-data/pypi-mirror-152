import numpy as np
import pandas as pd
import logging

from typing import Union
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from .model_params import ModelParams


SklearnClassifierModel = Union[LogisticRegression, RandomForestClassifier]

logger = logging.getLogger(__name__)


def create_model(model_params: ModelParams) -> SklearnClassifierModel:
    """
    Creates model describes in `model_params`.
    Args:
        model_params: Model description.

    Returns: Model.
    """
    if model_params.model_type == "LogisticRegression":
        model = LogisticRegression(**model_params.params)
    elif model_params.model_type == "RandomForestClassifier":
        model = RandomForestClassifier(**model_params.params)
    else:
        error_message = f"Unknown model type: {model_params.model_type}."
        logger.error(error_message)
        raise ValueError(error_message)

    return model


def train(
    features: Union[pd.DataFrame, np.ndarray],
    target: Union[pd.Series, np.ndarray],
    model_params: ModelParams,
) -> SklearnClassifierModel:
    """
    Returns a model described in `model_params` trained on features provided.

    Raises: ValueError if model_type is unknown.
    """

    model = create_model(model_params)
    model.fit(features, target)
    logger.info(f"Fit Model: {model.__str__()}")

    return model
