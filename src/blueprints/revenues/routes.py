""" Motorist Routes """


from flask import Blueprint, render_template, redirect, request, url_for
from src.database.querys import RevenuesQuery

revenues_app = Blueprint("revenues_app", __name__, url_prefix="/revenues/")


@revenues_app.route("/settings", methods=["GET"])
def show():
    "Get all motorists in database"
    porcents = RevenuesQuery.all()
    return render_template("pages/revenues/show.html", porcents=porcents)


@revenues_app.route("/create", methods=["POST", "GET"])
def create():
    "Create a new motorist"
    if request.method == "POST":
        group_name = request.form.get("group_name")
        porcent_one = request.form.get("porcent_one")
        porcent_two = request.form.get("porcent_two")
        porcent_tree = request.form.get("porcent_tree")
        RevenuesQuery.create_motorist_group(
            group_name, porcent_one, porcent_two, porcent_tree
        )

        return redirect(url_for("revenues_app.show"))

    return render_template("pages/revenues/create.html")


@revenues_app.route("/edit/<porcent_id>", methods=["POST", "GET"])
def edit(porcent_id):
    "Create a new motorist"
    # if request.method == "POST":
    #     porcent_one = request.form.get("porcent_one")
    #     porcent_two = request.form.get("porcent_two")
    #     porcent_tree = request.form.get("porcent_tree")
    #     RevenuesQuery.update_porcent(
    #         porcent_one,
    #         porcent_two,
    #         porcent_tree)

    # return redirect(url_for("revenues_app.show"))
    porcent = RevenuesQuery.find(porcent_id)
    print(porcent)
    return render_template("pages/revenues/edit.html", porcent=porcent)


@revenues_app.route("/invoices", methods=["POST", "GET"])
def invoices():
    "Create a new motorist"
    # if request.method == "POST":
    #     porcent_one = request.form.get("porcent_one")
    #     porcent_two = request.form.get("porcent_two")
    #     porcent_tree = request.form.get("porcent_tree")
    #     RevenuesQuery.update_porcent(
    #         porcent_one,
    #         porcent_two,
    #         porcent_tree)

    # return redirect(url_for("revenues_app.show"))
    return render_template("pages/revenues/invoices.html")
