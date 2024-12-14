import streamlit as st
import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np
from math import pi

np.random.seed(20)
m, si = 543, 10
bull = np.random.normal(m, si, 799) 
bull = np.append(bull, [543])
np.random.seed(3)
known = np.array([62, 63, 64, 65, 66, 67, 68, 69, 69, 69, 69, 71, 72, 73, 74, 77, 78, 78, 79, 80])
unkk = np.array([60, 61, 61, 62, 62, 63, 64, 65, 66, 67, 67, 68, 69, 69, 69, \
         69, 69, 69, 71, 71, 72, 73, 73, 74, 75, 77, 77, 78, 78, 79, 80])
f_100 = lambda x: 900 * np.exp(-((x - m)**2 /(2 * si**2))) / (si * np.sqrt(2 * pi)) 
eqv = np.random.randint(60, 81, 800)
known_pred = np.random.randint(60, 81, 20)
unkk_pred = np.random.randint(60, 81, 31)


def hists(data: np.ndarray, color: str) -> plt.Figure:
    un_dat, co = np.unique(data, return_counts=True)
    fig, ax = plt.subplots(figsize=(12, 6))
    bins=range(int(min(data)), int(max(data)) + 2)
    counts, edges, patches = ax.hist(data, bins=bins, edgecolor='black', align='left', 
                                        rwidth=0.7, color=color, linewidth=1.5)
    if 543 in data:
        i = 543
        xti = [j for j in range(510, 590, 10)]
        xti.append(i)
        xti.sort
        plt.xticks(xti)
        plt.xlabel('Вес быка')
        x = np.arange(510, 580, 0.1)
        y = np.array([f_100(i) for i in x])
        plt.plot(x, y, color='cyan')
    else:
        i = 73
        plt.xlabel('Число')
        plt.xticks(range(min(60, int(min(data))), int(max(data) + 2)))
        x = np.arange(59, 81, 0.1)
        y = np.empty(len(x))
        y.fill(len(data) // 20)
        plt.plot(x, y, color='red')
    highlight_index = list(edges).index(i)
    patches[highlight_index].set_facecolor('#ff7f0e')
    patches[highlight_index].set_edgecolor('#f5f5dc')
    patches[highlight_index].set_linewidth(1.5)
    ax.set_facecolor('#101010')
    fig.patch.set_facecolor('gray')
    plt.title(f'{len(data)} человек')
    plt.ylabel('Количество голосов')
    plt.grid(linestyle=':', alpha=0.25, color='white')
    st.write(f':green[Среднее значение равно: {np.mean(data):.1f}, Отклонение: {i - np.mean(data):.1f}]')
    return fig

st.set_page_config('Угадайка', page_icon=':space_invader:', initial_sidebar_state='auto')
st.header(":orange[Эксперимент 73]", divider='rainbow')
st.balloons()
st.markdown("""
            Данный небольшой мини-эксперимент был вдохновлён экспериментом, проведённым сэром
            [Фрэнсисом Гальтоном](https://ru.wikipedia.org/wiki/%D0%93%D0%B0%D0%BB%D1%8C%D1%82%D0%BE%D0%BD,_%D0%A4%D1%80%D1%8D%D0%BD%D1%81%D0%B8%D1%81) более века назад.
            Подробнее с содежанием эксперимента и тем, во что это вылилось можно ознакомиться [здесь](https://habr.com/ru/companies/vdsina/articles/525752/).
            Если кратко, на площадь выставили быка весом 543,4 кг (~1198 фунтов),
            собрали догадки о его весе у 800 человек,
            вычислили среднее значение ответов и получили 542,9 кг (~1197 фунтов).
            Данный результат мне кажется крышесносным
            """, unsafe_allow_html=True)
st.markdown("""
            Вы можете возразить мне: *"Ведь число не бык, выбор числа может быть абсолютно случайным"* 
            — и окажетесь совершенно правы.
            Действительно, при попытке угадать вес быка в эксперименте Гальтона люди руководствовались своим 
            уникальным эмпирическим опытом,
            полагались на здравый смысл и в целом видели самого быка.
            Перечислить можно множество иных факторов отличающих эксперименты, 
            от банального различия в размерах групп участников до разницы в видах статистических распределений,
            описывающих характер распределения значений
            """)
selected_hist = st.selectbox("Выберите размер группы и эксперимент:", 
                             ["Распределение веса быка(эксперимент Гальтона)",
                              "Ожидаемый вид распределения чисел соразмерного с Гальтоновским",  
                              "Ожидаемыйе вид распределения для 20 человек", 
                              "Ожидаемыйе вид распределения для 31 человека"])

with st.container(height=500):
    if selected_hist == "Ожидаемый вид распределения чисел соразмерного с Гальтоновским":
        hists(eqv, 'orange')
    elif selected_hist == "Ожидаемыйе вид распределения для 20 человек":
        hists(known_pred, 'green')
    elif selected_hist == "Ожидаемыйе вид распределения для 31 человека":
        hists(unkk_pred, 'purple')
    else:
        hists(bull, 'red')
st.markdown("#### __________________________________________________________")
st.markdown("""
            Число действительно не бык, однако у большинства участников(20 человек) имелся определённый эмпирический опыт
            взаимодействия со мной, что вроде как несколько должно менять положение дел""")
col1, col2 = st.columns(2)
with col1:
    st.image('media/rcionalizm.jpg', use_container_width=True)
with col2:
    st.image('media/numerology.jpg', use_container_width=True)
st.markdown("#### __________________________________________________________")
st.markdown("""
            Огромное влияние оказывает и вероятность того, что участник знает об уникальности числа 73.
            Здесь появляется пространство для решения задачи Ферми: оценить эту самую вероятность того,
            что участник обладает подобным знанием, но как в любых других лучших произведениях
            эта задача остаётся для самостоятельного решения читателю
            """)
st.video(r'media/sheldon73.mp4')

st.markdown("""Говоря о своём любимым числе, Шелдон поясняет: «73 — это 21-е простое число. 
               Написанное наоборот оно 37 — это 12-е простое число,и если написать его наоборот — 
               21, — это результат умножения семи и трёх, а также число 73, написанное в двоичной 
               системе счисления является палиндромом: 1-0-0-1-0-0-1», что делает число уникальным. """)
st.markdown(""":gray[[Задачи Ферми](https://en.wikipedia.org/wiki/Fermi_problem)
                — задачи, решить которые стандартными методами обычно не представляется возможным,
                однако можно попытаться оценить результат на основе имеющихся знаний и здравого смысла]{:target='_blank'}""")
st.markdown(""":gray[[Простое число](https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%BE%D1%81%D1%82%D0%BE%D0%B5_%D1%87%D0%B8%D1%81%D0%BB%D0%BE)
                — натуральное число, имеющее ровно два различных натуральных делителя, 
               т.е. число отличное от 1 и делящееся без остатка на 1 и на само себя, например: 2, 3, 5, 7, 11, 13 ...]{:target='_blank'}"""
               )
st.markdown(""":gray[[Числа-палиндромы](https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0-%D0%BF%D0%B0%D0%BB%D0%B8%D0%BD%D0%B4%D1%80%D0%BE%D0%BC%D1%8B)
                — числа, которые в определённой позиционной системе 
               исчисления (как правило — в десятичной) читаются одинаково как справа налево, так и слева направо.
               например: 11, 77, 121, 10101 ...]{:target='_blank'}""")
st.markdown("#### __________________________________________________________")
st.markdown("""
            Отсутствие уникальных знаний и опыта не единственная беда, диапазон чисел [60;80]
            пестрит различными "привлекательным" значениями, что несомненно могло сбить с толку
            """)
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.image(r'media/ch77.jpg', use_container_width=True)
with col2:
    st.image(r'media/def77.jpg', use_container_width=True)
with col3:
    st.image(r'media/palindrom.jpg', use_container_width=True)
with col4:
    st.image(r'media/prikol.jpg', use_container_width=True)
st.markdown("""
            И всё же есть тот, на ком сошлись звёзды. Обладая всем необходимым, он выбрал число 73.
            """)
with col5:
    st.image(r'media/winner.jpg', use_container_width=True)
st.markdown("#### __________________________________________________________")
st.markdown("""Далее представлена общая статистика ответов, сравнивая с предсказаниями
               на основе вида распределения выше, можно убедиться, что предсказания хорошо описывают общий вид
               подобных выборок, к сожалению, в среднем числа 73 получено не было, но это весьма закономерно.""")
selected_hist = st.selectbox("Выберите группу:", 
                              ["Добрые Самаритяне", "Добрые Самаритяне без уникальной информации и опыта включительно"])

with st.container(height=500):
    hists(known, 'green') if selected_hist == "Добрые Самаритяне" else hists(unkk, 'purple')
st.markdown("#### __________________________________________________________")
st.markdown("### :orange[Благодарю всех за участие, надеюсь вы узнали что-нибудь новое, а также это очередное \
            напоминание о том, что каждый из вас важен, в частности ты, именно ты, тот кто читает сейчас этот текст! \
            Коллективный разум обретает силу, когда каждый индивидуальный в нём существует и мыслит независимо. \
            Поэтому не забывай своей значимости, читатель]")
