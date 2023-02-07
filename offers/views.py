import json
from flask import Blueprint
from Class.Class import Offer

# Добавим настройку папки с шаблонами
offers_blueprint = Blueprint('offers_blueprint', __name__)


@offers_blueprint.route("/")
def all_offers():
    offers = Offer.query.all()
    offer_res = []

    for offer in offers:
        offer_res.append(
            {
                "id": offer.id,
                "order_id": offer.order_id,
                "executor_id": offer.executor_id
            }
        )
    return json.dumps(offer_res)


@offers_blueprint.route("/<int:id>")
def one_offer(id):
    offer = Offer.query.get(id)

    if offer is None:
        return "sorry"

    return json.dumps({
        "id": offer.id,
        "order_id": offer.order_id,
        "executor_id": offer.executor_id
    })