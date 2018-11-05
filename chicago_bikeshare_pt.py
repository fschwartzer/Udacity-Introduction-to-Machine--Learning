# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
    
n = 0
while n < 20:
    print("Amostra " + str(n+1) + ":")
    print(data_list[n])
    n += 1

""" n = 0 ---> variável para iniciar a contagem do loop
    O primeiro print é para identificar o número da amostra
    O segundo print imprime as amostras da posição 0 até 19
"""

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")

n = 0
while n < 20:
    print("Amostra " + str(n+1) + ": " + data_list[n][6])
    n += 1
    
""" n = 0 ---> variável para iniciar a contagem do loop
    Print do elemento da 6ª coluna, com a posiçaõ 'n' da linha variando conforme o loop
"""
   
# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    column_list = []
    for i in data :
        column_list.append(i[index])
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    return column_list

""" n = 0 ---> variável para iniciar a contagem do loop
    Print do elemento da 6ª coluna, com a posiçaõ 'n' da linha variando conforme o loop
"""
# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.
male = 0
female = 0

for gender in data_list:
    if gender[-2] == "Male":
        male += 1
    elif gender[-2] == "Female":
        female += 1

""" male e female inciando a contagem de 0 (zero)
    Loop for que avalia o gênero dentro da lista de dados.
    Se o elemento da penúltima linha for 'Male", acrescenta 1 à contagem do gênero masculino.
    Se o elemento da penúltima linha for 'Fenale", acrescenta 1 à contagem do gênero feminino.
"""

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    male = 0
    female = 0
    for gender in data_list:
        if gender[-2] == "Male":
            male += 1
        elif gender[-2] == "Female":
            female += 1
    return [male, female]

""" Define o procedimento de contagem de gêneros na lista.
    male e female inciando a contagem de 0 (zero)
    Loop for que avalia o gênero dentro da lista de dados.
    Se o elemento da penúltima linha for 'Male", acrescenta 1 à contagem do gênero masculino.
    Se o elemento da penúltima linha for 'Fenale", acrescenta 1 à contagem do gênero feminino.
    Retorna matriz com o primeiro elemento sendo a contagem do gênero masculino e o segundo elemento a contagem do gEnero feminino.
"""

print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list):
    male = 0
    female = 0
    for gender in data_list:
        if gender[-2] == "Male":
            male += 1
        elif gender[-2] == "Female":
            female += 1
    
    if male > female:
        return "Masculino"
    elif male < female:
        return "Feminino"
    else:
        return "Igual"
    answer = ""
    
    return answer

""" Define o procedimento de verificação do gênero mais popular.
    male e female inciando a contagem de 0 (zero)
    Loop for que avalia o gênero dentro da lista de dados.
    Se o elemento da penúltima linha for 'Male", acrescenta 1 à contagem do gênero masculino.
    Se o elemento da penúltima linha for 'Fenale", acrescenta 1 à contagem do gênero feminino.
    Se male maior que female, retorna Masculino.
    Se male menor que female, retorna Feminino.
    Se nenhuma das condições for atendida, retorna Igual.
    A resposta é uma string.
    Retorna a resposta.
"""

print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

user_types_list = column_to_list(data_list, -3)
types = ["Customer", "Subscriber"]
def count_user_types(data_list):
    customer = 0
    subscriber = 0
    for user_types in data_list:
        if user_types[-3] == "Customer":
            customer += 1
        elif user_types[-3] == "Subscriber":
            subscriber += 1
    return [customer, subscriber]
    
quantity = count_user_types(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de usuário')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de Usuário')
plt.show(block=True)

""" Transpõe os dados da antepenultima coluna em uma lista.
    Define os tipos de dados a serem plotados como "Customer" e "Subscriber".
    Define um procedimento para contagem de "Customer" e "Subscriber".
    customer e subscriber inciando a contagem de 0 (zero)
    Loop for que conta o tipo de usuário dentro da lista de dados.
    Se o elemento da penúltima linha for 'Customer', acrescenta 1 à contagem de 'Customer'.
    Se o elemento da penúltima linha for 'Subscriber", acrescenta 1 à contagem de 'Subscriber'.
    Retorna lista com 1º elemento sendo a contagem de "Customer" e 2º elemento sendo a contagem de "Subscriber".
    As quantidades para a plotagem do gráfico são obtidas no procedimento acima descrito.
    A posição Y do gráfico é definida pelo tamanho da amostra de cada tipo de usuário.
    Plota barras com as quantidades de tipos de usuários.
    O rótulo do eixo Y é 'Quantidade'.
    O rótulo do eixo X é 'Tipo de usuário'.
    Plota traços para parâmetro de quantidades.
    Plota o título Quantidade por Tipo de Usuário.
"""

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque existem amostras sem a informação do gênero do usuário."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
trip_duration_list = [int(i) for i in trip_duration_list]
trip_duration_list = sorted(trip_duration_list)
min_trip = int(trip_duration_list[0])
max_trip = int(trip_duration_list[-1])
mean_trip = sum(trip_duration_list) / len(trip_duration_list)
mean_trip = round(mean_trip)
median_pos = (len(trip_duration_list) + 1) / 2
median_pos = int(median_pos)
median_trip = trip_duration_list[median_pos]

""" Transpõe os dados da terceira coluna em uma lista.
    Converte os dados de trip_duration_list em integer.
    Classifica os dados de trip_duration_list do menor para o maior.
    min_trip = primeiro elemento da lista classificada.
    max_trip = último elemento da lista classificada.
    mean_trip = valor arredondado da razão do somatório dos elementos de trip_duration_list pela sua extensão.
    median_trip = defini a posição do meio da lista e pega o valor que se encontra na posição.
"""

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = []
start_stations = column_to_list(data_list, 3)
user_types = set(start_stations)

"""
    Cria nova lista start_stations
    start_stations é uma lista dos elementos da 4ª coluna transpostos.
    user_types é a lista start_stations sem elementos repetidos.
"""

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:

"""
      Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x.

      """

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")

"""
    item_types = pega a lista de column_list sem elementos repetidos e converte em lista para fornecer o índice para o procedimento seguinte.
    count_items = loop while onde x é o índice, que varia até o limite do comprimento da lista, e que vai contando a quantidade de cada item e incluindo em uma lista.
"""

a = input("Resposta: ")

if a == "yes":
    def count_items(column_list):
        item_types = []
        count_items = []
        
        item_types = set(column_list)
        item_types = list(item_types)
        
        x = 0
        while x < len(item_types):
            item = column_list.count(item_types[x])
            count_items.append(item)
            x += 1
  
        return item_types, count_items


    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------