# Algoritma Fast Fourier Transform

Algoritma untuk menghitung transforamasi fourier, merupakan suatu teknik matemat8ka untuk menganalisis frekuensi komponen suatu teknik matematika untuk menganalisis frekuensi komponen dalam suatu sinyal FFT

FFT (sinyal): dapat digunakan untuk mengubah sinyal dari domain waktu ke domain frekuensi.

    FFT (signal):
    N = panjang(signal)

        Jika N adalah bilangan ganjil:
            return "signal length must be even"

        if N == 1 :
            return signal

        Divide signal into even parts and odd parts
        even_signal= [signal[2k] for k from 0 until N/2 - 1]

        odd_signal= [signal [2k+1] for k from 0 until N/2 -1]
