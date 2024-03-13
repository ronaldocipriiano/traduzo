from flask import Blueprint, render_template, request
from deep_translator import GoogleTranslator
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


@bp.route("/", methods=["POST"])
def post_translate():
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    translated_text = GoogleTranslator(
        source=translate_from, target=translate_to
    ).translate(text_to_translate)

    languages = LanguageModel.list_dicts()
    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated_text
    )


@bp.route("/reverse", methods=["POST"])
def post_reverse():
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    translated_text = GoogleTranslator(
        source=translate_from, target=translate_to
    ).translate(text_to_translate)

    languages = LanguageModel.list_dicts()

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=translated_text,
        translate_from=translate_to,
        translate_to=translate_from,
        translated=text_to_translate
    )
