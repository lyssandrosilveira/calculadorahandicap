# -*- coding: utf-8 -*-
"""calculadora_handicap.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bvJNe17P1KhilXc_gwsOFy7qQ5__jn-J
"""

import streamlit as st

def calcular_odd_handicap(probabilidade_casa, probabilidade_visitante, probabilidade_empate):
    probabilidade_vitoria = probabilidade_casa + probabilidade_empate
    odd_linha_05 = 1 / probabilidade_casa
    odd_linha_00 = 1 / probabilidade_vitoria
    odd_linha_025 = (odd_linha_00 + odd_linha_05) / 2
    return round(odd_linha_025, 2)

def main():
    st.title("Cálculo de Odd para Handicap Asiático -0.25")
    st.write("Digite as probabilidades dos times para calcular a odd do handicap asiático -0.25")

    probabilidade_casa = st.number_input("Probabilidade de vitória do time da casa", min_value=0.0, max_value=1.0, step=0.01)
    probabilidade_visitante = st.number_input("Probabilidade de vitória do time visitante", min_value=0.0, max_value=1.0, step=0.01)
    probabilidade_empate = st.number_input("Probabilidade de empate", min_value=0.0, max_value=1.0, step=0.01)

    if st.button("Calcular Odd"):
        odd_handicap = calcular_odd_handicap(probabilidade_casa, probabilidade_visitante, probabilidade_empate)
        st.write("Odd Justa HA -0.25:", odd_handicap)

# Exibe o crédito do desenvolvedor
    st.write("Desenvolvido por Lyssandro Silveira")

if __name__ == "__main__":
    main()
