segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

# Number of seconds in a minute: 60
# Number of seconds in an hour: 3600
# Number of seconds in a day: 86400

# print(segundos)
dias = segundos // 86400
segundos = segundos % 86400
# print(dias, segundos)
horas = segundos // 3600
segundos = segundos % 3600
# print(dias, horas, segundos)
minutos = segundos // 60
segundos = segundos % 60
print(dias,"dias,", horas,"horas,", minutos,"minutos e", segundos,"segundos.")
