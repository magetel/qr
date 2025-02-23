import streamlit as st 
st.logo("logo-aedas.svg")




#st.title('Bienvenido a AEDAS Homes')
#st.header('Gestión de incidencias postventa')

#st.divider()
#st.subheader('Promoción: KANE')
st.subheader('Vivienda en KANE, Bloque 1, Escalera 1, Planta 2, Letra B')

#st.divider()
st.info('Incidencia 325416_001, oficio PINTURA', icon="ℹ️")

st.text_area('Por favor, describa el trabajo ralizado')
#img_file_buffer = st.camera_input("Adjuntar fotografía",label_visibility="collapsed")
st.button("Adjuntar fotografía")

st.text_input('Nombre y apellidos')
st.text_input('DNI del firmante')
#st.divider()

#options = ["Conforme", "No conforme"]
#selection = st.segmented_control(
#    "Conformidad con la ejecución de la tarea", options, selection_mode="single", default="Conforme")

on = st.toggle("¿Conforme con la ejecución?",value=1)

if on:
    st.write("Conforme con la ejecución de la tarea")
else:
    st.write("No conforme")
st.text_area('Firma del propietario-contacto')
#st.divider()
if st.button("Enviar CONFORMIDAD"):
    if on:
        st.success('Gracias por su confirmidad!', icon="✅")
    else:
        st.warning('Contactaremos con usted lo más rápido posible', icon="⚠️")


