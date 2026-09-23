from sensores import Sensor


def linha_painel(sensor: Sensor) -> str:
    return (
        f"{sensor.tag}: "
        f"{sensor.valor():.1f} "
        f"{sensor.unidade()} | "
        f"{'ALERTA' if sensor.em_alerta() else 'OK'}"
    )