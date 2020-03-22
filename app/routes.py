from app import app, db
from flask import render_template, redirect, url_for
from sqlalchemy.sql.expression import func
from app.models import Thing
from app.forms import NewForm


@app.route("/new", methods=["GET", "POST"])
def new():
    form = NewForm()
    if form.validate_on_submit():
        thing = Thing(description=form.description.data, original_value=float(form.value.data.replace(",", ".")))
        db.session.add(thing)
        db.session.commit()
        return redirect(url_for("new"))
    return render_template("new.html", form=form)


@app.route("/ranking")
def ranking():
    things = Thing.query.order_by(Thing.value.desc()).all()
    count = len(things)
    return render_template("ranking.html", things=things, count=count)


@app.route("/admin")
def admin():
    things = Thing.query.order_by(Thing.count.desc()).all()
    return render_template("admin.html", things=things)


@app.route("/faq")
def faq():
    return render_template("faq.html")


@app.route("/")
def index():
    avg = db.session.query(func.avg(Thing.count)).first()[0]
    print("AVG: ", avg)
    entries = Thing.query.filter(Thing.count <= avg).order_by(func.random()).limit(2).all()

    for e in entries:
        print("Count: ", e.count)
        e.choosen()
        db.session.add(e)
    db.session.commit()

    return render_template("index.html", left=entries[0], right=entries[1])


@app.route("/upvote/<id>")
def upvote(id):
    thing = Thing.query.get(id)
    thing.upvote()
    db.session.add(thing)
    db.session.commit()
    return redirect(url_for("index"))
