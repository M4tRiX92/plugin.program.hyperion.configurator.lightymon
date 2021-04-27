"""Routing."""
from flask import current_app as app
from flask import redirect, render_template, url_for

from .forms import SetLEDForm


@app.route("/")
def home():
    """Landing page."""
    return render_template(
        "index.jinja2",
        template="home-template",
        title="Lightymon Setup"
    )


@app.route("/setleds", methods=["GET", "POST"])
def setleds():
    """Set the LEDs."""
    form = SetLEDForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "setleds.jinja2",
        form=form,
        template="form-template",
        title="SetLEDs Form"
    )


@app.route("/success", methods=["GET", "POST"])
def success():
    """Generic success page upon form submission."""
    return render_template(
        "success.jinja2",
        template="success-template"
    )
