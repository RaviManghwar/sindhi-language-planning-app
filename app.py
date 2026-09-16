import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Language Planning: Sindhi & Regional Dialects",
    page_icon="🗣️",
    layout="wide",
)

# ---------- SIDEBAR NAVIGATION ----------
st.sidebar.title("🗣️ Navigation")
section = st.sidebar.radio(
    "Go to section",
    [
        "Overview",
        "Language Policy Development",
        "Globalization & Standardization Pressures",
        "Challenges to Preservation",
        "Strategies for Preservation",
        "Case Study: Sindhi",
        "Conclusion & Recommendations",
        "Quick Quiz",
        "References & Further Reading",
    ],
)

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

# ---------- HEADER ----------
st.title("Language Planning in Sociolinguistics")
st.subheader("Policy Development for Regional Dialects — A Focus on Sindhi")
st.markdown("---")

# ---------- OVERVIEW ----------
if section == "Overview":
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
    map_data = pd.DataFrame(
        {
            "lat": [25.3960, 24.8607, 27.7244],
            "lon": [68.3578, 67.0011, 68.8358],
            "city": ["Hyderabad, Sindh", "Karachi, Sindh", "Sukkur, Sindh"],
        }
    )
    st.map(map_data, latitude="lat", longitude="lon", size=100)

# ---------- POLICY DEVELOPMENT ----------
elif section == "Language Policy Development":
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

# ---------- GLOBALIZATION ----------
elif section == "Globalization & Standardization Pressures":
    st.header("Globalization & Standardization Pressures")
    st.write(
        """
        Regional dialects face two overlapping pressures:
        """
    )
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

# ---------- CHALLENGES ----------
elif section == "Challenges to Preservation":
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

# ---------- STRATEGIES ----------
elif section == "Strategies for Preservation":
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

# ---------- CASE STUDY ----------
elif section == "Case Study: Sindhi":
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

# ---------- CONCLUSION ----------
elif section == "Conclusion & Recommendations":
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

# ---------- QUICK QUIZ ----------
elif section == "Quick Quiz":
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

# ---------- REFERENCES ----------
elif section == "References & Further Reading":
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

st.markdown("---")
st.caption("Built with Streamlit · Sociolinguistics: Language Planning & Policy")
