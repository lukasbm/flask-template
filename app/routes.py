import os
from datetime import timezone, datetime, timedelta
from app import app, db
from flask import redirect, url_for, render_template, send_from_directory, current_app, session, flash

@app.route('/')
def index():
    return 'Hallo'
