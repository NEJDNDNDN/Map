import uuid
from flask import Flask, render_template, request

app = Flask(__name__)

# توليد رابط فريد
def generate_link():
    uid = str(uuid.uuid4())[:8]  # جزء من UUID ليكون الرابط قصيرًا
    return uid

@app.route('/')
def index():
    # توليد الرابط الفريد
    unique_id = generate_link()
    # إرسال الرابط الفريد إلى صفحة HTML
    return render_template('index.html', track_id=unique_id)

if __name__ == "__main__":
    app.run(debug=True)
