import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores
from schemas import StoreSchema

blp = Blueprint("stores", __name__, description="Operations on stores.")


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            return {"message": "Store not found."}, 404

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted."}
        except KeyError:
            return {"message": "Store not found."}, 404


@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return list(stores.values())

    @blp.response(201, StoreSchema)
    @blp.arguments(StoreSchema)
    def post(self, store_data):
        store_id = uuid.uuid4().hex
        new_store = {**store_data, "id": store_id}
        stores[store_id] = new_store
        return new_store


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(cls, store_id):
        try:
            # You presumably would want to include the store's items here too
            # More on that when we look at databases
            return stores[store_id]
        except KeyError:
            abort(404, message="Store not found.")

    def delete(cls, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted."}
        except KeyError:
            abort(404, message="Store not found.")
