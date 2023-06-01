import numpy as np
import matplotlib.pyplot as plt
import statistics
import warnings
from matplotlib import MatplotlibDeprecationWarning
warnings.filterwarnings("ignore", category=MatplotlibDeprecationWarning)

#обчислення точних значень послідовності
def exact_values(x, A, n, phi):
    return A * np.sin(n * x + phi) + n


#генерація послідовності з похибкою для заданих параметрів
def generate_sequence(n, N, A, phi, a, b):
    #генерація масиву x, що містить N значень, рівномірно розподілених від a до b
    x = np.linspace(a, b, N)
    #обчислення точних значень сигналу для кожного значення x
    y = exact_values(x, A, n, phi)


 #генерується масив error, який містить N випадкових чисел з розподілу uniform від -max_error до max_error.
    #Кількість чисел у масиві відповідає кількості точок в послідовності.
    # Цей масив похибки додається до точних значень сигналу, щоб отримати фінальну послідовність Y

    #обмеження похбки
    max_error = 0.05 * A
    error = np.random.uniform(-max_error, max_error, N)
    y += error

    return x, y


def plot_result(x, y, exact_values=None):
    plt.figure()
    plt.plot(x, y, color='green', label='Згенерована послідовність')
    if exact_values is not None:
        plt.plot(x, exact_values, color='blue', linestyle='-', label='Точне значення')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Згенерована послідовність')
    plt.legend()
    plt.show()


#порівнюємо наближені значення з точними значеннями послідовності та обчислюємо абсолютні та відносні похибки.
def compare_approximations(approximation_values, exact_values):
    absolute_errors = np.abs(approximation_values - exact_values)
    relative_errors = []
    for i in range(len(approximation_values)):
        if exact_values[i] != 0:
            relative_errors.append(abs(absolute_errors[i] / exact_values[i]))

    max_absolute_error = np.max(absolute_errors)
    min_absolute_error = np.min(absolute_errors)

    max_relative_error = np.max(relative_errors)
    min_relative_error = np.min(relative_errors)

    print("Максимальна абсолютна похибка:", max_absolute_error)
    print("Мінімальна абсолютна похибка:", min_absolute_error)
    print(f"Максимальна відносна похибка: {max_relative_error*100} %")
    print(f"Мінімальна відносна похибка: {min_relative_error*100} %")


def main():
    n = 34
    N = n * 1000
    A = 1.0
    phi = 3 * np.pi / 2
    a = 0
    b = np.pi / 4.5

    x, y = generate_sequence(n, N, A, phi, a, b)

# функція для обчислення середніх значень: арифметичного, гармонійного та геометричного
    arithmetic_mean_value = np.mean(y)
    geometric_mean_value = statistics.geometric_mean(y)
    harmonic_mean_value = statistics.harmonic_mean(y)

    print("Середнє арифметичне :", arithmetic_mean_value)
    print("Середнє геометричне :", geometric_mean_value)
    print("Середнє гармонійне :", harmonic_mean_value)

    exact_vals = exact_values(x, A, n, phi)
    plot_result(x, y, exact_vals)

    approximation_arithmetic_values = np.array([arithmetic_mean_value] * N)
    approximation_geometric_values = np.array([geometric_mean_value] * N)
    approximation_harmonic_values = np.array([harmonic_mean_value] * N)

    print("\nДля середнього арифметичного:")
    compare_approximations(approximation_arithmetic_values, exact_vals)
    print("\nДля середнього геометричного:")
    compare_approximations(approximation_geometric_values, exact_vals)
    print("\nДля середнього гармонійного:")
    compare_approximations(approximation_harmonic_values, exact_vals)

    plt.figure()
    plt.plot(x, exact_vals, color='black', label='Точне значення')
    plt.plot(x, approximation_arithmetic_values, color='blue', label='Середнє арифметичне наближене значення')
    plt.plot(x, approximation_geometric_values, color='grey', label='Середнє геометричне наближене значення')
    plt.plot(x, approximation_harmonic_values, color='green', label='Середнє гармонійне наближене значення')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Порівняння точного та наближеного значень')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
