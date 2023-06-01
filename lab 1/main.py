import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x * np.sin(np.pi * x)


def calculate_fourier_series(n, b_k):
    # Обчислення ряду Фур'є для заданого n та коефіцієнтів b_k
    series_sum = np.zeros_like(x)
    for i in range(1, n + 1):
        series_sum += b_k[i] * np.sin(i * np.pi * x / interval_length)
    return series_sum


def plot_approximation(N, b_k):
    fig, ax = plt.subplots()
    ax.set_title('Graph of approximation in the interval ({},{})'.format(graph_left_boundary.__round__(2),
                                                                         graph_right_boundary.__round__(2)))

    # Відображення апроксимації ряду Фур'є
    for n in range(1, min(N + 1, 11)):
        y = calculate_fourier_series(n, b_k)
        plt.plot(x, y, label=f"N={n}")

    # Відображення вашої функції
    plt.plot(x, x * np.sin(np.pi * x), label='n * np.sin(n * np.pi * x)', color='red')

    plt.legend(loc='upper right', fontsize='xx-small')
    ax.grid()
    plt.show()


# Параметри
interval_length = 2
num_samples = 1000
graph_left_boundary = -1
graph_right_boundary = 1

# Генерація точок на інтервалі
x = np.linspace(graph_left_boundary, graph_right_boundary, num_samples)

# Обчислення коефіцієнтів Фур'є
b_k = {}
for n in range(1, 11):
    b_k[n] = 2 / (n * np.pi) * (1 - np.cos(n * np.pi))

# Побудова графіку апроксимації
plot_approximation(10, b_k)


# графік гармонійних коефіцієнтівs
def plot_harmonics(a_k, b_k):
    #творення нової фігури (графіка) з заданим розміром 8х8, використовуючи fig = plt.figure(figsize=(8, 8))
    fig = plt.figure(figsize=(8, 8))

    # Визначаємо розташування осей графіків за допомогою subplot2grid
    ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
    ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=3)

    # Графік a_k
    ax1.stem([0] + a_k)
    ax1.set_xlabel('k')
    ax1.set_ylabel('a(k)')
    ax1.set_title('Graph of harmonics for a_k')

    # Графік b_k
    ax2.stem(range(1, N + 1), b_k)
    ax2.set_xlabel('k')
    ax2.set_ylabel('b(k)')
    ax2.set_title('Graph of harmonics for b_k')
    ax2.set_xticks(range(1, N + 1))
    ax2.set_xticklabels([f'{i}' for i in range(1, N + 1)])

    # Розтягуємо графіки на весь рядок
    plt.tight_layout()

    # Показуємо фігуру
    plt.show()


# відносну похибку апроксимації ряду Фур’є
def calculate_approximation_relative_error(N, b_k):
    # Calculate the Fourier series approximation and exact function values at each point in the interval
    y_approx = [calculate_fourier_series(N, b_k, x_i) for x_i in x]
    y_exact = [f(x_i) for x_i in x]

    # відносна похибка в кожній точці
    relative_error = []
    for i in range(0, len(x)):
        relative_error.append(np.abs((y_approx[i] - y_exact[i]) / (y_exact[i] + 1e-10)))

    # графік відносної похибки
    fig, ax = plt.subplots()
    ax.plot(x, relative_error)
    ax.set_title('Approximation error')
    ax.grid()
    plt.show()

    return relative_error


# вихідна функція
plot_function()

# викликаємо функцію для обчислення коефіцієнтів Фур'є
a_0, a_k, b_k = calculate_fourier_coefficients(N)

#  графік наближення функції в ряд Фур’є
plot_approximation(N, b_k)

# графік гармонійних коефіцієнтів
plot_harmonics(a_k, b_k)

# відносну похибку апроксимації ряду Фур’є
relative_error = calculate_approximation_relative_error(N, b_k)

# результати у файл

with open('fourier_series_results.txt', 'w') as file:
    file.write('N = {}\n'.format(N))
    file.write('a_0 = {}\n'.format(a_0))
    file.write('a_k\tb_k\n')  # заголовок стовпчика
    for i in range(1, len(a_k)):
        file.write('{}\t{}\n'.format(a_k[i], b_k[i]))  # записуємо кожен елемент у стовпчик
    file.write('Похибка наближення = {}\n\n'.format(relative_error))










