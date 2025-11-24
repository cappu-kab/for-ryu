from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/intro')
def intro():
    return render_template('page1_intro.html')

@app.route('/puzzle')
def puzzle():
    return render_template('page2_puzzle.html')

@app.route('/memory')
def memory():
    return render_template('page3_memory.html')

@app.route('/message1')
def message1():
    return render_template('page4_message1.html')

@app.route('/message2')
def message2():
    return render_template('page5_message2.html')

@app.route('/likes')
def likes():
    like_list = [
        "เราชอบเวลาพี่ยิ้มมากๆๆๆเลย ทั้งตาทั้งปากทั้งแก้ม ทุกอย่างมันน่ารักสุดๆ",
        "เวลากอดพี่มันอบอุ่นตลอดเลย ชอบมากที่สุดเลยนะ ",
        "พี่ไม่เคยยอมแพ้ในตัวเราเลย ไม่เคยคิดจะทิ้งเราด้วย",
        "พี่ยังทำให้วันธรรมดาๆของเรามีความสุขได้ตลอด เราชอบมุกตลก(?)ของพี่นะ ไว้เล่นอีก",
        "พี่เปนคนที่ใจดี แล้วก้ทัศนคติดีมากๆเลย",
        "พี่รับฟังเราตลอด หลายๆเรื่อง เปนผู้ฟังที่ดีสุดๆ ใจเยนมากๆด้วย",
        "พี่เปนเซฟโซนของเราจริงๆนะ เวลาอยุ่ด้วยแล้วเราก้ยังสบายใจเหมือนเดิมเลย",
        "พี่ให้โอกาส แล้วก้ยอมให้เราทำนุ่นทำนี่หลายๆอย่างด้วย",
        "เราชอบสายตาของพี่มากๆ ตาพี่สวยจริงๆนะ ",
        "เราชอบริวนะ ชอบทั้งหมดที่เปนริว "
    ]
    return render_template("page5_5_likes.html", likes=like_list)


@app.route('/final')
def final():
    return render_template('page6_final.html')

if __name__ == '__main__':
    app.run(debug=True)
