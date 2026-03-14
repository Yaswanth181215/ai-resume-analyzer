from flask import Flask, render_template, request
from pdfminer.high_level import extract_text
from skills import skills_list
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def extract_skills(text):

    text = text.lower()
    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills


def calculate_score(resume_skills, job_skills):

    matched = list(set(resume_skills) & set(job_skills))
    missing = list(set(job_skills) - set(resume_skills))

    if len(job_skills) == 0:
        score = 0
    else:
        score = (len(matched) / len(job_skills)) * 100

    return matched, missing, score


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        file = request.files["resume"]
        jobdesc = request.form["jobdesc"]

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        resume_text = extract_text(filepath)

        resume_skills = extract_skills(resume_text)
        job_skills = extract_skills(jobdesc)

        matched, missing, score = calculate_score(resume_skills, job_skills)

        return render_template(
            "index.html",
            matched=matched,
            missing=missing,
            score=round(score, 2)
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)