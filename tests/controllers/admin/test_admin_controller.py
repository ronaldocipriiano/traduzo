from src.models.history_model import HistoryModel
from src.models.user_model import UserModel


def user():
    UserModel(
        {
            "name": "Peter",
            "level": "admin",
            "token": "token",
        }
    ).save()

    return {"name": "Peter", "level": "admin", "token": "token"}


def history():
    history_instance = HistoryModel(
        {
            "text_to_translate": "text",
            "translate_from": "pt",
            "translate_to": "en",
        }
    )

    history_instance.save()
    return history_instance.data


def test_history_delete(app_test):
    user_data = user()
    history_data = history()

    response = app_test.delete(
        f"/admin/history/{str(history_data['_id'])}",
        headers={
            "Authorization": user_data["token"],
            "User": user_data["name"]
        },
    )

    assert response.status_code == 204
