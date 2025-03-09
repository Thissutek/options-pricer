from fasthtml.common import *


app, rt = fast_app()


@rt("/")
def get():
    desc = Container(
        H1("Finance Made Easy"),
        H4("How does Option Pricer Work"),
        P("Loren ipsum"),
        Ol(
            Li("Enter Current Stock Price"),
            Li("Enter Options Strike Price "),
            Li("Enter the time of expiration"),
            Li("Enter the Risk Free Interest Rate"),
            Li("Enter the Volatility of the Stock")
        )
    )

    inp = Container(
            Grid(
                Label(
                    "Stock Price ($)",
                    Input(id="current-stock-price", name="current-stock-price", placeholder="Current Stock Price")
                ),
                Label(
                    "Option Price ($)",
                    Input(id="option-strike-price", name="option-strike-price", placeholder="Option Strike Price")

                ),
                Label(
                    "Time to expiration (years)",
                    Input(id="time-expiration", name="time-expiration", placeholder="Time untill expiration"),

                ),
                Label(
                    "Risk Free Interest Rate (%)",
                    Input(id="risk-free-rate", name="risk-free-rate", placeholder="Risk Free Interest Rate"),

                ),
                Label(
                    "Volatility (%)",
                    Input(id="volatility-stock", name="volatility-stock", placeholder="Volatility of Stock")),

                ),
                Button("Click Me")
            )
    
    map = Container(
        H1("Heat Map")
    )

    options = Container(
        H1("Options Price"),
        Grid(
            H3("Call Option Price"),
            H3("Put Option Price")
        )
    )
    

    return (Title("Options Pricer"), 
            Div(
                desc,
                inp,
                map,
                options
            ))


serve()
