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
            data = {
                "zona": "A"
            }
            response = requests.post("http://api:8000/predict-risks", files=files, data=data)

            st.subheader("🔍 Evaluación del riesgo:")

            data = response.json()
            if "resultados" in data:
                for clase, resultado in data["resultados"].items():
                    st.markdown(f"### 🛑 Pictograma detectado: `{clase}`")
                    if isinstance(resultado, dict):
                        st.write(f"**Riesgo estimado:** {resultado.get('riesgo_estimado', 'N/A')}")
                        st.write("**Motivos:**")
                        for motivo in resultado.get("motivos", []):
                            st.markdown(f"- {motivo}")
                        sugerencias = resultado.get("sugerencias")
                        if sugerencias:
                            st.write("**Sugerencias:**")
                            for sugerencia in sugerencias:
                                st.markdown(f"- {sugerencia}")
                    else:
                        st.warning(resultado)
            else:
                st.json(data)

            status.update(label="✅ Evaluación completada", state="complete")

        except Exception as e:
            status.update(label=f"❌ Error: {e}", state="error")
