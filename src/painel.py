from sensores import Sensor


def linha_painel(sensor: Sensor) -> str:
    return f"{sensor.tag}: {sensor.valor():.1f} {sensor.unidade()} | {'ALERTA' if sensor.em_alerta() else 'OK'}"
