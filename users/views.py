import json
from flask import Blueprint
from Class.Class import User


users_blueprint = Blueprint('users_blueprint', __name__)


# @users_blueprint.route("/")
# def all_users():
#     users = User.query.all()
#     user_res = []
#
#     for user in users:
#         user_res.append(
#             {
#                 "id": user.id,
#                 "first_name": user.first_name,
#                 "last_name": user.last_name,
#                 "age": user.age,
#                 "email": user.email,
#                 "role": user.role,
#                 "phone": user.phone
#             }
#         )
#     return json.dumps(user_res)
#
#
# @users_blueprint.route("/<int:id>")
# def one_user(id):
#     user = User.query.get(id)
#
#     if user is None:
#         return "sorry"
#
#     return json.dumps({
#         "id": user.id,
#         "first_name": user.first_name,
#         "last_name": user.last_name,
#         "age": user.age,
#         "email": user.email,
#         "role": user.role,
#         "phone": user.phone
#     })