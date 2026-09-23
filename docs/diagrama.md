# Modelo a completar

Desenhe Sensor como classe abstrata, as três especializações e a dependência do painel em Sensor. Inclua as operações do contrato e marque as abstratas. O painel recebe uma referência; ele não possui os sensores.

classDiagram

class Sensor {
    <<abstract>>
    -_tag : string
    +tag() string
    +valor() double*
    +unidade() string*
    +atualizar(leitura : double) bool*
    +emAlerta() bool*
}

class SensorNivel {
    -valor_ : double
    +unidade() string
    +atualizar(leitura : double) bool
    +emAlerta() bool
}

class SensorPressão {
    -valor_ : double
    +valor() double
    +unidade() string
    +atualizar(leitura : double) bool
    +emAlerta() bool
}

class Painel {
    +linhaPainel(sensor : Sensor) string
}

Sensor <|-- SensorNivel
Sensor <|-- SensorTemperatura
Sensor <|-- SensorPressao

Painel ..> Sensor : consulta