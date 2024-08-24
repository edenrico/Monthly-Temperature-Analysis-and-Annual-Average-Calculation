# Função para obter o nome do mês por extenso
def get_month_name(month):
    months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
              "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    return months[month-1]

# Função para validar a entrada do mês
def get_valid_month():
    while True:
        try:
            month = int(input("Digite o número do mês (1-12): "))
            if 1 <= month <= 12:
                return month
            else:
                print("Erro: O mês deve ser um número entre 1 e 12.")
        except ValueError:
            print("Erro: Por favor, insira um número válido.")

# Função para validar a entrada da temperatura
def get_valid_temperature():
    while True:
        try:
            temp_str = input("Digite a temperatura máxima do mês em °C: ").replace(",", ".")
            temp = float(temp_str)
            if -60 <= temp <= 50:
                return temp
            else:
                print("Erro: A temperatura deve estar entre -60 e 50 graus Celsius.")
        except ValueError:
            print("Erro: Por favor, insira um número válido.")

# Função principal para coletar os dados, calcular e exibir os resultados
def main():
    temperatures = [None] * 12  # Lista para armazenar as temperaturas dos 12 meses

    print("Informe os dados meteorológicos de 2021:")

    # Coletar e armazenar os dados de temperatura para cada mês
    for i in range(12):
        while True:
            print(f"\nMês {i+1}:")
            month = get_valid_month() - 1  # Subtrai 1 para indexar corretamente na lista (0-11)
            if temperatures[month] is not None:
                print(f"Dados para o mês {get_month_name(month+1)} já foram inseridos. Redigite.")
            else:
                temperatures[month] = get_valid_temperature()
                break

    # Cálculos solicitados
    avg_max_temp = sum(temp for temp in temperatures if temp is not None) / 12
    scorching_months = sum(1 for temp in temperatures if temp is not None and temp > 33)
    hottest_month = temperatures.index(max(temperatures))
    coldest_month = temperatures.index(min(temperatures))

    # Exibição dos resultados
    print("\nResultados das análises:")
    print(f"Temperatura média máxima anual: {avg_max_temp:.2f}°C")
    print(f"Quantidade de meses escaldantes (temp > 33°C): {scorching_months}")
    print(f"Mês mais escaldante do ano: {get_month_name(hottest_month+1)} ({temperatures[hottest_month]}°C)")
    print(f"Mês menos quente do ano: {get_month_name(coldest_month+1)} ({temperatures[coldest_month]}°C)")

# Executa o programa
if __name__ == "__main__":
    main()
