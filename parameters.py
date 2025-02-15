import base64
import streamlit as st

airlines_list = ["Aegean Airlines",
"Aer Lingus",
"Aeroflot",
"Aerolineas Argentinas",
"Aeromexico",
"Air Arabia",
"Air Astana",
"Air Austral",
"Air Baltic",
"Air Belgium",
"Air Canada",
"Air Caraibes",
"Air China",
"Air Corsica",
"Air Dolomiti",
"Air Europa",
"Air France",
"Air India",
"Air India Express",
"Air Macau",
"Air Malta",
"Air Mauritius",
"Air Namibia",
"Air New Zealand",
"Air North",
"Air Seoul",
"Air Serbia",
"Air Tahiti Nui",
"Air Transat",
"Air Vanuatu",
"AirAsia",
"AirAsia X",
"Aircalin",
"Alaska Airlines",
"Alitalia",
"Allegiant",
"American Airlines",
"ANA",
"Asiana",
"Austrian",
"Azerbaijan Hava Yollary",
"Azores Airlines",
"Azul",
"Bamboo Airways",
"Bangkok Airways",
"British Airways",
"Brussels Airlines",
"Caribbean Airlines",
"Cathay Dragon",
"Cathay Pacific",
"Cayman Airways",
"CEBU Pacific Air",
"China Airlines",
"China Eastern",
"China Southern",
"Condor",
"Copa Airlines",
"Croatia Airlines",
"Czech Airlines",
"Delta",
"easyJet",
"Edelweiss Air",
"Egyptair",
"EL AL",
"Emirates",
"Ethiopian Airlines",
"Etihad",
"Eurowings",
"EVA Air",
"Fiji Airways",
"Finnair",
"flydubai",
"FlyOne",
"French bee",
"Frontier",
"Garuda Indonesia",
"Gol",
"Gulf Air",
"Hainan Airlines",
"Hawaiian Airlines",
"Helvetic Airways",
"HK Express",
"Hong Kong Airlines",
"Iberia",
"Icelandair",
"IndiGo Airlines",
"InterJet",
"Japan Airlines",
"Jeju Air",
"Jet2",
"JetBlue",
"Jetstar",
"Jin Air",
"Kenya Airways",
"KLM",
"Korean Air",
"Kulula",
"La Compagnie",
"LATAM",
"Lion Airlines",
"LOT Polish Airlines",
"Lufthansa",
"Luxair",
"Malaysia Airlines",
"Mango",
"Middle East Airlines",
"Nok Air",
"Nordwind Airlines",
"Norwegian Air International",
"Norwegian Air Shuttle",
"Norwegian Air Sweden",
"Norwegian Air UK",
"Oman Air",
"Pakistan International Airlines",
"Peach",
"Pegasus Airlines",
"Philippine Airlines",
"Porter",
"Qantas",
"Qatar Airways",
"Regional Express",
"Rossiya - Russian Airlines",
"Royal Air Maroc",
"Royal Brunei",
"Royal Jordanian",
"RwandAir",
"Ryanair",
"S7 Airlines",
"SAS",
"Saudia",
"Scoot Airlines",
"Shanghai Airlines",
"Silkair",
"Silver",
"Singapore Airlines",
"Skylanes",
"South African Airways",
"Southwest",
"SpiceJet",
"Spirit",
"Spring Airlines",
"Spring Japan",
"SriLankan Airlines",
"Sun Country",
"Sunclass Airlines",
"Sunwing",
"SWISS",
"Swoop",
"TAAG",
"TACA",
"TAP Portugal",
"THAI",
"tigerair Australia",
"Transavia Airlines",
"TUI UK",
"TUIfly",
"Tunis Air",
"Turkish Airlines",
"Ukraine International",
"United",
"Ural Airlines",
"UTair Aviation",
"Uzbekistan Airways",
"Vietnam Airlines",
"Virgin Atlantic",
"Virgin Australia",
"Vistara",
"Viva Aerobus",
"Volaris",
"Volotea",
"Vueling Airlines",
"WestJet",
"Wizzair",
"Xiamen Airlines",
]

@st.cache_data()
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str

    st.markdown(page_bg_img, unsafe_allow_html=True)
    return


def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''

    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url("https://static.vecteezy.com/system/resources/thumbnails/043/191/561/small_2x/airplane-side-view-flying-above-the-clouds-with-blue-sky-background-illustration-vector.jpg");
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )