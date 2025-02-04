#  Copyright 2021-present, the Recognai S.L. team.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from typing import TYPE_CHECKING, Any

import pytest
from argilla.client.models import Framework
from argilla.feedback import TrainingTask

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


@pytest.fixture
def rating_question_payload():
    return {
        "name": "label",
        "description": "label",
        "required": True,
        "values": ["1", "2"],
    }


@pytest.fixture
def label_question_payload():
    return {
        "name": "label",
        "description": "label",
        "required": True,
        "labels": ["1", "2"],
    }


@pytest.fixture
def ranking_question_payload():
    return {
        "name": "label",
        "description": "label",
        "required": True,
        "values": ["1", "2"],
    }


@pytest.fixture
def mocked_is_on_huggingface(mocker: "MockerFixture") -> bool:
    mocker.patch(
        "argilla.client.feedback.integrations.huggingface.model_card.model_card.is_on_huggingface", return_value=True
    )
