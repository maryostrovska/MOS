import numpy as np
import time
import matplotlib.pyplot as plt

#рекурсивний алгоритм FFT для масиву x
#алгоритм для обчислення дискретного перетворення Фур'є (ДПФ)
def fft(x):
    n = len(x)
    if n <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    T = [np.exp(-2j * np.pi * k / n) * odd[k] for k in range(n // 2)]
    return [even[k] + T[k] for k in range(n // 2)] + \
           [even[k] - T[k] for k in range(n // 2)]

#генерація випадкового сигналу заданої довжини ()
def generate_signal(length):
    return np.random.randn(length)


x = generate_signal(64)


t0 = time.time() #запам'ятовуємо час початку обчислень.
y = fft(x) #обчислюємо FFT для сигналу x.
t1 = time.time() #час завершення обчислень
#print(t1,t0)

#змінні для обчислення кількості операцій множення та додавання в FFT
num_mults = 0
num_adds = 0
for n in range(len(x)):
    num_mults += n/2 * np.log2(n + 1)
    num_adds += n* np.log2(n + 1) - 2*(n/2 * np.log2((n + 1)/2))


print("Час обчислення: {:.5f} с".format(t1 - t0))
print("\nКількість операцій множення: {:.0f}".format(num_mults))
print("\nКількість операцій додавання: {:.0f}".format(num_adds))
print("\nВхідний сигнал:", x)
print("\nРезультат ШПФ:")
for i in range(len(y)):
    print("C_{} = {}".format(i, y[i]))

#Амплітудний та фазовий спектри FFT
fft_abs = np.abs(y)
fft_phase = np.angle(y)

fig, axs = plt.subplots(2, 1, figsize=(8, 8))
axs[0].bar(np.arange(len(fft_abs)), fft_abs, align='center', alpha=0.5, color="green")
axs[0].set_title("Спектр амплітуд")
axs[0].set_xlabel("Частота")
axs[0].set_ylabel("Амплітуда")
axs[1].bar(np.arange(len(fft_phase)), fft_phase, align='center', alpha=0.5, color="green")

axs[1].set_title("Спектр фаз")
axs[1].set_xlabel("Частота")
axs[1].set_ylabel("Фаза")
plt.show()