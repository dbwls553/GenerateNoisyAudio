import get_signal_to_noise as stn
from math import sqrt

def calc_snr(signal, noise):
    """
    Calculate signal noise ratio.
    :param signal: (list)
    :param noise: (list)
    :return: (value) SNR(dB)
    """

    pass

def calc_ssnr(signal, noise, frame_size):
    """
    Calculate segmental signal noise ratio.
    :param signal: (list)
    :param noise: (list)
    :param frame_size: (int) ssnr frame size
    :return: (value) SSNR(dB)
    """

    pass

def change_power(input, power):
    """
    Change input power.
    :param input: (list)
    :param power: (value)
    :return: (list)
    """
    output = input.copy()
    ratio = 1
    while 1:
        POWER = 0
        for i in range(len(input)):
            POWER += pow(ratio * output[i], 2) / len(input)

        if (POWER > 0.9) & (POWER < 1.1):
            break
        else:
            ratio = sqrt(power / POWER)

    return output

def mix_noise(signal, noise, dB, snr_or_ssnr='snr', frame_size=None):
    """
    Mix noise to signal with specified dB. dB can be SNR or SSNR.
    :param signal: (list)
    :param noise: (list)
    :param dB: (value)
    :param snr_or_ssnr: 'snr' or 'ssnr'
    :param frame_size:  (int) only use in ssnr
    :return: (list)
    """

    pass