print("\n=== Sistema de Radar ===")

# Configurações do radar (constantes)
VELOCIDADE_MAXIMA = 60  # km/h
LOCAL_RADAR = 100       # km na estrada
ALCANCE_RADAR = 1       # km de alcance

# Dados do carro
velocidade_carro = 65
local_carro = 100

# Verificações
carro_no_radar = (local_carro >= LOCAL_RADAR - ALCANCE_RADAR and 
                  local_carro <= LOCAL_RADAR + ALCANCE_RADAR)
velocidade_excedida = velocidade_carro > VELOCIDADE_MAXIMA
carro_multado = carro_no_radar and velocidade_excedida

# Resultados
print(f"Velocidade do carro: {velocidade_carro} km/h")
print(f"Local do carro: {local_carro} km")
print(f"Carro no alcance do radar: {carro_no_radar}")
print(f"Velocidade excedida: {velocidade_excedida}")
print(f"Carro multado: {carro_multado}")

if carro_multado:
    multa = 195.23  # Valor da multa
    print(f"\n🚨 MULTA APLICADA: R$ {multa:.2f}")
else:
    print("\n✅ Nenhuma infração detectada")