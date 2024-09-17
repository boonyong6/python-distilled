def make_table(data, **params):
    # Get configuration parameters from params (a dict)
    fgcolor = params.pop("fgcolor", "black")
    bgcolor = params.pop("bgcolor", "white")
    width = params.pop("width", None)

    print("fgcolor:", fgcolor)
    print("bgcolor:", bgcolor)
    print("width:", width)

    # No more options
    if params:
        raise TypeError(f"Unsupported configuration options {list(params)}")


items = []
make_table(
    items,
    fgcolor="black",
    bgcolor="white",
    border=1,
    borderstyle="grooved",
    cellpadding=10,
    width=400,
)
