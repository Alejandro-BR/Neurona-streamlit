import streamlit as st

st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

st.title("¡Hola neurona!")

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

with tab1:
    st.header("Una neurona con una entrada y un peso")

    w = st.slider("Peso", 0.0, 5.0, 1.0, key="t1slw")
    x = st.number_input(
    "Introduzca el valor de la entrada", value=0.0, key="t1inp")

    if st.button("Calcular la salida", key="btn1"):
        y = x * w
        st.write(f"La salida de la neurona es {y}")

with tab2:
    col1, col2 = st.columns(2)

    with col1:
        w0 = st.slider("Peso W0", 0.0, 5.0, 1.0, key="t2slw1")
        x0 = st.number_input(
        "Entrada X0", value=0.0, key="t2inp1")

    with col2:
        w1 = st.slider("Peso W1", 0.0, 5.0, 1.0, key="t2slw2")
        x1 = st.number_input(
        "Entrada X1", value=0.0, key="t2inp2")

    if st.button("Calcular la salida", key="btn2"):
        y = (x0 * w0) + (x1 * w1)
        st.write(f"La salida de la neurona es {y}")

with tab3:
    col1, col2, col3 = st.columns(3)

    # Tengo quue poner los numeros en subjetivo
    with col1:
        w0 = st.slider("Peso W0", 0.0, 5.0, 1.0, key="t3slw1")
        x0 = st.number_input(
        "Entrada X0", value=0.0, key="t3inp1")

    with col2:
        w1 = st.slider("Peso W1", 0.0, 5.0, 1.0, key="t3slw2")
        x1 = st.number_input(
        "Entrada X1", value=0.0, key="t3inp2")

    with col3:
        w2 = st.slider("Peso W2", 0.0, 5.0, 1.0, key="t3slw3")
        x2 = st.number_input(
        "Entrada X2", value=0.0, key="t3inp3")

    b = st.number_input(
        "Sesgo", value=0.0, key="b")

    if st.button("Calcular la salida", key="btn3"):
        y = (x0 * w0) + (x1 * w1) + (x2 * w2) + b
        st.write(f"La salida de la neurona es {y}")





st.write("© Alejandro Barrionuevo Rosado - CPIFP Alan Turing")