import os

import pytest
import yaml

import ga4gh.vr
from ga4gh.vr.extras.seqrepo import get_vmc_sequence_identifier


validation_fn = os.path.join(os.path.dirname(__file__), "..", "data", "schema-tests", "functions.yaml")
validation_tests = yaml.load(open(validation_fn), Loader=yaml.SafeLoader)


@pytest.mark.parametrize("test", validation_tests["digest"])
def test_digest(test):
    assert test["out"]["digest"] == ga4gh.vr.digest(**test["in"])
