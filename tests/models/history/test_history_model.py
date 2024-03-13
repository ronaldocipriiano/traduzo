import json
import pytest


try:
    from src.models.history_model import HistoryModel
except ImportError as error:
    pytestmark = pytest.mark.skip(reason=error.msg)


def test_request_history(prepare_base):
    json_data = HistoryModel.list_as_json()

    expected_json = [
        {
            "text_to_translate": "Hello, I like videogame",
            "translate_from": "en",
            "translate_to": "pt",
        },
        {
            "text_to_translate": "Do you love music?",
            "translate_from": "en",
            "translate_to": "pt",
        },
    ]

    json_data_list = json.loads(json_data)

    for item in json_data_list:
        item.pop('_id', None)

    json_data_list_sorted = sorted(
        json_data_list, key=lambda x: x["text_to_translate"]
    )
    expected_json_list_sorted = sorted(
        expected_json, key=lambda x: x["text_to_translate"]
    )

    assert json_data_list_sorted == expected_json_list_sorted
