HIDE_ST_STYLE = """
<style>
[data-testid=stSidebar] {
    background-color: #dfe8e8;
}
div[data-testid="stToolbar"] {
    visibility: hidden;
    height: 0%;
    position: fixed;
    z-index: 100;
}
div[data-testid="stDecoration"] {
    visibility: hidden;
    height: 0%;
    position: fixed;
    z-index: 100;
}
#MainMenu {
    visibility: hidden;
    height: 0%;
}
header {
    visibility: hidden;
    height: 0%;
}
footer {
    visibility: hidden;
    height: 0%;
}
.appview-container .main .block-container {
    padding-top: 1rem;
    padding-right: 3rem;
    padding-left: 3rem;
    padding-bottom: 1rem;
}
.reportview-container {
    padding-top: 0rem;
    padding-right: 3rem;
    padding-left: 3rem;
    padding-bottom: 0rem;
}
header[data-testid="stHeader"] {
    z-index: -1;
}
</style>
"""
