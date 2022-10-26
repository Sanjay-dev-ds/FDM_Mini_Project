import requests
import smtplib
import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html")