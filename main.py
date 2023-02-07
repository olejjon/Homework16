import json
from urllib import request

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

# from users.views import users_blueprint
# from orders.views import orders_blueprint
# from offers.views import offers_blueprint
from lists import users_list, orders_list, offers_list

# from Class.Class import User, Order, Offer


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
app.url_map.strict_slashes = False
db = SQLAlchemy(app)


# app.register_blueprint(users_blueprint, url_prefix='/users')
# app.register_blueprint(orders_blueprint, url_prefix='/orders')
# app.register_blueprint(offers_blueprint, url_prefix='/offers')

def get_response(data: dict) -> json:
    return json.dumps(data), 200, {'Content-Type':'application/json; charset=utf-8'}


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    age = db.Column(db.Integer)
    email = db.Column(db.String)
    role = db.Column(db.String)
    phone = db.Column(db.String)

    def to_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__tablename__}


class Offer(db.Model):
    __tablename__ = 'offer'
    id = db.Column(db.Integer, primary_key=True)

    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    order = relationship("Order")

    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = relationship("User")
    def to_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__tablename__}

class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    start_date = db.Column(db.Text)
    end_date = db.Column(db.Text)
    address = db.Column(db.String)
    price = db.Column(db.Integer)

    customer_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    order = relationship("Order")

    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = relationship("User")

    def to_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__tablename__}


# with app.app_context():
#     db.create_all()


# with app.app_context():
#     for user in users_list():
#         user_ = User(id=user['id'], first_name=user['first_name'], last_name=user['last_name'], age=user['age'],
#                      email=user['email'], role=user['role'], phone=user['phone'])
#         db.session.add(user_)
#     db.session.commit()
#     for offer in offers_list():
#         offer_ = Offer(id=offer['id'], order_id=offer['order_id'], executor_id=offer['executor_id'])
#         db.session.add(offer_)
#     db.session.commit()
#     for order in orders_list():
#         order_ = Order(id=order['id'], name=order['name'], description=order['description'],
#                        start_date=order['start_date'], end_date=order['end_date'], address=order['address'],
#                        price=order['price'], customer_id=order['customer_id'], executor_id=order['executor_id'], )
#         db.session.add(order_)
#     db.session.commit()


@app.route("/users", methods=['GET', 'POST'])
def all_users():
    if request.method == 'GET':
        users = User.query.all()
        user_res = [users.to_dict() for users in users]
        return get_response(user_res)
    elif request.method == 'POST':
        user_data = json.load(request.data)
        db.session.add(User(**user_data))
        db.session.commit()
        return '', 201


@app.route("/users/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def one_user(id: int):
    user = User.query.get(id)
    if request.method == 'GET':
        return get_response(user.to_dict())
    if request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
    if request.method == 'PUT':
        user_data = json.loads(request.data)
        user.first_name = user_data['first_name']
        user.last_name = user_data['last_name']
        user.role = user_data['role']
        user.phone = user_data['phone']
        user.email = user_data['email']
        user.age = user_data['age']
        db.session.add(user)
        db.session.commit()
        return '',204


@app.route("/orders", methods=['GET', 'POST'])
def all_orders():
    orders = Order.query.all()
    if request.method == 'GET':
        orders_res = [orders.to_dict() for orders in orders]
        return get_response(orders_res)
    elif request.method == 'POST':
        user_data = json.load(request.data)
        db.session.add(Order(**user_data))
        db.session.commit()
        return '', 201


@app.route("/orders/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def one_order(id):
    order = Order.query.get(id)
    if request.method == 'GET':
        return get_response(order.to_dict())
    if request.method == 'DELETE':
        db.session.delete(order)
        db.session.commit()
    if request.method == 'PUT':
        order_data = json.loads(request.data)
        order.name = order_data['name']
        order.description = order_data['description']
        order.start_date = order_data['start_date']
        order.end_date = order_data['end_date']
        order.address = order_data['address']
        order.price = order_data['price']
        order.customer_id = order_data['customer_id']
        order.executor_id = order_data['executor_id']
        db.session.add(order)
        db.session.commit()
        return '',204

@app.route("/offers", methods=['GET', 'POST'])
def all_offers():
    offers = Offer.query.all()
    if request.method == 'GET':
        offer_res = [offers.to_dict() for offers in offers]
        return get_response(offer_res)
    elif request.method == 'POST':
        user_data = json.load(request.data)
        db.session.add(Offer(**user_data))
        db.session.commit()
        return '', 201


@app.route("/offers/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def one_offer(id):
    offer = Offer.query.get(id)
    if request.method == 'GET':
        return get_response(offer.to_dict())
    if request.method == 'DELETE':
        db.session.delete(offer)
        db.session.commit()
    if request.method == 'PUT':
        offer_data = json.loads(request.data)
        offer.order_id = offer_data['order_id']
        offer.executor_id = offer_data['executor_id']
        db.session.add(offer)
        db.session.commit()
        return '', 204


if __name__ == '__main__':
    app.run(debug=True)
