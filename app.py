import streamlit as st
import pandas as pd
import plotly.express as px
from groq import Groq

st.set_page_config(
    page_title="Language Planning: Sindhi & Regional Dialects",
    page_icon="🧵",
    layout="wide",
)

# ---------- THEME: inspired by Ajrak block-print textiles ----------
# Indigo ink, madder red, and mustard ochre — the traditional Ajrak palette.
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Karla:wght@400;500;600&display=swap');

    html, body, [class*="css"], .stMarkdown, p, li, span, label {
        font-family: 'Karla', sans-serif;
    }

    h1, h2, h3, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        font-family: 'Fraunces', serif !important;
        color: #F2ECDA !important;
        letter-spacing: 0.005em;
    }

    .stApp {
        background-color: #132A45;
        color: #F2ECDA;
    }

    [data-testid="stSidebar"] {
        background-color: #1C3B5C;
        border-right: 1px solid #2E4E70;
    }

    [data-testid="stSidebar"] * {
        color: #F2ECDA !important;
    }

    /* Sidebar radio list — styled as a clean bullet-point nav.
       Uses only standard HTML elements (label, div) inside the sidebar,
       not fragile internal Streamlit component names, so it stays
       reliable across Streamlit versions. */
    [data-testid="stSidebar"] [role="radiogroup"] {
        gap: 2px;
    }

    [data-testid="stSidebar"] [role="radiogroup"] label {
        border-radius: 6px;
        padding: 0.5rem 0.6rem;
        transition: background-color 0.15s ease;
        cursor: pointer;
    }

    [data-testid="stSidebar"] [role="radiogroup"] label:hover {
        background-color: rgba(211, 160, 54, 0.22);
    }

    /* The selected radio's circle already picks up primaryColor
       (madder red) automatically from .streamlit/config.toml. This
       adds a matching highlight to the whole row for the selected item. */
    [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {
        background-color: rgba(166, 58, 50, 0.55);
    }

    [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) p {
        font-weight: 700 !important;
        color: #F2ECDA !important;
    }

    .stMarkdown, .stCaption, p, li, span {
        color: #E7DFC8 !important;
    }

    .stButton>button, .stDownloadButton>button {
        background-color: #A63A32;
        color: #F2ECDA;
        border: none;
        border-radius: 3px;
        font-family: 'Karla', sans-serif;
        font-weight: 600;
    }

    .stButton>button:hover, .stDownloadButton>button:hover {
        background-color: #D3A036;
        color: #132A45;
    }

    [data-testid="stMetricValue"] {
        color: #D3A036 !important;
        font-family: 'Fraunces', serif !important;
    }

    [data-testid="stExpander"] {
        background-color: #1C3B5C;
        border-left: 3px solid #A63A32;
        border-radius: 2px;
    }

    .stAlert {
        border-radius: 2px;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        margin: 0 auto;
    }

    .stButton>button:focus-visible, .stDownloadButton>button:focus-visible,
    [data-testid="stSidebar"] [role="radio"]:focus-visible {
        outline: 2px solid #D3A036 !important;
        outline-offset: 2px;
    }

    .hero-band {
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='72' height='72'%3E%3Cpath d='M36 4 L68 36 L36 68 L4 36 Z' fill='none' stroke='%23D3A036' stroke-width='1.5' opacity='0.4'/%3E%3Ccircle cx='36' cy='36' r='4' fill='%23A63A32' opacity='0.5'/%3E%3C/svg%3E");
        background-repeat: repeat;
        padding: 1.8rem 1.6rem 1.4rem 1.6rem;
        border-radius: 6px;
        border: 1px solid #2E4E70;
        margin-bottom: 0.4rem;
    }

    @keyframes heroFade {
        from { opacity: 0; transform: translateY(6px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .hero-title, .hero-subtitle {
        animation: heroFade 0.7s ease-out;
    }

    .ajrak-divider {
        height: 6px;
        margin: 1.2rem 0 1.6rem 0;
        background: repeating-linear-gradient(
            45deg,
            #A63A32 0px, #A63A32 10px,
            #D3A036 10px, #D3A036 20px,
            #F2ECDA 20px, #F2ECDA 30px
        );
        border-radius: 1px;
        opacity: 0.9;
    }

    .hero-title {
        font-family: 'Fraunces', serif;
        font-weight: 700;
        font-size: 2.6rem;
        color: #F2ECDA;
        margin-bottom: 0.1rem;
    }

    .hero-subtitle {
        font-family: 'Karla', sans-serif;
        font-size: 1.05rem;
        color: #D3A036;
        font-weight: 500;
        margin-top: 0;
    }

    /* ---------- RESPONSIVE: tablet & mobile ---------- */
    @media (max-width: 768px) {
        .block-container {
            padding-top: 1.2rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .hero-band {
            padding: 1.1rem 1rem 0.9rem 1rem;
            margin-bottom: 0.2rem;
        }

        .hero-title {
            font-size: 1.55rem;
            line-height: 1.25;
        }

        .hero-subtitle {
            font-size: 0.85rem;
            line-height: 1.35;
        }

        .ajrak-divider {
            height: 4px;
            margin: 0.8rem 0 1.1rem 0;
        }

        [data-testid="stSidebar"] [role="radiogroup"] label {
            padding: 0.65rem 0.6rem;
        }

        /* Full-width, thumb-friendly buttons on touch screens */
        .stButton>button, .stDownloadButton>button {
            width: 100%;
        }

        [data-testid="stMetricValue"] {
            font-size: 1.3rem !important;
        }
    }

    @media (max-width: 480px) {
        .hero-title {
            font-size: 1.3rem;
        }

        .hero-band {
            background-size: 48px 48px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def ajrak_divider():
    """A woven-stripe rule evoking Ajrak block-print borders, used in
    place of a plain horizontal line between sections."""
    st.markdown('<div class="ajrak-divider"></div>', unsafe_allow_html=True)


def page_header():
    """Shared hero header shown at the top of every page."""
    st.markdown(
        '<div class="hero-band">'
        '<p class="hero-title">Language Planning in Sociolinguistics</p>'
        '<p class="hero-subtitle">Policy Development for Regional Dialects — A Focus on Sindhi</p>'
        '</div>',
        unsafe_allow_html=True,
    )
    ajrak_divider()


def page_footer():
    """Shared footer shown at the bottom of every page."""
    ajrak_divider()
    st.caption("Built with Streamlit · Sociolinguistics: Language Planning & Policy")


# =========================================================
# PAGE FUNCTIONS
# =========================================================

def render_overview():
    page_header()
    st.header("Overview")
    st.write(
        """
        Language planning refers to the deliberate efforts by governments,
        institutions, or communities to influence the structure, use, and
        status of a language. This analysis examines how such planning
        applies to regional dialects — languages that hold strong local and
        cultural significance but face pressure from globally and
        nationally dominant languages.

        The Sindhi language, spoken primarily in the Sindh province of
        Pakistan and parts of India, serves as a central case study. It
        illustrates the tension between preserving linguistic and cultural
        identity and adapting to forces of globalization, national language
        standardization, and shifting educational or economic incentives.
        """
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Focus Language", "Sindhi")
    col2.metric("Key Tension", "Preservation vs. Standardization")
    col3.metric("Driving Force", "Globalization")

    st.markdown("### Domain Usage: Sindhi vs. Urdu/English (illustrative)")
    st.caption(
        "Estimated relative usage share by domain — for illustration of "
        "the language-shift pattern, not measured survey data."
    )
    domain_data = pd.DataFrame(
        {
            "Domain": ["Home", "Primary School", "Secondary/Higher Ed",
                       "Government/Courts", "Media", "Digital/Social Media"],
            "Sindhi": [75, 55, 20, 30, 25, 10],
            "Urdu/English": [25, 45, 80, 70, 75, 90],
        }
    )
    fig = px.bar(
        domain_data,
        x="Domain",
        y=["Sindhi", "Urdu/English"],
        barmode="group",
        labels={"value": "Relative usage (%)", "variable": "Language"},
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Where Sindhi is Spoken")
    st.caption("Click a marker to learn more about that city.")
    map_data = pd.DataFrame(
        {
            "lat": [25.3960, 24.8607, 27.7244],
            "lon": [68.3578, 67.0011, 68.8358],
            "city": ["Hyderabad, Sindh", "Karachi, Sindh", "Sukkur, Sindh"],
            "blurb": [
                "A historic center of Sindhi language and literature — "
                "the Sindhi language movement of the 1970s, which pushed "
                "for Sindhi's official provincial status, was centered here.",
                "Pakistan's largest and most linguistically diverse city. "
                "Sindhi remains a major mother tongue, especially in older "
                "and interior neighborhoods, alongside Urdu and other "
                "migrant-community languages.",
                "A key trade and administrative hub in northern Sindh, "
                "historically important for Sindhi-language print media "
                "and publishing.",
            ],
        }
    )
    map_fig = px.scatter_mapbox(
        map_data,
        lat="lat",
        lon="lon",
        hover_name="city",
        custom_data=["city", "blurb"],
        zoom=5.2,
        height=420,
    )
    map_fig.update_traces(marker=dict(size=16, color="#A63A32"))
    map_fig.update_layout(
        mapbox_style="open-street-map",
        margin=dict(l=0, r=0, t=0, b=0),
    )
    map_event = st.plotly_chart(
        map_fig,
        use_container_width=True,
        key="sindhi_map",
        on_select="rerun",
    )

    if map_event and map_event.selection and map_event.selection.points:
        point = map_event.selection.points[0]
        clicked_city, clicked_blurb = point["customdata"]
        st.info(f"**{clicked_city}** — {clicked_blurb}")
    else:
        st.caption("No marker selected yet.")
    page_footer()


def render_policy():
    page_header()
    st.header("Language Policy Development")
    st.write(
        """
        Language policy development for regional dialects typically unfolds
        across three interacting levels:
        """
    )
    st.markdown(
        """
        1. **Status planning** — decisions about the official or
           institutional recognition of a language (e.g., is Sindhi a
           medium of instruction, an official provincial language, or
           only a "heritage" language?).
        2. **Corpus planning** — decisions about the language's internal
           form: orthography, standard grammar, vocabulary modernization,
           and terminology development for new domains (science,
           technology, law).
        3. **Acquisition planning** — decisions about how the language is
           taught and transmitted, including its place in school
           curricula, teacher training, and literacy programs.

        Effective policy usually requires coordinated action across all
        three levels; focusing on only one (for example, granting official
        status without investing in acquisition planning) tends to produce
        symbolic rather than functional recognition.
        """
    )
    page_footer()


def render_globalization():
    page_header()
    st.header("Globalization & Standardization Pressures")
    st.write("Regional dialects face two overlapping pressures:")
    tab1, tab2 = st.tabs(["Globalization", "National Standardization"])

    with tab1:
        st.write(
            """
            - Dominance of global languages (especially English) in higher
              education, digital media, and international commerce reduces
              the perceived economic value of regional languages.
            - Migration and urbanization mix speech communities, often
              accelerating shift toward more "prestigious" or widely
              spoken varieties.
            - Digital and social media are overwhelmingly built around a
              small number of world languages, limiting the digital
              presence of regional dialects.
            """
        )

    with tab2:
        st.write(
            """
            - National governments often promote a single standardized
              language (e.g., Urdu in Pakistan) for administrative
              efficiency and national unity.
            - Standardization can marginalize regional dialects by
              framing them as "non-standard," reducing their use in
              formal domains like courts, government offices, and
              national exams.
            - Even when a regional language has official status, resource
              allocation (textbooks, media time, exam options) often still
              favors the national standard.
            """
        )
    page_footer()


def render_challenges():
    page_header()
    st.header("Challenges to Preservation")
    challenges = {
        "Educational Domain": "Limited use of Sindhi as a medium of instruction beyond primary levels; weak transition support into higher education.",
        "Economic Incentives": "Job markets favor Urdu and English proficiency, reducing motivation for younger speakers to invest in Sindhi literacy.",
        "Media Representation": "Underrepresentation in national broadcast media and digital platforms compared to Urdu and English content.",
        "Intergenerational Transmission": "Urban, mixed-language households increasingly shift to Urdu or English at home, weakening transmission to children.",
        "Script & Standardization Issues": "Variation in orthographic conventions and limited standardized terminology for modern/technical domains.",
        "Political Will & Funding": "Inconsistent implementation of language policies due to shifting political priorities and limited budget allocation.",
    }
    for title, desc in challenges.items():
        with st.expander(title):
            st.write(desc)
    page_footer()


def render_strategies():
    page_header()
    st.header("Strategies for Preservation")
    st.write("Sociolinguistic literature suggests several strategies:")

    strategies = [
        ("Mother-tongue-based multilingual education (MTB-MLE)",
         "Introducing Sindhi as the medium of instruction in early schooling, transitioning gradually into Urdu/English, rather than an abrupt switch."),
        ("Corpus modernization",
         "Developing standardized terminology for science, technology, and law so Sindhi remains usable in modern professional domains."),
        ("Media and digital presence",
         "Expanding Sindhi-language content on television, radio, and digital platforms, including localization of software and apps."),
        ("Community-based literacy programs",
         "Supporting adult literacy and cultural programs that reinforce the prestige and everyday utility of the language."),
        ("Legal and institutional recognition",
         "Strengthening enforcement of existing provincial language laws, ensuring Sindhi is genuinely usable in courts and government offices."),
        ("Documentation and corpus building",
         "Creating digital corpora, dictionaries, and archives to support both education and language technology (e.g., spellcheckers, translation tools)."),
    ]

    for title, desc in strategies:
        st.markdown(f"**• {title}**")
        st.write(desc)
        st.markdown("")
    page_footer()


def render_case_study():
    page_header()
    st.header("Case Study: Sindhi Language Planning")
    st.write(
        """
        Sindhi offers a useful case because it has *de jure* recognition
        (official provincial language status in Sindh, Pakistan, and a
        scheduled language in India) but faces *de facto* pressures common
        to many regional dialects.
        """
    )

    st.subheader("Strengths")
    st.write(
        """
        - Long literary tradition and a well-established standard script.
        - Constitutional and provincial recognition supporting its use in
          education and local government.
        - Active civil society and academic interest in Sindhi linguistics
          and literature.
        """
    )

    st.subheader("Ongoing Pressures")
    st.write(
        """
        - Urdu's role as the national lingua franca and English's role in
          higher education and the job market continue to limit Sindhi's
          functional domains.
        - Urban youth increasingly code-switch or shift toward Urdu/English
          in informal and digital communication.
        - Divergence between the Pakistani (Sindh) and Indian Sindhi
          communities has led to some variation in script use (Perso-Arabic
          vs. Devanagari) and standardization practices.
        """
    )

    st.info(
        "The Sindhi case illustrates a broader pattern in language "
        "planning: formal recognition alone does not guarantee vitality — "
        "sustained investment across status, corpus, and acquisition "
        "planning is required."
    )
    page_footer()


def render_conclusion():
    page_header()
    st.header("Conclusion & Recommendations")
    st.write(
        """
        Preserving regional dialects like Sindhi in an era of globalization
        and national standardization requires policy that is coordinated,
        adequately funded, and responsive to the everyday incentives that
        shape language choice — not just symbolic recognition.
        """
    )
    st.markdown(
        """
        **Key recommendations:**
        - Align status, corpus, and acquisition planning rather than
          treating them as separate initiatives.
        - Invest in digital infrastructure (fonts, keyboards, corpora,
          translation tools) to keep the language relevant in modern
          domains.
        - Strengthen mother-tongue-based education models with a clear,
          well-supported transition into national/international languages.
        - Monitor implementation, not just legislation — ensure that legal
          recognition translates into real classroom and institutional use.
        """
    )
    page_footer()


def render_quiz():
    page_header()
    st.header("Quick Quiz: Test Your Understanding")
    st.write("Check what you've learned about language planning and Sindhi.")

    score = 0
    total = 3

    q1 = st.radio(
        "1. What are the three levels of language planning?",
        ["Status, corpus, and acquisition planning",
         "Grammar, vocabulary, and pronunciation",
         "Federal, provincial, and local planning"],
        index=None, key="q1",
    )
    if q1:
        if q1 == "Status, corpus, and acquisition planning":
            st.success("Correct! These three levels interact to shape a language's vitality.")
            score += 1
        else:
            st.error("Not quite — it's status, corpus, and acquisition planning.")

    q2 = st.radio(
        "2. In Pakistan, which language most often serves as the national lingua franca, competing with Sindhi for institutional use?",
        ["Urdu", "Punjabi", "Pashto"],
        index=None, key="q2",
    )
    if q2:
        if q2 == "Urdu":
            st.success("Correct! Urdu's role as national language creates pressure on regional languages like Sindhi.")
            score += 1
        else:
            st.error("Not quite — Urdu is the national lingua franca in this context.")

    q3 = st.radio(
        "3. What does 'mother-tongue-based multilingual education' (MTB-MLE) propose?",
        ["Teaching only in the national language from day one",
         "Starting instruction in the child's first language, then transitioning gradually",
         "Banning regional languages from classrooms"],
        index=None, key="q3",
    )
    if q3:
        if q3 == "Starting instruction in the child's first language, then transitioning gradually":
            st.success("Correct! MTB-MLE eases the transition rather than forcing an abrupt language switch.")
            score += 1
        else:
            st.error("Not quite — MTB-MLE starts in the mother tongue, then transitions gradually.")

    if q1 and q2 and q3:
        st.markdown(f"### Your score: {score}/{total}")
        if score == total:
            st.balloons()
    page_footer()


def render_references():
    page_header()
    st.header("References & Further Reading")
    st.write(
        """
        This app presents an illustrative overview. For rigorous academic
        grounding, consult these foundational and Pakistan/Sindhi-specific
        sources:
        """
    )
    st.markdown(
        """
        **Foundational language-planning theory**
        - Haugen, E. (1966). *Language Conflict and Language Planning: The
          Case of Modern Norwegian*. Harvard University Press. (Introduced
          the classic four-step language planning model.)
        - Fishman, J. A. (1991). *Reversing Language Shift: Theoretical and
          Empirical Foundations of Assistance to Threatened Languages*.
          Multilingual Matters.

        **Sindhi & Pakistan-specific sociolinguistics**
        - Rahman, T. (1996). *Language and Politics in Pakistan*. Oxford
          University Press. — The standard history of language politics in
          Pakistan, including the Sindhi language movement.
        - Rahman, T. (2006). "Language Policy, Multilingualism and Language
          Vitality in Pakistan." In *Trends in Linguistics Studies and
          Monographs*, Vol. 175.
        - Pathan, H., Shah, S., Lohar, S., Khoso, A., & Memon, S. (2018).
          "Language Policy and Its Consequences on Sindhi Language
          Teaching in Sindh, Pakistan." *International Journal of English
          Linguistics*, 8(5).

        **International frameworks**
        - UNESCO. *Atlas of the World's Languages in Danger* — a reference
          tool for assessing language vitality and endangerment globally.

        ---
        *Note: This app's content is an educational summary for coursework
        purposes. Always cite the original sources above in academic work,
        not this app.*
        """
    )
    page_footer()


def render_ai_assistant():
    page_header()
    st.header("Ask AI Assistant")
    st.write(
        "Ask a question about language planning, Sindhi, or dialect "
        "preservation and get an instant AI-generated answer."
    )

    api_key = st.secrets.get("GROQ_API_KEY", None)

    if not api_key:
        st.warning(
            "No Groq API key found. Add GROQ_API_KEY to your Streamlit "
            "secrets to enable this feature (see setup instructions)."
        )
    else:
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

        user_question = st.chat_input("Ask about language planning or Sindhi...")

        if user_question:
            st.session_state.chat_history.append(
                {"role": "user", "content": user_question}
            )
            with st.chat_message("user"):
                st.write(user_question)

            try:
                client = Groq(api_key=api_key)
                with st.chat_message("assistant"):
                    with st.spinner("Thinking..."):
                        response = client.chat.completions.create(
                            model="openai/gpt-oss-120b",
                            messages=[
                                {
                                    "role": "system",
                                    "content": (
                                        "You are a helpful sociolinguistics "
                                        "assistant specializing in language "
                                        "planning, policy, and regional "
                                        "dialect preservation, with expertise "
                                        "on Sindhi and South Asian languages. "
                                        "Give clear, concise, accurate answers."
                                    ),
                                },
                                *st.session_state.chat_history,
                            ],
                        )
                        answer = response.choices[0].message.content
                        st.write(answer)
                st.session_state.chat_history.append(
                    {"role": "assistant", "content": answer}
                )
            except Exception as e:
                st.error(f"Error contacting Groq API: {e}")

        if st.button("Clear conversation"):
            st.session_state.chat_history = []
            st.rerun()
    page_footer()


def render_comparison():
    page_header()
    st.header("Language Comparison Tool")
    st.write(
        "Compare Sindhi against Pakistan's other major regional languages "
        "using 2023 census mother-tongue figures and provincial policy status."
    )

    LANGUAGE_DATA = {
        "Punjabi": {"pct": 37.0, "region": "Punjab", "official_status": "Not an official provincial language; limited use in schooling despite being the largest mother tongue."},
        "Pashto": {"pct": 18.0, "region": "Khyber Pakhtunkhwa", "official_status": "Provincial language of KP; used in some primary education."},
        "Sindhi": {"pct": 14.0, "region": "Sindh", "official_status": "Official provincial language of Sindh; medium of instruction through primary school."},
        "Saraiki": {"pct": 12.0, "region": "Southern Punjab", "official_status": "Recognized regionally but not an official provincial language."},
        "Urdu": {"pct": 9.0, "region": "National (lingua franca)", "official_status": "National and co-official language; dominant in administration and media nationwide."},
        "Balochi": {"pct": 3.0, "region": "Balochistan", "official_status": "One of Balochistan's provincial languages, alongside Pashto and Brahui."},
    }

    selected = st.multiselect(
        "Choose languages to compare",
        list(LANGUAGE_DATA.keys()),
        default=["Sindhi", "Punjabi", "Pashto", "Urdu"],
    )

    if not selected:
        st.info("Select at least one language above to see the comparison.")
    else:
        compare_df = pd.DataFrame(
            {
                "Language": selected,
                "Share of population (%)": [LANGUAGE_DATA[lang]["pct"] for lang in selected],
            }
        )
        fig = px.bar(
            compare_df,
            x="Language",
            y="Share of population (%)",
            color="Language",
            text="Share of population (%)",
        )
        fig.update_traces(textposition="outside")
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
        st.caption("Source: 2023 Pakistan Bureau of Statistics census, mother-tongue share of national population.")

        st.markdown("### Policy status at a glance")
        for lang in selected:
            info = LANGUAGE_DATA[lang]
            with st.expander(f"{lang} — {info['pct']}% · {info['region']}"):
                st.write(info["official_status"])

    st.markdown("---")
    st.caption(
        "Note: figures reflect mother-tongue share of Pakistan's national "
        "population, not regional concentration — e.g. Sindhi speakers are "
        "far denser within Sindh itself than the national 14% suggests."
    )
    page_footer()


def render_glossary():
    page_header()
    st.header("Glossary of Key Terms")
    st.write(
        "Core sociolinguistics and language-planning terminology used "
        "throughout this app."
    )

    search = st.text_input("🔍 Search glossary", "")

    glossary = {
        "Status planning": "Decisions about the official, legal, or institutional recognition given to a language — e.g., whether it is an official language, a medium of instruction, or used in courts and government.",
        "Corpus planning": "Deliberate intervention in a language's internal form: its orthography (writing system), grammar, spelling standards, and vocabulary — including creating new terms for modern/technical concepts.",
        "Acquisition planning": "Planning focused on how a language is taught and transmitted, including its place in school curricula, teacher training programs, and literacy campaigns.",
        "Language shift": "The process by which a speech community gradually stops using its original (often minority) language in favor of another, usually more dominant, language — often occurring across generations.",
        "Language maintenance": "The continued use of a language by a community despite pressure from a dominant language, often supported by strong intergenerational transmission and community institutions.",
        "Reversing Language Shift (RLS)": "A concept developed by sociolinguist Joshua Fishman describing deliberate efforts to restore intergenerational transmission of an endangered or threatened language.",
        "Diglossia": "A situation in a speech community where two language varieties are used, each in distinct social contexts — typically a 'high' variety for formal/official domains and a 'low' variety for everyday/informal use.",
        "Language vitality": "A measure of how actively a language is used and transmitted, considering factors like number of speakers, intergenerational transmission, domains of use, and institutional support.",
        "EGIDS (Expanded Graded Intergenerational Disruption Scale)": "A framework used by linguists (notably in Ethnologue) to classify a language's level of vitality or endangerment, from 'international' use down to 'extinct'.",
        "Mother-tongue-based multilingual education (MTB-MLE)": "An educational approach where children begin schooling in their first/home language before gradually transitioning into additional languages (often the national or official language).",
        "Linguistic imperialism": "A concept describing how dominant languages (historically often colonial languages) spread and gain prestige partly through political and economic power, often at the expense of local/regional languages.",
        "Lingua franca": "A language systematically used to enable communication between speakers of different native languages, often for trade, administration, or education (e.g., Urdu functions this way in Pakistan).",
        "Language nationalism": "The use of a specific language as a core symbol of national or ethnic identity, often central to political movements (e.g., the Sindhi language movement in Pakistan).",
        "Language academy/authority": "An official institution tasked with regulating, standardizing, and promoting a language — e.g., Pakistan's Sindhi Language Authority or National Language Authority (for Urdu).",
    }

    filtered = {
        term: definition
        for term, definition in glossary.items()
        if search.lower() in term.lower() or search.lower() in definition.lower()
    }

    if not filtered:
        st.info("No matching terms found. Try a different search word.")
    else:
        for term, definition in sorted(filtered.items()):
            with st.expander(term):
                st.write(definition)
    page_footer()


# =========================================================
# SIDEBAR: shared elements + native grouped navigation
# =========================================================

SUMMARY_TEXT = """LANGUAGE PLANNING: SINDHI & REGIONAL DIALECTS — SUMMARY

Language planning shapes a language's status (official recognition),
corpus (standard form/vocabulary), and acquisition (how it is taught).
Regional dialects like Sindhi hold official recognition in Sindh,
Pakistan, but face real pressure from globalization (English in
higher education, digital media) and national standardization (Urdu
as lingua franca).

Key challenges: limited use as medium of instruction beyond primary
school, weak job-market incentives, underrepresentation in national
media, and inconsistent intergenerational transmission in urban
households.

Key strategies: mother-tongue-based multilingual education, corpus
modernization for technical domains, expanded media/digital presence,
community literacy programs, and stronger enforcement of existing
language laws.

Sindhi shows that legal recognition alone does not guarantee
vitality — sustained, coordinated investment across all planning
levels is required.
"""

st.sidebar.markdown('<p class="hero-title" style="font-size:1.4rem;">🧵 Sindhi Language Planning</p>', unsafe_allow_html=True)
st.sidebar.caption("A sociolinguistics analysis")
st.sidebar.markdown("---")

PAGES = {
    "📖 Overview": render_overview,
    "🏛️ Policy Development": render_policy,
    "🌐 Globalization Pressures": render_globalization,
    "⚠️ Challenges": render_challenges,
    "🧭 Strategies": render_strategies,
    "📍 Case Study: Sindhi": render_case_study,
    "✅ Conclusion": render_conclusion,
    "🗺️ Language Comparison": render_comparison,
    "🧠 Quick Quiz": render_quiz,
    "📘 Glossary": render_glossary,
    "📚 References": render_references,
    "🤖 Ask AI Assistant": render_ai_assistant,
}

choice = st.sidebar.radio("Go to section", list(PAGES.keys()), label_visibility="collapsed")

st.sidebar.markdown("---")
st.sidebar.download_button(
    label="📥 Download Summary (.txt)",
    data=SUMMARY_TEXT,
    file_name="sindhi_language_planning_summary.txt",
    mime="text/plain",
)
st.sidebar.markdown("---")
st.sidebar.info(
    "This app presents a language-planning analysis of regional dialect "
    "policy, with a focus on Sindhi, in the context of globalization and "
    "standardization pressures."
)

PAGES[choice]()
