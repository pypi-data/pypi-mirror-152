from dataclasses import dataclass
from marshmallow_dataclass import class_schema

from .data import FeatureParams
from .preprocessing import PreprocessingParams
from .models import ModelParams


@dataclass()
class PredictPipelineParams:
    input_data_path: str
    output_inference_data_path: str
    features: FeatureParams
    model: ModelParams
    model_path: str
    transformer_path: str
    preprocessing: PreprocessingParams
    save_output: bool


PredictPipelineParamsSchema = class_schema(PredictPipelineParams)


def get_predict_pipeline_params(dict_config: dict) -> PredictPipelineParams:
    return PredictPipelineParamsSchema().load(dict_config)
