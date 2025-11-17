print("\n=== Conversor de Tempo ===")

# Converter segundos para horas, minutos e segundos
total_segundos = 7265  # Exemplo: 7265 segundos

horas = total_segundos // 3600  # 1 hora = 3600 segundos
minutos = (total_segundos % 3600) // 60  # Resto dividido por 60
segundos = total_segundos % 60  # Resto final

print(f"{total_segundos} segundos = {horas}h {minutos}m {segundos}s")

# Converter idade em dias para anos, meses e dias
idade_dias = 10950  # Exemplo: 30 anos

anos = idade_dias // 365
meses = (idade_dias % 365) // 30
dias = idade_dias % 30

print(f"{idade_dias} dias ≈ {anos} anos, {meses} meses e {dias} dias")