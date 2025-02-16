import streamlit as st
from agno.models.openai import OpenAIChat
from parameters import airlines_list, set_bg_hack_url, countries_list, cities_list
from agents import transitguide, terminalguide, baggageguide, openai_api_key, serp_api_key

set_bg_hack_url()
st.title(":blue[AI Air Guide] ✈️")
st.subheader(":green[Enjoy smooth and well prepared travel!]")

if openai_api_key and serp_api_key:

    baggage, transit, terminal = st.tabs([":gray[Baggage]", ":gray[Transit]", ":gray[Terminal]"])
    with baggage:
        airline = st.selectbox(":gray[Which airline do you wish to travel with?]", airlines_list, index=None)
        domestic = st.radio(":gray[Are you traveling domestic or international?]", [":gray[Domestic]", ":gray[International]"])
        if st.button(":gray[Get Baggage information]"):
            with st.spinner(":gray[Getting Baggage information...]"):
                response = baggageguide.run(f"with {airline} travelling {domestic} and getting baggage information for checked bad, carry-on bag with weight and count limit", stream=False)
                st.write(response.content)
    with transit:
        city = st.selectbox(":gray[Which is the layover city?]", cities_list, index=None)
        passport = st.selectbox(":gray[Which country passport are you flying with?]", countries_list, index=None)
        if st.button(":gray[Get transit information]"):
            with st.spinner(":gray[Getting transit information...]"):
                response = transitguide.run(f"given the transit city {city} and the user passport/country {passport}, find the details about requirement of transit visa or any other kind of visa required or not required", stream=False)
                st.write(response.content)
    with terminal:
        airport = st.selectbox(":gray[Which airport you are flying from?]", cities_list, index=None)
        airline = st.selectbox(":gray[Which airline you are flying with?]", airlines_list, index=None)
        domestic = st.radio(":gray[Are you traveling domestic or international]", [":gray[Domestic]", ":gray[International]"])
        if st.button(":gray[Get terminal information]"):
            with st.spinner(":gray[Getting terminal information...]"):
                response = terminalguide.run(f"for given city/airport {airport}, find the terminal {airline} airline flies from for {domestic}", stream=False)
                st.write(response.content)

