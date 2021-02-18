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

def calc_power(input):
    """
    Calculate power of input.
    :param input: (list)
    :return: (value)
    """
    sum = 0
    for n in input:
        sum += pow(n, 2)
    return sum / len(input)


def change_power(input, power):
    """
    Change input power.
    :param input: (list)
    :param power: (value)
    :return: (list)
    """
    input_power = calc_power(input)
    ratio = sqrt(power/input_power)

    output = input.copy()
    for i in range(len(input)):
        output[i] = input[i]*ratio
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
    if snr_or_ssnr == 'snr':
        pass
    elif snr_or_ssnr == 'ssnr':
        pass
    else:
        raise Exception("ERROR: You must select only in range of snr or ssnr.")