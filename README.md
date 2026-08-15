# BME Student Toolkit

A lightweight Flask web app built by a Biomedical Engineering student, for BME students — starting with two practical tools for everyday coursework and group project struggles.

## Why I built this

I'm a Biomedical Engineering undergraduate who never originally planned to be in this field, but chose to take ownership of it. Along the way, I noticed how much time BME students lose to small but constant friction — converting units for lab values and dosages, or keeping group projects organized without a proper tool. This toolkit is my attempt to remove some of that friction, one small tool at a time.

It's also personal proof of what's possible with limited resources: this entire project — every commit — was built and deployed from a phone, with no laptop, using Spck Editor and GitHub.

## Features

**Unit & Dosage Converter**
- mg/dL ↔ mmol/L (blood glucose conversion)
- Dosage by body weight (mg/kg → total mg)
- BMI calculator

**Group Project Task Tracker**
- Add tasks with assignee and deadline
- Mark tasks as done / pending
- Simple JSON-based storage, no database required

## Tech stack

- Python 3 / Flask
- Jinja2 templating
- HTML/CSS (no frontend framework)
- JSON file storage
- Deployed on Render

## Running it locally

Clone the repo, install dependencies with pip install -r requirements.txt, then run python app.py and visit http://127.0.0.1:5000 in your browser.

## Roadmap

This is v1 of a toolkit meant to grow. Ideas for what's next:
- More unit conversions (lab values, drug calculations)
- Editing/deleting tasks
- Multi-user support for real group projects
- Lab data visualization tools

## Live demo

https://bme-student-toolkit.onrender.com/
