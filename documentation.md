# Documentação do Projeto de Previsão do Titanic

1. Entendimento do Problema
O objetivo do projeto é prever se um passageiro do Titanic sobreviveu ou não ao desastre, utilizando características como idade, sexo, classe socioeconômica, e outras variáveis presentes no dataset. A métrica principal de avaliação do modelo será a acurácia, além de outras métricas como Precision, Recall, F1-score e AUC-ROC.
    - Qual o problema?
    O problema a ser resolvido é a previsão da sobrevivência dos passageiros do Titanic. A pergunta central é: "Quais fatores influenciam a sobrevivência dos passageiros?".

    - Qual o experimento proposto?
    O experimento proposto envolve a aplicação de técnicas de aprendizado de máquina para modelar a relação entre as características dos passageiros e suas chances de sobrevivência. O objetivo é treinar um modelo usando um conjunto de dados de treinamento e avaliar sua performance em um conjunto de validação ou teste.

    - Resultados esperados
        - Um modelo capaz de prever a sobrevivência de passageiros com uma boa acurácia.
        - Identificação das características mais relevantes a sobrevivência.
        - Apresentação de visualizações que ajudem a comunicar os resultados de forma clara e eficaz.

2. Coleta e Análise Exploratória de Dados
Foi utilizado o dataset do Titanic, que contém 891 amostras, com variáveis categóricas e numéricas, como:
Categóricas: Sex, Embarked, Pclass.
Numéricas: Age, Fare, SibSp (número de irmãos/cônjuges a bordo), Parch (número de pais/filhos a bordo).
A análise exploratória inicial identificou a distribuição dessas variáveis e as correlações com o resultado de sobrevivência.
Valores ausentes foram tratados, especialmente nas variáveis Age e Embarked, enquanto outliers no Fare foram analisados.

3. Preparação dos Dados
Durante a preparação dos dados:
    - Valores ausentes foram imputados com a mediana para variáveis numéricas e com a moda para variáveis categóricas.
    - Variáveis categóricas foram codificadas com o método de codificação de variáveis dummy (one-hot encoding) para transformar Sex, Embarked, e Pclass.

4. Avaliação dos Modelos

| Modelo              | Acurácia      |  Class         | Precision     | Recall        | F1-score      |
| -------------       | ------------- | -------------  | ------------- | ------------- | ------------- |
| Regressão Logística | 0.77          | 0              | 0.79          | 0.86          | 0.82          |
| Regressão Logística |               | 1              | 0.75          | 0.63          | 0.68          |
| Random Forest       | 0.76          | 0              | 0.79          | 0.83          | 0.81          |
| Random Forest       |               | 1              | 0.71          | 0.65          | 0.68          |
| SVM                 | 0.78          | 0              | 0.79          | 0.87          | 0.83          |
| SVM                 |               | 1              | 0.76          | 0.63          | 0.67          |
| Gradient Boosting   | 0.80          | 0              | 0.80          | 0.91          | 0.85          |
| Gradient Boosting   |               | 1              | 0.81          | 0.63          | 0.71          |

O Gradient Boosting foi escolhido como o melhor modelo porque apresentou a melhor performance em termos de acurácia, ROC-AUC, e capacidade de generalização.
Ele também permite ajustar hiperparâmetros como a taxa de aprendizado, número de estimadores, e profundidade das árvores, o que foi feito usando o método Grid Search, garantindo que o modelo tenha sido otimizado adequadamente.
Os resultados da validação cruzada mostram que o modelo Gradient Boosting tem uma média de acurácia de 83.06%, com um desvio padrão de 0.0531 (aproximadamente 5.31%).
    - Média de acurácia (83.06%): Apresenta um desempenho sólido e consistente em diferentes divisões dos dados.
    - Desvio padrão (5.31%): Desvio relativamente baixo indica que o modelo é robusto e não sofre grandes variações de desempenho entre os diferentes folds. Ou seja, ele é consistente e tende a generalizar bem para novos dados.

5. Conclusão
    - Resultados Esperados
        - O modelo de Gradient Boosting apresentou uma acurácia de 0.80, indicando uma boa capacidade de prever a sobrevivência dos passageiros do Titanic.
        - As métricas de precision, recall e F1-score para a classe de sobreviventes (1) mostraram resultados que, embora não perfeitos, indicam um modelo funcional e com potencial de aplicação prática.
        - A validação cruzada resultou em uma média de acurácia de 0.8306, com um desvio padrão baixo, sugerindo que o modelo é robusto e consistente.
    - Possíveis Melhorias do Modelo
        - Tratamento de Valores Ausentes: Explorar métodos mais sofisticados para imputar valores ausentes, como o uso de algoritmos de aprendizado de máquina para prever os valores ausentes em vez de métodos simples de média ou mediana.
        - Engenharia de Atributos: Criar novas variáveis que possam capturar informações não explícitas nos dados, como a interação entre variáveis ou binarização de variáveis categóricas com múltiplas categorias.
        - Hiperparâmetros: Realizar uma busca mais extensa na otimização de hiperparâmetros usando técnicas como Grid Search ou Random Search para melhorar o ajuste do modelo.
        - Modelos Alternativos: Testar outros modelos, como Redes Neurais ou modelos de ensemble diferentes, para verificar se há alguma melhora no desempenho.
