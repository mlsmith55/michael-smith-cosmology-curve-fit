speed_of_light = 299792

Hubble_initial = 70
Hubble_min = 60
Hubble_max = 80

Matter_initial = 0.5
Matter_min = 0.01
Matter_max = 0.99

curve_fit_parameter_settings = {
    'p0': [Hubble_initial, Matter_initial],
    'bounds': (
        [Hubble_min, Matter_min],
        [Hubble_max, Matter_max]
    )
}