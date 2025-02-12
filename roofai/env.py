from blue_options.env import load_config, load_env, get_env

load_env(__name__)
load_config(__name__)


GOOGLE_MAPS_API_KEY = get_env("GOOGLE_MAPS_API_KEY")

TEST_roofAI_ingest_AIRS_v1 = get_env("TEST_roofAI_ingest_AIRS_v1")

TEST_roofAI_ingest_AIRS_v2 = get_env("TEST_roofAI_ingest_AIRS_v2")

TEST_roofAI_ingest_CamVid_v1 = get_env("TEST_roofAI_ingest_CamVid_v1")

TEST_roofAI_semseg_model_AIRS_full_v1 = get_env("TEST_roofAI_semseg_model_AIRS_full_v1")

TEST_roofAI_semseg_model_AIRS_full_v2 = get_env("TEST_roofAI_semseg_model_AIRS_full_v2")

TEST_roofAI_semseg_model_CamVid_v1 = get_env("TEST_roofAI_semseg_model_CamVid_v1")

ROOFAI_AIRS_CACHE_OBJECT_NAME = get_env("ROOFAI_AIRS_CACHE_OBJECT_NAME")

ROOFAI_TEST_GOOGLE_MAPS_LAT = get_env("ROOFAI_TEST_GOOGLE_MAPS_LAT", 0.0)
ROOFAI_TEST_GOOGLE_MAPS_LON = get_env("ROOFAI_TEST_GOOGLE_MAPS_LON", 0.0)
