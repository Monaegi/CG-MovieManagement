import datetime

from io import StringIO
import django
from django.http import HttpResponse
from django.shortcuts import render
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Create your views here.
def index(request):
    return render(request, 'base/base.html')

def statistics(request):

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    fig = Figure()
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=1)

    value = np.random.standard_normal(40)
    index = range(len(value))

    # 여기서 그림1이 출력됨
    plt.plot(index, value)  # 선이나 마커를 플롯하는 함수

    plt.xlim(0, 20)  # x축 범위 설정
    plt.ylim(np.min(value) - 1,
             np.min(value) + 1)  # y축 범위 설정 value 변수의 최솟값보다 하나 작은 값으로 아래 한계를 정하고, 최대값보다 하나 큰 값으로 위의 한계를 정함

    # Plot 옵션 설정 및 꾸미기
    plt.figure(figsize=(7, 4))  # plot의 모양. 가로 세로가 7인치, 4인치 비로 설정
    plt.plot(value.cumsum(), 'b',
             lw=1.5)  # plot 함수 호출 numpy.cumsum() : plot의 새로운 figure을 생성하는 함수. 'b' : 파란색, w=1.5(표시할 스타일)
    plt.plot(value.cumsum(), 'ro')  # plot 함수 호출 'ro'는 빨간색 동그라미를 의미
    plt.xlabel('index')  # x축 이름 설정
    plt.ylabel('value')  # y축 이름 설정
    plt.title("Line Plot1")  # 플롯의 제목을 설정하는 함수
    plt.savefig("../.media/graphic/graphic.png", format='png')

    fig.autofmt_xdate()
    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    mpl.pyplot.close(fig)

    return render(request, 'statistics/statistics.html')

def search(request):
    pass
