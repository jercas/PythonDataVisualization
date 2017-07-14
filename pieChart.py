""" 
**************************************************************************************
***    coding = utf-8                                                              ***
***    By JerCas                                                                   ***
***    2017-7-13                                                                   ***
***                                                                                ***
***    A little test of print a pie chart by matplotlib.pyplot package             ***
**************************************************************************************
"""

import matplotlib.pyplot as plt
def main():
    # 存储扇形块标签列表
    labels = ['computer science', 'foreign languages', 'analytical chemistry', 'education',
              'humanities', 'physics', 'biology', 'math and statistics', 'engineering']
    # 存储扇形块大小列表
    sizes = [21,3,7,7,8,9,10,15,19]
    # 存储扇形块颜色列表，自适应识别string类型的颜色标记
    colors = ['darkolivegreen', 'gold', 'lightskyblue', 'lightcoral', 'red', 'purple', '#f280de' ,'orange', 'green']
    explode = (0,0,0,0,0,0,0,0,0.1)

    fig1, ax1 = plt.subplots()
    # 调用pyplot.pie()绘制饼图/扇形图
    ax1.pie(sizes, colors=colors,labels=labels, explode=explode, autopct='%1.1f%%', pctdistance=0.5,
            labeldistance=1.1, shadow=True, startangle=180, radius=1, counterclock=False, frame=False)
    # 相等的纵横比保证饼图始终是圆的
    ax1.axis('equal')
    plt.show()

if __name__ == '__main__':
    main()