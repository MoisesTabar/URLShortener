from flask import Blueprint, request, redirect, jsonify
from models import Url
from configs import db
from repositories import UrlsRepository
from usecases import URLShortenerUseCase
import webbrowser

router = Blueprint('shortener_router', __name__, url_prefix='/api/v1')

url_shortener_use_case = URLShortenerUseCase(UrlsRepository(db))

@router.post('/url/shorten')
def shorten_url():

    req = request.get_json(force=True)

    url: str = req["url"]

    model: Url = Url(url)

    url_already_exists = url_shortener_use_case.verify_url_existence_use_case(model)

    if url_already_exists["result"] != "OK":
        return jsonify({"result": url_already_exists["result"]}), 400

    short_url = url_shortener_use_case.shorten_an_url_use_case(model)

    return jsonify({"result": short_url}), 201

@router.get('/url/top')
def top_visited_urls():

    visited_urls = url_shortener_use_case.top_visited_urls_use_case()

    return jsonify({"urls": visited_urls}), 200

@router.post('/url/visit/<url>')
def visit_url(url: str):
    update_clicks = url_shortener_use_case.update_url_clicks_use_case(url)

    if update_clicks["result"] != "OK":
        return jsonify({"result": update_clicks["result"]}), 400
    
    long_url: str = update_clicks["document"]["longUrl"]
    
    webbrowser.open(long_url)
    
    return redirect(long_url), 200