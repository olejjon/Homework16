import json
from flask import Blueprint
from Class.Class import Order
from main import db

# Добавим настройку папки с шаблонами
orders_blueprint = Blueprint('orders_blueprint', __name__)


@orders_blueprint.route("/")
def all_orders():
    orders = Order.query.all()
    order_res = []

    for order in orders:
        order_res.append(
            {
                "id": order.id,
                "name": order.first_name,
                "description": order.last_name,
                "start_date": order.age,
                "end_date": order.email,
                "address": order.role,
                "price": order.phone,
                "customer_id": order.customer_id,
                "executor_id": order.executor_id
            }
        )
    return json.dumps(order_res)


@orders_blueprint.route("/<int:id>")
def one_order(id):
    order = Order.query.get(id)

    if order is None:
        return "sorry"

    return json.dumps({
        "id": order.id,
        "name": order.first_name,
        "description": order.last_name,
        "start_date": order.age,
        "end_date": order.email,
        "address": order.role,
        "price": order.phone,
        "customer_id": order.customer_id,
        "executor_id": order.executor_id
    })


# @orders_blueprint.post("/post")
# def one_order(text):
#     new_order = text
#     db.session.add(new_order)
#     db.session.commit()
#
#
# @orders_blueprint.put("/<int:id>/put")
# def one_order(id):
#     order = Order.query.get(id)
#     #s =
#     db.session.add(order)
#     db.session.commit()
#
#
# @orders_blueprint.delete("/<int:id>/delete")
# def one_order(id):
#     order = Order.query.get(id)
#     db.session.delete(order)
#     db.session.commit()