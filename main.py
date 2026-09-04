from fasthtml.common import *


app, rt = fast_app(
    pico=False,
    static_path=".",
    hdrs=(
        Meta(charset="utf-8"),
        Meta(
            name="viewport",
            content=(
                "width=device-width, initial-scale=1, "
                "viewport-fit=cover"
            ),
        ),
        Link(
            rel="stylesheet",
            href=(
                "https://fonts.googleapis.com/css2?"
                "family=Archivo:wght@400;500;600;700&"
                "family=Bricolage+Grotesque:"
                "opsz,wght@12..96,400;12..96,500;"
                "12..96,600;12..96,700&display=swap"
            ),
        ),
        Link(
            rel="stylesheet",
            href="/styles.css",
        ),
        Script(
            src=(
                "https://cdn.jsdelivr.net/npm/"
                "gsap@3/dist/gsap.min.js"
            ),
            defer=True,
        ),
        Script(
            src=(
                "https://cdn.jsdelivr.net/npm/"
                "gsap@3/dist/ScrollTrigger.min.js"
            ),
            defer=True,
        ),
        Script(
            src="/script.js",
            defer=True,
        ),
    ),
)


SECTIONS = [
    (
        "background",
        "01",
        "Introduction and Background",
        [
            (
                "What is your earliest music memory?",
                "Listening to music with my friends and family.",
            ),
            (
                "How has music shaped your life?",
                "Music has been something that I have been learning, "
                "listening to, and performing.",
            ),
            (
                "What musical training or experience do you have?",
                "I have been learning the violin at school and I have "
                "been taking piano lessons for almost 4 years.",
            ),
        ],
    ),
    (
        "preferences",
        "02",
        "Musical Preferences",
        [
            (
                "Who are your favorite artists or bands, and why?",
                "I don't have a favorite.",
            ),
            (
                "What music genres do you enjoy, and why?",
                "I don't have a favorite.",
            ),
            (
                "Which songs or albums have special meaning to you?",
                "I don't have a favorite.",
            ),
        ],
    ),
    (
        "skills",
        "03",
        "Strengths and Skills",
        [
            (
                "What are your musical strengths?",
                "Music Theory",
            ),
            (
                "Have you created or contributed to a piece of music?",
                "No, but maybe when I am older and have a better "
                "understanding of music and music theory. Maybe then "
                "I could learn how to properly compose a piece.",
            ),
        ],
    ),
    (
        "reflection",
        "04",
        "Personal Reflection",
        [
            (
                "What role will music play in your future?",
                "I think I will play music until after high school, "
                "then it will probably be something that I just play "
                "for fun and listen to.",
            ),
            (
                "What are your musical goals or dreams?",
                "To get NCHO this year.",
            ),
            (
                "How do you share your love of music with others?",
                "Playing music with my friends. Or fellow orchestra "
                "members.",
            ),
        ],
    ),
    (
        "future",
        "05",
        "Future Aspirations",
        [
            (
                "What would you like to improve in orchestra class?",
                "To play actual vibrato and get better at sight reading.",
            ),
            (
                "What projects would you like to work on this year?",
                "Not really",
            ),
        ],
    ),
]


def navigation():
    return Header(
        A(
            "ML/M",
            href="#top",
            cls="logo magnetic",
        ),
        Nav(
            *[
                A(
                    number,
                    href=f"#{slug}",
                    cls="nav-dot magnetic",
                    aria_label=title,
                )
                for slug, number, title, questions in SECTIONS
            ]
        ),
        A(
            "Index",
            href="#background",
            cls="index-link magnetic",
        ),
        cls="site-nav",
    )


def question_card(question, answer, number):
    return Article(
        Span(
            f"Q/{number:02}",
            cls="question-id",
        ),
        H3(
            question,
            cls="question-text",
        ),
        Div(
            P(answer),
            Span("↗"),
            cls="answer-pill cursor-target",
        ),
        cls="qa-card",
    )


def chapter(slug, number, title, questions):
    return Section(
        Header(
            Span(
                number,
                cls="section-number",
            ),
            H2(
                *[
                    Span(word + " ")
                    for word in title.split()
                ],
                cls="section-title",
            ),
            cls="section-header",
        ),
        Div(
            *[
                question_card(question, answer, index)
                for index, (question, answer)
                in enumerate(questions, start=1)
            ],
            cls="cards-track",
        ),
        id=slug,
        cls=f"story-section theme-{number}",
    )


@rt("/")
def get():
    return (
        Title("My Life in Music"),

        Div(
            Span("OPEN"),
            cls="loader",
        ),

        Div(
            cls="cursor-small",
            aria_hidden="true",
        ),

        Div(
            Span("VIEW"),
            cls="cursor-large",
            aria_hidden="true",
        ),

        Div(
            cls="progress",
            aria_hidden="true",
        ),

        navigation(),

        Main(
            Section(
                Div(
                    Span("MY LIFE"),
                    Span("IN MUSIC"),
                    cls="hero-title",
                ),

                Div(
                    Span("VIOLIN"),
                    Span("PIANO"),
                    Span("ORCHESTRA"),
                    cls="hero-marquee",
                ),

                A(
                    Span("Scroll"),
                    Span("↓"),
                    href="#background",
                    cls="scroll-button magnetic",
                ),

                Div(
                    cls="hero-orb cursor-target",
                ),

                id="top",
                cls="hero",
            ),

            *[
                chapter(
                    slug,
                    number,
                    title,
                    questions,
                )
                for slug, number, title, questions in SECTIONS
            ],

            Footer(
                H2(
                    "MY LIFE",
                    Br(),
                    "IN MUSIC",
                ),
                A(
                    "Back to top ↑",
                    href="#top",
                    cls="magnetic",
                ),
            ),
        ),
    )


serve()