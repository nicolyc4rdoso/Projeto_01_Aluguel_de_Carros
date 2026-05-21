import streamlit as st
st.write("ARMY - Aluguel De Carros")
st.sidebar.title("buick super")
st.sidebar.image("ARMY.png")

carros = ["Buick super","ferrari","chevrolet bel air","Lamborghini","mclaren"]

opçao = st.sidebar.selectbox("escolha o carro que foi alugado", carros)

st.image(f"{opçao}.png")
st.markdown(f"## Você Alugou o Modelo:{opçao}")
st.markdown("---")

dias = st.text_input(f"Por quantos dias o {opçao} foi alugado?")
km = st.text_input(f"quantos km você rodou com o {opçao}?")

if opçao == "Buick super":
    diaria = 2000

elif opçao == "ferrari":
    diaria = 8100

elif opçao == "chevrolet bel air":
    diaria = 3500


elif opçao == "Lamborghini":
    diaria = 7000

elif opçao == "mclaren":
    diaria = 10000

if st.button("Calcular"):
    dias = int(dias)
    km = float(km)

    total_dias = dias *diaria
    total_km = km * 8.15
    aluguel_total = total_dias+total_km

    st.warning(f"Você alugou o {opçao} por {dias} dias e rodou {km} km.O valor total a pagar é R${aluguel_total:.2f}")