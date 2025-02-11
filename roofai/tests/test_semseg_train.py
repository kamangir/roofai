import pytest

from blue_objects import objects

from roofai import env
from roofai.tests.caching import cache_pretrainedmodels
from roofai.semseg.interface import predict, train
from roofai.semseg.model import SemSegModel


@pytest.mark.parametrize(
    "dataset_object_name, classes",
    [
        (
            # roofai dataset ingest \
            #  source=palisades-dataset-v1,upload \
            #  palisades-dataset-v1-1000X-test \
            #  --test_count 100 \
            #  --train_count 800 \
            #  --val_count 100
            "palisades-dataset-v1-1000X-test",
            ["affected"],
        ),
        (
            env.TEST_roofAI_ingest_AIRS_v1,
            ["roof"],
        ),
        (
            env.TEST_roofAI_ingest_CamVid_v1,
            ["car"],
        ),
    ],
)
def test_semseg_train(dataset_object_name, classes):
    assert cache_pretrainedmodels()

    assert objects.download(dataset_object_name)

    model_object_name = objects.unique_object("test_semseg_train-model")

    model = train(
        dataset_path=objects.object_path(dataset_object_name),
        model_path=objects.object_path(model_object_name),
        classes=classes,
    )
    assert isinstance(model, SemSegModel)

    predict(
        model_path=objects.object_path(model_object_name),
        dataset_path=objects.object_path(dataset_object_name),
        prediction_path=objects.object_path(objects.unique_object()),
        device="cpu",
    )
