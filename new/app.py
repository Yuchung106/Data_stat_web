from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    # 데이터 로드
    data = pd.read_csv('csv.csv')
  # 'age' 컬럼에 대한 히스토그램 생성
    plt.figure(figsize=(10, 6))
    sns.histplot(data['age'])
    plt.title('Age Distribution')
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url_age = base64.b64encode(img.getvalue()).decode()

    # 'sex' 컬럼에 대한 카운트 플롯 생성
    plt.figure(figsize=(10, 6))
    sns.countplot(data['sex'])
    plt.title('Sex Distribution')
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url_sex = base64.b64encode(img.getvalue()).decode()

    # HTML 페이지로 데이터 시각화 전달
    return render_template('index.html', plot_url_age=plot_url_age, plot_url_sex=plot_url_sex)

if __name__ == '__main__':
    app.run(debug=True)
