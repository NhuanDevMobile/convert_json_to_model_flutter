from flask import Flask, request, render_template
import FormatAttribute as fotmat
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-text', methods=['GET', 'POST'])
def foo():
    # try:
    if request.form.get("submit_1"):
        bar = request.form['test']
        title = request.form['title']
        if bar != '':
            arr = bar.split("\n")
            print(bar)
            re = fotmat.FormatAttribute(arr)
            return render_template('index.html', data=re, text = bar, title = title)
        else:
            arr = []
            arr.append("Bạn chưa nhập dữ liệu")
            return render_template('index.html', data=arr,  text = bar, title = title)
    if request.form.get("submit_2"):
        bar = request.form['test']
        title = request.form['title']
        if bar != '':
            arr = bar.split("\n")
            re = fotmat.FormatModel(arr,title)
            return render_template('index.html', data=re,  text = bar, title = title)
        else:
            arr = []
            arr.append("Bạn chưa nhập dữ liệu")
            return render_template('index.html', data=arr,  text = bar, title = title)
    if request.form.get("submit_3"):
        bar = request.form['test']
        title = request.form['title']
        if bar != '':
            arr = bar.split("\n")
            re = fotmat.FormatSuper(arr)
            return render_template('index.html', data=re, text=bar, title = title)
        else:
            arr = []
            arr.append("Bạn chưa nhập dữ liệu")
            return render_template('index.html', data=arr, text=bar, title = title)
    if request.form.get("submit_4"):
        bar = request.form['test']
        title = request.form['title']
        if bar != '':
            arr = bar.split("\n")
            re = fotmat.FormatJson(arr)
            return render_template('index.html', data=re, text=bar, title = title)
        else:
            arr = []
            arr.append("Bạn chưa nhập dữ liệu")
            return render_template('index.html', data=arr, text=bar, title = title)
    if request.form.get("submit_10"):
        bar = request.form['test']
        title = request.form['title']
        if bar != '':
            arr = bar.split("\n")
            re = fotmat.FormatJson1(arr, title)
            return render_template('index.html', data=re, text=bar, title = title)
        else:
            arr = []
            arr.append("Bạn chưa nhập dữ liệu")
            return render_template('index.html', data=arr, text=bar, title = title)
    if request.form.get("submit_5"):
        bar = request.form['test']
        title = request.form['title']
        if bar != '':
            arr = bar.split("\n")
            re = fotmat.FormatFinal(arr)
            return render_template('index.html', data=re, text=bar, title = title)
        else:
            arr = []
            arr.append("Bạn chưa nhập dữ liệu")
            return render_template('index.html', data=arr, text=bar, title = title)
    if request.form.get("submit_6"):
        bar = request.form['test']
        title = request.form['title']
        if bar != '':
            arr = bar.split("\n")
            re = fotmat.FormatThis(arr, title)
            return render_template('index.html', data=re, text=bar, title = title)
        else:
            arr = []
            arr.append("Bạn chưa nhập dữ liệu")
            return render_template('index.html', data=arr, text=bar, title = title)
    if request.form.get("submit_7"):
        bar = request.form['test']
        title = request.form['title']
        if bar != '':
            arr = bar.split("\n")
            re = fotmat.FormatRequiredThis(arr)
            return render_template('index.html', data=re, text=bar, title = title)
        else:
            arr = []
            arr.append("Bạn chưa nhập dữ liệu")
            return render_template('index.html', data=arr, text=bar, title = title)
    if request.form.get("submit_8"):
        bar = request.form['test']
        title = request.form['title']
        if bar != '':
            arr = bar.split("\n")
            re = fotmat.FormatAttributeCT(arr)
            return render_template('index.html', data=re, text=bar, title = title)
        else:
            arr = []
            arr.append("Bạn chưa nhập dữ liệu")
            return render_template('index.html', data=arr, text=bar, title = title)
    if request.form.get("submit_9"):
        bar = request.form['test']
        title = request.form['title']
        if bar != '':
            arr = bar.split("\n")
            re = fotmat.FormatHoaThuong(arr)
            return render_template('index.html', data=re, text=bar, title = title)
        else:
            arr = []
            arr.append("Bạn chưa nhập dữ liệu")
            return render_template('index.html', data=arr, text=bar, title = title)
    if request.form.get("submit_11"):
        bar = request.form['test']
        title = request.form['title']
        if bar != '':
            arr = bar.split("\n")
            re = fotmat.FormatToJson(arr)
            return render_template('index.html', data=re, text=bar, title = title)
        else:
            arr = []
            arr.append("Bạn chưa nhập dữ liệu")
            return render_template('index.html', data=arr, text=bar, title = title)
    if request.form.get("submit_12"):
        bar = request.form['test']
        title = request.form['title']
        if bar != '' and title != '':
            arr = bar.split("\n")
            re = fotmat.AutoModel(arr, title)
            return render_template('index.html', data=re, text=bar, title = title)
        else:
            arr = []
            arr.append("Bạn chưa nhập dữ liệu")
            return render_template('index.html', data=arr, text=bar, title = title)
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False)