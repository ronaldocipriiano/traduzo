from flask import Blueprint, render_template
from models.language_model import LanguageModel


bp = Blueprint("translate_controller", __name__)


@bp.route("/", methods=["GET"])
def index():
    languages = LanguageModel.list_dicts()

    text_to_translate = "O que deseja traduzir?"
    translate_from = "pt"
    translate_to = "en"
    translated = "What do you want to translate?"

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated
    )
