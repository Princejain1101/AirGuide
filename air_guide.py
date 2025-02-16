from textwrap import dedent
from agno.agent import Agent
from agno.tools.serpapi import SerpApiTools
import streamlit as st
from agno.models.openai import OpenAIChat
from parameters import airlines_list, set_bg_hack_url, countries_list, cities_list

set_bg_hack_url()
st.title(":blue[AI Air Guide] ✈️")
st.subheader(":green[Enjoy smooth and well prepared travel!]")

# Get OpenAI API key from user
openai_api_key = st.secrets["openai_api_key"]
#st.text_input("Enter OpenAI API Key to access GPT-4o", type="password")

# Get SerpAPI key from the user
serp_api_key = st.secrets["serp_api_key"]
#st.text_input("Enter Serp API Key for Search functionality", type="password")

if openai_api_key and serp_api_key:
    airlineguide = Agent(
        name="Airlineguide",
        role="Searches for airline general information",
        model=OpenAIChat(id="gpt-4o", api_key=openai_api_key),
        description=dedent(
            """\
        You are a world-class Airline guide. Given an airline and domestic/international and the information user is looking for,
        find the airline website and also the blogposts to find relevant travel details about the airline.
        Then in all these websites, search for requested information, analyze and summarize the results.
        Generate and return in 10 to 20 lines of text.
        """
        ),
        instructions=[
            "Given an airline and domestic/international user wants to travel for, find airline website and other related partner websites.",
            "On each of these websites, search for the information user is looking for and analyze the results.",
            "From these results, summarize the results across all websites and provide results in 10-20 lines.",
            "Remember, the quality of the results in important.",
            "Make sure to include links of the source."
        ],
        tools=[SerpApiTools(api_key=serp_api_key)],
        add_datetime_to_instructions=True,
    )
    transitguide = Agent(
        name="Transitguide",
        role="Searches for transit visa requirements for a given passport/country",
        model=OpenAIChat(id="gpt-4o", api_key=openai_api_key),
        description=dedent(
            """\
        You are a world-class Travel guide. Given a city and Passport/country,
        find the websites from the city's country websites and other relevant partner websites. for transit visa requirements.
        This information should be relevant to the passport or country of interest.
        for requested information, analyze and summarize the results.
        Generate and return in 10 to 20 lines of text.
        """
        ),
        instructions=[
            "Given a city and usert passport/country, find the visa requirements for a given passport/country.",
            "find the websites from the city's country websites and other relevant partner websites. for transit visa requirements.",
            "From these websites, summarize the results across all information and provide results in 10-20 lines.",
            "Remember, the quality of the results in important.",
            "Make sure to include links of the source."
        ],
        tools=[SerpApiTools(api_key=serp_api_key)],
        add_datetime_to_instructions=True,
    )

    baggage, transit, terminal = st.tabs([":gray[Baggage]", ":gray[Transit]", ":gray[Terminal]"])
    with baggage:
        airline = st.selectbox(":gray[Which airline do you wish to travel with?]", airlines_list, index=None)
        domestic = st.radio(":gray[Are you traveling domestic or international?]", [":gray[Domestic]", ":gray[International]"])
        if st.button(":gray[Get Baggage information]"):
            with st.spinner(":gray[Getting Baggage information...]"):
                response = airlineguide.run(f"with {airline} travelling {domestic} and getting baggage information for checked bad, carry-on bag with weight and count limit", stream=False)
                st.write(response.content)
    with transit:
        city = st.selectbox(":gray[Which is the layover city?]", cities_list, index=None)
        passport = st.selectbox(":gray[Which country passport are you flying with?]", countries_list, index=None)
        if st.button(":gray[Get transit information]"):
            with st.spinner(":gray[Getting transit information...]"):
                response = transitguide.run(f"given the transit city {city} and the user passport/country {passport}, find the details about requirement of transit visa or any other kind of visa required or not required", stream=False)
                st.write(response.content)

