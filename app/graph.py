# from altair import Chart, Tooltip
# from pandas import DataFrame
# from app.data import Database
#
# db = Database('bandersnatch')
#
# def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
#     # Create the Altair chart using the DataFrame
#     graph = Chart(
#         df,
#         title=f"{y} by {x} for {target}",
#     ).mark_circle(size=100).encode(
#         x=x,
#         y=y,
#         color=target,
#         tooltip=Tooltip(df.columns.to_list())
#     )
#     return graph
# from altair import Chart, Tooltip
# from pandas import DataFrame
# from app.data import Database
#
# db = Database('bandersnatch')
#
# from altair import Chart, Tooltip
# from pandas import DataFrame
# from app.data import Database
#
# db = Database('bandersnatch')
#
# from altair import Chart, Tooltip
# from pandas import DataFrame
# from app.data import Database
#
# db = Database('bandersnatch')

import altair as alt
from altair import Chart, Tooltip
from pandas import DataFrame
from app.data import Database

db = Database('bandersnatch')


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:

    # Create the Altair chart using the DataFrame
    graph = alt.Chart(
        df,
        title=f"{y} by {x} for {target}",
    ).mark_circle(size=100).encode(
        x=x,
        y=y,
        color=target,
        tooltip=Tooltip(df.columns.to_list())

    ).properties(
        width=500,
        height=300,
        background='#1E1E1E',  # Background color
    ).configure_title(
        fontSize=16,
        font='Arial',
        color='#808080',  # Title color
    ).configure_axis(
        titleColor='#808080',
        labelColor="#808080",  # Axis label color
        gridColor="#696969",
        gridOpacity=0.15,

    ).configure_view(
        stroke=None,

    ).configure_legend(
        labelColor="#808080",
        titleColor='#808080',  # Legend label color
    ).configure_mark(
        color='#FF4500',
    )

    return graph




