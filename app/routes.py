from app import app, db
from flask import render_template, redirect, url_for
from  sqlalchemy.sql.expression import func
from app.models import Thing
from app.forms import NewForm


@app.route("/new", methods=["GET", "POST"])
def new():
    form = NewForm()
    if form.validate_on_submit():
        thing = Thing(description=form.description.data, original_value=float(form.value.data))
        db.session.add(thing)
        db.session.commit()
        return redirect(url_for("new"))
    return render_template("new.html", form=form)


@app.route("/ranking")
def ranking():
    things = Thing.query.order_by(Thing.value.desc()).all()
    return render_template("ranking.html", things=things)


@app.route("/")
def index():
    entries = Thing.query.order_by(func.random()).limit(2).all()
    return render_template("index.html", left=entries[0], right=entries[1])


@app.route("/upvote/<id>")
def upvote(id):
    thing = Thing.query.get(id)
    thing.upvote()
    db.session.add(thing)
    db.session.commit()
    return redirect(url_for("index"))
