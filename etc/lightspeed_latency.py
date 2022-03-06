def lightspeed_latency(mi):
    """
    :param mi: miles between client and server
    :return: the roundtrip time, considering only the speed of light
    """
    km_per_mi = 1.60934
    m_per_km = pow(10, 3)
    speed_of_light_m_per_s = 3 * pow(10, 8)
    distance_m = mi * km_per_mi * m_per_km * 2  # multiply by 2 to account for both directions
    time_ms = (distance_m / speed_of_light_m_per_s) * pow(10, 3)
    return '{:.3} ms'.format(time_ms)


def la_to_oregon():
    mi = 860
    time = lightspeed_latency(mi)
    print(f'Roundtrip time from la to oregon: {time}')


if __name__ == '__main__':
    la_to_oregon()