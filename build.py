#!/usr/bin/env python3
"""Generate projects.html and projects/<slug>.html from the data below.

Run: python3 build.py
"""
from html import escape
from pathlib import Path

M = "https://static.wixstatic.com/media/"
ROOT = Path(__file__).parent

LOGO = M + "da5604_84d522a122744a3a984f44c5a98bbd48~mv2.png"

# Each project: slug, card name, heading, thumbnail, paragraphs, galleries.
# A gallery is (caption, [(image id, alt), ...]).
PROJECTS = [
    dict(
        slug="employer-household-dynamics",
        name="Employer-Household Dynamic",
        title="Employer-Household Dynamics",
        thumb="da5604_626214a7b3cf4063bc892427fe842dde~mv2.png",
        text=[
            "This project aims to chart the network of links between an employee's residence and their workplace.",
            "The maps provide visual representations of connections spanning a radius of 60 miles or less between a household (employee) and a workplace (employer) within Census tracts in California. One map showcases the connection pattern categorized by income levels, while another is organized by industry segmentation.",
        ],
        galleries=[(None, [
            ("da5604_35fc4dd49dbb449a85bf40009fbc7bd2~mv2.png", "Employer-household connections by income level"),
            ("da5604_d147df333f584dde84d4c2ad211fd048~mv2.png", "Employer-household connections by industry"),
        ])],
    ),
    dict(
        slug="urban-job-distribution",
        name="Urban Job Distribution",
        title="Urban Job Distribution",
        thumb="da5604_7d27b36ed8f94a6daabacb2c2925d42e~mv2.png",
        text=[
            "These maps visually represent the concentration and dispersion of super-sectors and industry sectors within significant cities, employing a multivariate dot-density approach. Each dot's color corresponds to a specific industry or super-sector. The map provides a unified depiction of employment patterns at the census block level, highlighting the city’s dynamics, distribution, and clustering of jobs.",
        ],
        galleries=[
            (None, [
                ("da5604_6b85bc7749ea49f5aef866a332b8fdc6~mv2.png", "San Francisco"),
                ("da5604_a6a4618a502b457b80f68813e3f0b78c~mv2.png", "Los Angeles"),
                ("da5604_c1a1a216e83f443cbb5c372cf9cb9477~mv2.png", "Chicago"),
            ]),
            (None, [
                ("da5604_b748abc4bd8f4e5cb1b59653ead17ae8~mv2.png", "Los Angeles"),
                ("da5604_dd4e7f2c595942599051fbabfbda5a7b~mv2.png", "Bay Area"),
                ("da5604_babd847deb4c457890fba8271c3c3736~mv2.png", "San Francisco by industry"),
            ]),
        ],
    ),
    dict(
        slug="los-angeles-building",
        name="Los Angeles Building",
        title="Los Angeles Building Industry Density",
        thumb="da5604_1a77776534bd405e8c8e6bdc0977243b~mv2.jpg",
        text=[
            "“Los Angeles Building Industry Density: Mapping 3D Structures by Census Block-Level Industry Density.”",
            "In this project, Los Angeles buildings are depicted in 3D, with their coloration determined by the predominant industry in the respective census block where the building is situated. Industry density is determined by aggregating the number of jobs within the dominant industry in each census block.",
        ],
        galleries=[("Coloring the building by type of dominant industry.", [
            ("da5604_1a77776534bd405e8c8e6bdc0977243b~mv2.jpg", "Santa Monica"),
            ("da5604_94c71e7d1bf2470da703049e288f48e8~mv2.jpg", "LA Downtown"),
            ("da5604_a1d62b0d4f7844a5a02ac874375e795f~mv2.jpg", "LA Airport"),
        ])],
    ),
    dict(
        slug="city-dynamics",
        name="City Dynamic",
        title="City Dynamics",
        thumb="da5604_e1a19ff8b38e4aceb74ea37d11f36d77~mv2.jpg",
        text=[
            "“City Dynamics: Unraveling the Complexity of Urban Systems”",
            "Cities are intricate and ever-evolving systems characterized by dynamism. Urban patterns are in a constant state of flux, influenced by the lifestyle, living arrangements, and work preferences of the population. These factors, along with the interplay of economics and geography, as well as the rapid advancements in technology, have a profound impact on the movement and interactions of individuals within cities. This dynamic interplay results in the emergence of novel patterns of change.",
            "The Dynamic City Project specifically delves into the employment aspects related to the economic dimension of cities. Leveraging Employment Statistics (LODES), it provides insights into the geographical distribution of employment based on both workplace and residence locations. Variables such as earnings, industry, gender, race, and educational attainment between 2009 and 2017 in the state of California are tracked. The project aims to showcase the dominant subcategories of these variables at the city and zip code levels, shedding light on the intricate dynamics of urban employment patterns.",
        ],
        galleries=[("Depicting the dominant job by sex at city level.", [
            ("da5604_6cf104912fb5412fa13b1360cb234a7e~mv2.jpg", "City Dynamic by Race"),
            ("da5604_be283710ee494979b6ab4b3533bcce3b~mv2.jpg", "City Dynamic by Industry"),
            ("da5604_e1a19ff8b38e4aceb74ea37d11f36d77~mv2.jpg", "Growth of Industry type"),
        ])],
    ),
    dict(
        slug="socioeconomic",
        name="Socioeconomic",
        title="Socioeconomic Regional Clustering",
        thumb="da5604_324a01b059724baf8d50e778a7541847~mv2.jpg",
        text=[
            "The Socioeconomic Project explores the interdependence of government, economy, and prosperity by grouping countries within the same region or political sphere based on their state type, economic characteristics, and prosperity indices.",
            "Each index is assigned a grade derived from the scores of its constituent pillars. The clustering of countries is accomplished by assessing the similarities between the pillars of each index.",
        ],
        galleries=[("Clustering based on the political pillars.", [
            ("da5604_324a01b059724baf8d50e778a7541847~mv2.jpg", "Regional Clustering"),
            ("da5604_0994feba51514d6f8eeb18905d7519f5~mv2.jpg", "Regional Clustering"),
            ("da5604_c51ae0917a45440f843f9e4d64265dcb~mv2.jpg", "Regional Clustering"),
        ])],
    ),
    dict(
        slug="trade",
        name="Trade",
        title="Examining Trade Deficit",
        thumb="da5604_db1f65e97b5048fc978b165a1cff590b~mv2.jpg",
        text=[
            "United States Trade is a dynamic process. The Trade Project illustrates the historical import, export and trade deficit for each country. The project was divided into two parts—commodity and advanced technological products. One of the core objectives of this project is to illustrate the historical trade deficiency and its correlation with money supply and tax cuts. The project is still in progress.",
        ],
        galleries=[("Illustrating the import, export and trade deficit by a country.", [
            ("da5604_b2f15028954644a1a7c6d5c10ff740a5~mv2.jpg", "USA Trade by a country"),
            ("da5604_db1f65e97b5048fc978b165a1cff590b~mv2.jpg", "USA Trade by a country"),
            ("da5604_3ec9b7f42397406d882eb4fa892ee1d8~mv2.jpg", "USA Trade by State"),
        ])],
    ),
    dict(
        slug="labor-supply",
        name="Labor Supply",
        title="Labor Supply",
        thumb="da5604_dc51bd1824b94d7eadb5e918ecb7571a~mv2.png",
        text=[
            "This project displays the historical trend of non-farm labor supply for the sectors of each industry from 1990 to 2017. The project looks at the level and growth rate of labor supply through these twenty-seven years. One section of the project ranks the top and bottom twenty sectors based on the annual growth rate.",
            "One of the project's objectives is to illustrate the rise and fall of the labor supply for each sector. The project also attempts to shed light on the demand side of labor for each sector throughout this period.",
        ],
        galleries=[("Growth of labor supply at each sector.", [
            ("da5604_1aeb561806cf4ef091c4340a5988b59d~mv2.jpg", "Growth of Labor Supply"),
            ("da5604_7bae10abb2d34ee7ae2bcca5dacc2243~mv2.jpg", "Labor supply by sector"),
        ])],
    ),
    dict(
        slug="political-economy",
        name="Political Economy",
        title="Political Economy",
        thumb="da5604_1136277a01034794814ee6883ea3e26b~mv2.png",
        text=[
            "The culture of a nation—the shared values and belief system—impact and form the political system of that nation. The political system or the system of government likewise shapes a nation's economic and legal system. These systems are not independent. They interact and affect each other. The extent to which a nation's political system emerges from democratic or authoritarian values will impact the type of economic system.",
            "The political economy project illustrates these interactions at the regional and political levels. This project is interactive.",
        ],
        galleries=[("World based on the political structure.", [
            ("da5604_94f16734a5934f1caf84b8abf7e715a4~mv2.png", "Political Structure"),
            ("da5604_1136277a01034794814ee6883ea3e26b~mv2.png", "Type of Economy"),
            ("da5604_d3d9365bff16457089f43fed2d04f7f6~mv2.png", "Income level regional level"),
        ])],
    ),
    dict(
        slug="orange-county-property-tax",
        name="Orange County Property Tax",
        title="Orange County Property Tax",
        thumb="da5604_34118eb86adf4ed4b4612ddf6693752a~mv2.png",
        text=[
            "This project displays the historical trend of the trading of parcels within a city between 1979 and 2018 to help forecast tax revenue for each city and the entire county.",
            "The project exhibits the one percent (1%) tax rate set by Proposition 13 and tax rates for voter-approved debt for each TRA. Taxable properties are grouped into the Tax Rate Area (TRA). TRAs include taxing agencies such as cities, school districts, and special districts.",
            "The interactive map provides information about the type of parcels, the net value of properties, total tax revenue, and revenue distribution for special districts and schools for each TRA. This format provides comprehensive information about tax and revenue distribution for special districts of different cities.",
        ],
        galleries=[(None, [
            ("da5604_b9c4d8a8ce224e158c526ff7ee5af723~mv2.png", "Orange County Tax Rate Area"),
            ("da5604_adcdac08fa55497dbb1b4d61e4a6bc54~mv2.png", "Property Tax Distribution"),
            ("da5604_83f2e18b65f548e8ba4d73343a6458e8~mv2.png", "Historical Parcel Change"),
        ])],
    ),
    dict(
        slug="city-human-capital",
        name="City Human Capital",
        title="Human Capital Index",
        thumb="da5604_ac2018072e6240bd8089df0e07da7502~mv2.png",
        text=[
            "Human capital as a collection of resources is one of the important factors to represent the total capacity of people as a form of wealth. Building high human capital in the next generation is required to meet the demand of the future workforce and enhance the standard of living.",
            "City Human Capital Index (CHCI) measures the current CHCI from national to zip code levels. The correlation of the CHCI and the income level of the households are represented at the county and zip code level. The project depicts the state's ranking according to CHCI and represents the CHCI score as a heatmap for the whole country.",
        ],
        galleries=[(None, [
            ("da5604_acab186f6a8549bba3a8b552fd359f2a~mv2.jpg", "CHCI County Level"),
            ("da5604_b66db179ce2c4403bec65d6330f6f2f8~mv2.jpg", "CHCI Coastal Level"),
            ("da5604_f869d19bd3b640c4939ee610ecb95e8f~mv2.jpg", "Heat Map"),
        ])],
        link=("View Interactive Map »", "https://dotdimensions.shinyapps.io/CityHumanCapital/"),
    ),
]


def img_url(media_id, width):
    ext = media_id.rsplit(".", 1)[-1]
    return f"{M}{media_id}/v1/fit/w_{width},h_{width},q_85/img.{ext}"


def head(title, css):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} | Dot Dimensions</title>
<link rel="stylesheet" href="{css}">
</head>
<body>
"""


def header(prefix, current):
    items = [("About", "about.html"), ("Projects", "projects.html"),
             ("Home", "index.html"), ("Contact", "contact.html")]
    links = "\n".join(
        f'    <a href="{prefix}{href}"' + (' aria-current="page"' if label == current else "") + f">{label}</a>"
        for label, href in items
    )
    return f"""<header class="site-header">
  <a class="logo" href="{prefix}index.html"><img src="{LOGO}" alt="Dot Dimensions"></a>
  <nav class="nav" aria-label="Main">
{links}
  </nav>
</header>
"""


def project_page(i, p):
    prev_p = PROJECTS[i - 1] if i > 0 else None
    next_p = PROJECTS[i + 1] if i < len(PROJECTS) - 1 else None
    out = [head(p["title"], "../styles.css"), header("../", "Projects")]
    out.append(f'<div class="page-title"><h1>{escape(p["title"])}</h1></div>\n<main class="wrap project">\n')
    out.append('  <div class="copy">\n')
    out += [f"    <p>{escape(t)}</p>\n" for t in p["text"]]
    if "link" in p:
        out.append(f'    <p><a class="cta" href="{p["link"][1]}" target="_blank" rel="noopener">{escape(p["link"][0])}</a></p>\n')
    out.append("  </div>\n")
    for caption, slides in p["galleries"]:
        out.append('  <div class="gallery">\n')
        for media_id, alt in slides:
            out.append(
                f'    <figure><a href="{M}{media_id}" target="_blank" rel="noopener">'
                f'<img src="{img_url(media_id, 1400)}" alt="{escape(alt)}"></a>'
                f"<figcaption>{escape(alt)}</figcaption></figure>\n"
            )
        out.append("  </div>\n")
        if caption:
            out.append(f'  <p class="gallery-note">{escape(caption)}</p>\n')
    nav = []
    if prev_p:
        nav.append(f'<a href="{prev_p["slug"]}.html">&larr; Previous</a>')
    else:
        nav.append("<span></span>")
    nav.append('<a href="../projects.html">All Projects</a>')
    nav.append(f'<a href="{next_p["slug"]}.html">Next &rarr;</a>' if next_p else "<span></span>")
    out.append('  <nav class="pager" aria-label="Projects">' + "".join(nav) + "</nav>\n")
    out.append("</main>\n</body>\n</html>\n")
    return "".join(out)


def index_page():
    cards = "\n".join(
        f'    <a class="card" href="projects/{p["slug"]}.html">'
        f'<div class="thumb"><img src="{M}{p["thumb"]}/v1/fill/w_520,h_260,al_c,q_80/thumb.{p["thumb"].rsplit(".", 1)[-1]}" alt=""></div>'
        f'<span>{escape(p["name"])}</span></a>'
        for p in PROJECTS
    )
    return (head("Projects", "styles.css") + header("", "Projects")
            + '<div class="page-title"><h1>Projects</h1></div>\n<main class="wrap">\n  <div class="grid">\n'
            + cards + "\n  </div>\n</main>\n</body>\n</html>\n")


(ROOT / "projects").mkdir(exist_ok=True)
(ROOT / "projects.html").write_text(index_page())
for i, p in enumerate(PROJECTS):
    (ROOT / "projects" / f'{p["slug"]}.html').write_text(project_page(i, p))
print(f"wrote projects.html and {len(PROJECTS)} project pages")
