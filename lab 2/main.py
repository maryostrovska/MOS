import numpy as np
import warnings
from matplotlib import MatplotlibDeprecationWarning
import matplotlib.pyplot as plt
import time

warnings.filterwarnings("ignore", category=MatplotlibDeprecationWarning)

N = 64

#Функція fourier_coefficient(x, k) обчислює коефіцієнт Фур'є для заданого сигналу x і певного індексу k.
def fourier_coefficient(x, k):
    N = len(x)
    Ak = np.sum(x * np.cos(2*np.pi*k*np.arange(N)/N))
    Bk = np.sum(x * np.sin(2*np.pi*k*np.arange(N)/N))
    Ck = Ak + 1j*Bk
    # кількість операцій
    num_multiplications = 3 * N
    num_additions = N
    return Ck, num_multiplications, num_additions

#Функція discrete_fourier_transform(x) виконує дискретне перетворення Фур'є (ДПФ) для заданого сигналу x.
def discrete_fourier_transform(x):
    N = len(x)
    C = np.zeros(N, dtype=np.complex128)
    # лічильники кількості операцій
    total_multiplications = 0
    total_additions = 0
    for k in range(N):
        C[k], num_multiplications, num_additions = fourier_coefficient(x, k)
        total_multiplications += num_multiplications
        total_additions += num_additions
    print(f"кількість операцій множення: {total_multiplications}")
    print(f"кільксть операцій додавання: {total_additions}")
    print(f"кільксть операцій віднімання: {total_additions-N}")
    return C

# генеруємо масив випадкових даних
x = np.random.rand(N + 10)

# замір часу на початку
start_time = time.time()

# обчислюємо ДПФ
C = discrete_fourier_transform(x)

# обчислення спектру амплітуд
amplitude_spectrum = abs(C)

# обчислення спектру фаз
phase_spectrum = np.angle(C)

# вивід результатів та часу виконання
for k in range(len(C)):
    print(f"\nC[{k}] = {C[k]}")

# замір часу в кінці та вивід часу виконання
end_time = time.time()
print(f"Execution time: {end_time - start_time:.5f} seconds")

# побудова графіку спектру амплітуд
plt.figure(figsize=(8, 6))
plt.stem(amplitude_spectrum, use_line_collection=True)
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('Amplitude Spectrum')
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.show()

# побудова графіку спектру фаз
plt.figure(figsize=(8, 6))
plt.stem(phase_spectrum, use_line_collection=True)
plt.xlabel('Frequency')
plt.ylabel('Phase')
plt.title('Phase Spectrum')
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.show()