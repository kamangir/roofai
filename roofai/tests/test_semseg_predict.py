from blue_objects import objects

from roofai.tests.caching import cache_pretrainedmodels
from roofai.semseg.interface import predict
from roofai import env


def test_semseg_predict():
    assert cache_pretrainedmodels()

    model_object_name = env.TEST_roofAI_semseg_model_CamVid_v1
    assert objects.download(model_object_name)

    dataset_object_name = env.TEST_roofAI_ingest_CamVid_v1
    assert objects.download(dataset_object_name)

    prediction_object_name = objects.unique_object("test_semseg_predict")

    predict(
        model_path=objects.object_path(model_object_name),
        dataset_path=objects.object_path(dataset_object_name),
        prediction_path=objects.object_path(prediction_object_name),
        device="cpu",
    )
