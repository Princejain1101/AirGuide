import streamlit as st
from textwrap import dedent
from agno.agent import Agent
from agno.tools.serpapi import SerpApiTools
from agno.models.openai import OpenAIChat

# Get OpenAI API key from user
openai_api_key = st.secrets["openai_api_key"]
#st.text_input("Enter OpenAI API Key to access GPT-4o", type="password")

# Get SerpAPI key from the user
serp_api_key = st.secrets["serp_api_key"]
#st.text_input("Enter Serp API Key for Search functionality", type="password")

terminalguide = Agent(
    name="Terminalguide",
    role="Searches for the terminal at an airport",
    model=OpenAIChat(id="gpt-4o", api_key=openai_api_key),
    description=dedent(
        """\
    You are a world-class Airport guide. Given an airline and domestic/international and the City/country airport,
    find the terminal this airline is flying from.
    Generate and return in 10 to 20 words of text.
    """
    ),
    instructions=[
        "Given an airline, city/airport and domestic/international user wants to travel from",
        "find the terminal, this airline is flying from at this airport",
        "From these results, summarize the results across all websites and provide results in 10-20 words.",
        "Remember, the quality of the results in important.",
        "Make sure to include links of the source."
    ],
    tools=[SerpApiTools(api_key=serp_api_key)],
    add_datetime_to_instructions=True,
)

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
