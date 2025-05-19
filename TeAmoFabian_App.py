
import streamlit as st

st.set_page_config(page_title="¿Me amas?", page_icon="💖", layout="centered")

st.markdown("## Hola Fabián 💖")
st.markdown("### Tengo una pregunta para ti...")

respuesta = st.text_input("¿Me amas?")

if respuesta:
    A = respuesta.strip()

    if A == "Sí":
        st.success("Yo te amo más mi amor ❤️")
    elif A == "si":
        st.success("Qué bello amorcito, yo te amo más <3")
    elif A == "Obvio":
        st.success("Yo sabía que ibas a decir que sí mi amor ❤️")
    elif A == "obvio":
        st.success("Es obvio que me ibas a amar precioso... yo te amo más 💋")
    elif A == "no":
        st.error("Ya lo sabía, mejor vete con la otra culero")
    elif A == "No":
        st.error("Yo menos, qué bueno que te enteraste, bai.")
    elif A == "non":
        st.warning("Si vas a decirme que no me amas, al menos escríbelo bien... Mmgbo")
    elif A == "Non":
        st.warning("Si vas a decirme que no, al menos escríbelo bien... Mmvrg")
    elif A == "Tonota":
        st.info("Tú también eres un tonoto. No me hables más, bai")
    elif A == "tonota":
        st.info("Tonoto tú. Súper tonoto. Mega tonoto")
    elif A == "Fabian":
        st.balloons()
        st.success("Felicidades, has probado varias combinaciones pendejas y por fin has acertado una, te mereces una galleta ✨🍪")
    elif A == "Fabian y Johanna":
        st.balloons()
        st.success("❤️️Juntos por siempre❤️")
    elif A == "Miau":
        st.info("Miau para ti también")
    elif A == "miau":
        st.info("Cuando le dije eso a mi gata, me sacó la madre y me amenazó que no vuelva a estar hablando de su mamá")
    elif A == "te amo":
        st.success("Y yo te amaré más, mucho más")
    elif A == "Te amo":
        st.success("Te amo Fabián, con todo mi corazoncito de pollo")
    else:
        st.warning("Prueba otra cosa wei, así no se supone que debías responder")
