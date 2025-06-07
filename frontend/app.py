import streamlit as st
import requests

st.set_page_config(page_title="Evaluador de Riesgo", layout="centered")
st.title("🧪 Evaluador de Riesgo por Imagen")

uploaded_file = st.file_uploader("Subí una imagen de la zona de trabajo", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Imagen cargada", use_container_width=True)

    with st.status("Enviando al backend...", expanded=False) as status:
        try:
            files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
            response = requests.post("http://api:8000/predict-risks", files=files)

            st.subheader("🔍 Evaluación del riesgo:")
            try:
                st.json(response.json())
            except:
                st.write("Respuesta (no JSON):")
                st.text(response.text)

            status.update(label="✅ Evaluación completada", state="complete")

        except Exception as e:
            status.update(label=f"❌ Error: {e}", state="error")
