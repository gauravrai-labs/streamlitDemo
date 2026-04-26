# Streamlit Zero to Hero Notes

This document teaches Streamlit from absolute beginner level to production-ready app development. Streamlit is a Python framework for building interactive web apps for data apps, dashboards, and ML tools using only Python, and Streamlit apps are launched with `streamlit run` rather than `python app.py`.[cite:173][cite:171][cite:174]

## What Streamlit is

Streamlit is a Python framework that turns Python scripts into interactive web apps without requiring HTML, CSS, or JavaScript for the basic workflow.[cite:173] The official getting started guide highlights app layouts, widgets, charts, maps, caching, and themes as core capabilities.[cite:173]

## How Streamlit works

A Streamlit app runs as a Python script that is executed from top to bottom, and the script reruns whenever a user interacts with a widget.[cite:171] This rerun-based model is the key mental model for understanding why widget values, session state, caching, and callbacks matter in real apps.[cite:171][cite:177]

## Installation and setup

The official installation flow recommends creating a Python virtual environment with `venv`, activating it, installing Streamlit with `pip`, and then running a sample app.[cite:182] A virtual environment keeps Streamlit and other dependencies isolated from other Python projects, which reduces conflicts and is the right default for real projects.[cite:170][cite:182]

### Prerequisites

- Install Python 3 on your machine and ensure `python` and `pip` work in the terminal.[cite:182]
- Confirm the installation with:

```bash
python --version
pip --version
```

### Create a project folder

```bash
mkdir my_streamlit_app
cd my_streamlit_app
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the environment

#### Windows Command Prompt

```bash
.venv\Scripts\activate
```

#### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

#### macOS or Linux

```bash
source .venv/bin/activate
```

Once activated, the environment name appears at the beginning of the terminal prompt.[cite:182]

### Install Streamlit

```bash
pip install streamlit
```

### Verify installation

```bash
streamlit --version
```

## Create and run the first app

Create a file named `app.py`:

```python
import streamlit as st

st.title("Hello Streamlit")
st.write("My first Streamlit app")
```

Run the app with:

```bash
streamlit run app.py
```

The official docs state that Streamlit apps are run with `streamlit run`, and the app opens locally in the browser when launched this way.[cite:171][cite:174] Running the script with plain `python app.py` can lead to warnings such as missing `ScriptRunContext`, because Streamlit expects to manage the app lifecycle itself.[cite:171][cite:174]

## Core mental model

To become productive in Streamlit, understand these rules first:

- The Python file reruns from top to bottom on widget interaction.[cite:171]
- Widget values are returned directly by widget functions such as `st.text_input` and `st.slider`.[cite:177]
- `st.session_state` is used to preserve values across reruns in a user session.[cite:177]
- Expensive work should be cached so the app feels fast and avoids repeated computation, which the official guides describe as part of the Streamlit development flow.[cite:173]

## Basic output methods

These methods display information in the app.

### `st.write(*args, unsafe_allow_html=False)`

`st.write` is the most flexible display function and can render text, markdown-like content, dataframes, figures, and many Python objects, which is why beginners often start with it.[cite:173] Use it when you want a single display method that adapts to many object types.

Typical usage:

```python
st.write("Hello")
st.write({"name": "Aman", "role": "Student"})
st.write(df)
```

Arguments:

- `*args`: One or more objects to display.
- `unsafe_allow_html`: Allows raw HTML in certain contexts, but it should be used carefully for maintainability and safety.

### `st.title(body, anchor=None, help=None)`

Use `st.title` for the main page heading.[cite:173] It should normally appear once near the top of the page so users immediately understand the app purpose.

Arguments:

- `body`: The title text.
- `anchor`: Optional heading anchor behavior.
- `help`: Optional tooltip/help text in supported contexts.

### `st.header(body, anchor=None, help=None)` and `st.subheader(body, anchor=None, help=None)`

These methods create section headings and subsection headings for page structure.[cite:173] Use them to break long apps into logical blocks.

### `st.text(body)`

Displays plain preformatted text.[cite:173] Use it when you do not want markdown formatting.

### `st.markdown(body, unsafe_allow_html=False, help=None)`

Displays Markdown content and is useful for rich formatting, inline code, links, lists, and emphasis.[cite:177] This is often the best choice for explanation-heavy apps or documentation-style pages.

Arguments:

- `body`: Markdown string.
- `unsafe_allow_html`: Whether to allow raw HTML.
- `help`: Optional contextual help in supported versions.

### `st.code(body, language="python")`

Displays formatted code blocks.[cite:173] This is useful for tutorials, code viewers, and debugging panels.

### `st.caption(body)`

Displays small secondary text, commonly used for notes, tips, and metadata.[cite:173]

### `st.latex(body)`

Renders LaTeX expressions for math-heavy apps.[cite:173]

## Data display methods

### `st.dataframe(data, width=None, height=None, use_container_width=None, ...)`

Use `st.dataframe` to show interactive tabular data with scrolling and table interaction.[cite:173] This is ideal for analytics apps and internal tools.

Arguments:

- `data`: DataFrame or tabular object.
- `width`, `height`: Display sizing.
- `use_container_width`: Expands the table to fit the parent container.

### `st.table(data)`

Displays a static table, which is better for small summary tables than for large datasets.[cite:173]

### `st.json(body, expanded=True)`

Displays JSON in an inspectable format, which is helpful for APIs, config viewers, and debugging output.[cite:173]

### `st.metric(label, value, delta=None, delta_color="normal", help=None)`

Displays KPI-style metrics such as sales, growth, or active users.[cite:173] This is useful for dashboards where one or two numbers must stand out.

Arguments:

- `label`: Metric label.
- `value`: Main value shown.
- `delta`: Change indicator.
- `delta_color`: How Streamlit colors the delta.
- `help`: Tooltip text.

## Media methods

### `st.image(image, caption=None, width=None, use_container_width=None, clamp=False, channels="RGB", output_format="auto")`

Displays local images, URLs, PIL images, or arrays.[cite:173] Use this for dashboards, CV apps, and educational apps.

Important arguments:

- `image`: Image source.
- `caption`: Caption text.
- `width`: Explicit width.
- `use_container_width`: Responsive display.
- `channels`: Color channel interpretation.
- `output_format`: Output behavior.

### `st.audio(data, format="audio/wav", start_time=0)` and `st.video(data, format="video/mp4", start_time=0)`

Use these for multimedia apps, demos, and annotation workflows.[cite:173]

## Input widget methods

Widgets are the heart of interactivity in Streamlit.

### `st.button(label, key=None, help=None, on_click=None, args=None, kwargs=None, disabled=False, use_container_width=False)`

A button returns `True` for the run in which the user clicks it.[cite:173] Use it for explicit actions such as running a model, submitting a filter, or clearing outputs.

Arguments:

- `label`: Button text.
- `key`: Unique widget key.
- `help`: Tooltip.
- `on_click`: Callback function to run on click.
- `args`: Positional arguments for the callback.
- `kwargs`: Keyword arguments for the callback.
- `disabled`: Whether the button is disabled.
- `use_container_width`: Make the button stretch to the container width.

### `st.checkbox(label, value=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)`

Use a checkbox for boolean settings such as toggles, filters, and enable/disable controls.[cite:173]

### `st.radio(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, horizontal=False)`

Use `st.radio` when the user must pick exactly one option from a small set.[cite:173]

Important arguments:

- `label`: Widget label.
- `options`: List or tuple of choices.
- `index`: Default selected option index.
- `format_func`: Optional function to customize how options display.
- `horizontal`: Shows options in a row when supported.

### `st.selectbox(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible")`

Use a selectbox for single selection when the list is longer or when you want a compact UI.[cite:173]

### `st.multiselect(label, options, default=None, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, max_selections=None, placeholder=None, disabled=False, label_visibility="visible")`

Use a multiselect when users may choose multiple categories, tags, or filters.[cite:173]

### `st.slider(label, min_value=None, max_value=None, value=None, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")`

Use sliders for numeric ranges, thresholds, and continuous-style user input.[cite:173]

Important arguments:

- `min_value`, `max_value`: Range bounds.
- `value`: Current or default value.
- `step`: Increment size.
- `format`: Display formatting.

### `st.number_input(label, min_value=None, max_value=None, value="min", step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible")`

Use `st.number_input` when precise numeric entry matters more than dragging a slider.[cite:179]

### `st.text_input(...)`

`st.text_input` displays a single-line text input widget and supports defaults, placeholders, validation-related limits, callbacks, icons, width control, and URL query binding.[cite:177]

Official function signature:[cite:177]

```python
st.text_input(
    label,
    value="",
    max_chars=None,
    key=None,
    type="default",
    help=None,
    autocomplete=None,
    on_change=None,
    args=None,
    kwargs=None,
    *,
    placeholder=None,
    disabled=False,
    label_visibility="visible",
    icon=None,
    width="stretch",
    bind=None,
)
```

Detailed argument explanation:[cite:177]

- `label`: Short description shown to the user. It should not be empty for accessibility reasons.[cite:177]
- `value`: Initial value. If `None`, the widget initializes empty and returns `None` until the user enters something.[cite:177]
- `max_chars`: Maximum allowed character count.[cite:177]
- `key`: Unique identifier. It stabilizes widget identity across reruns and makes the value accessible in `st.session_state[key]`.[cite:177]
- `type`: Either `"default"` or `"password"`.[cite:177]
- `help`: Tooltip shown next to the label when the label is visible.[cite:177]
- `autocomplete`: Value passed to the HTML input autocomplete property.[cite:177]
- `on_change`: Callback function executed when the input changes.[cite:177]
- `args`: Positional arguments sent to the callback.[cite:177]
- `kwargs`: Keyword arguments sent to the callback.[cite:177]
- `placeholder`: Hint text shown when empty.[cite:177]
- `disabled`: Disables the input when `True`.[cite:177]
- `label_visibility`: One of `"visible"`, `"hidden"`, or `"collapsed"`.[cite:177]
- `icon`: Optional emoji, Material Symbol, or `"spinner"` icon shown inside the field.[cite:177]
- `width`: `"stretch"` or a fixed pixel width.[cite:177]
- `bind`: Can sync the widget with a URL query parameter when set to `"query-params"`, and this requires `key` to be set.[cite:177]

Return value:[cite:177]

- Returns the current string value, or `None` if no value is present and the widget was initialized accordingly.

Example:

```python
name = st.text_input(
    "Enter your name",
    placeholder="Type here...",
    key="name_input",
    max_chars=50,
)
if name:
    st.write(f"Hello, {name}")
```

### `st.text_area(label, value="", height=None, max_chars=None, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible")`

Use `st.text_area` for multiline input such as notes, prompts, comments, and descriptions.[cite:173]

### `st.date_input(...)` and `st.time_input(...)`

Use these methods for scheduling, filtering date ranges, reports, and booking-style apps.[cite:173]

### `st.file_uploader(label, type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")`

Use this widget when the app needs CSV, Excel, image, PDF, or other user-uploaded files.[cite:173] Production apps often combine this with validation, size checks, and clear error messages.

### `st.camera_input(label, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")`

Captures an image from the user device camera in supported environments.[cite:173]

## Selection and action design tips

Choose widgets based on intent:

- Use `st.button` for actions.
- Use `st.checkbox` for booleans.
- Use `st.radio` for one-of-few choices.
- Use `st.selectbox` for one-of-many choices.
- Use `st.multiselect` for multiple choices.
- Use `st.slider` for quick range control.
- Use `st.number_input` for precise numeric entry.
- Use `st.text_input` and `st.text_area` for typed input.

This widget choice discipline makes apps easier to use and more production-ready because the UI matches the task naturally.[cite:173][cite:177]

## Layout methods

A production app needs clean layout structure.

### `st.sidebar`

`st.sidebar` lets you place widgets and content in the sidebar rather than the main area, which is a common pattern for filters and navigation.[cite:173]

Example:

```python
choice = st.sidebar.selectbox("Choose chart", ["Sales", "Profit"])
```

### `st.columns(spec, gap="small")`

Creates columns for side-by-side layout.[cite:177] Use this for KPI rows, form splits, and compact controls.

### `st.container()`

Creates a container that helps group related content and control ordering.[cite:173]

### `st.expander(label, expanded=False)`

Creates collapsible sections, useful for advanced filters, logs, FAQs, and debug panels.[cite:173]

### `st.tabs(tab_names)`

Creates tabbed interfaces for dashboards and analysis views.[cite:173]

### `st.form(key, clear_on_submit=False, enter_to_submit=True, border=True)` and `st.form_submit_button(...)`

Forms batch user inputs so the app does not react to every widget change immediately.[cite:173] This is extremely useful for search forms, configuration forms, and production workflows where many fields should be submitted together.

Arguments:

- `key`: Unique form key.
- `clear_on_submit`: Clears fields after submit when `True`.
- `enter_to_submit`: Allows Enter key submission when supported.
- `border`: Visual border behavior when supported.

`st.form_submit_button` is the action button inside the form that triggers submission.[cite:173]

## Status and feedback methods

Good production apps always communicate app state.

### `st.success(body)`, `st.error(body)`, `st.warning(body)`, `st.info(body)`

Use these to show clear status feedback after actions or validations.[cite:173] They improve usability and make failures easier to understand.

### `st.exception(exception)`

Displays exception details in a readable way, which is useful during development and controlled debug modes.[cite:173]

### `st.progress(value, text=None)`

Displays a progress bar for long-running jobs.[cite:173]

### `st.spinner(text="In progress...")`

Use inside a `with` block while running slow work.[cite:173]

Example:

```python
with st.spinner("Loading model..."):
    model = load_model()
```

### `st.toast(body, icon=None)` and `st.balloons()` or `st.snow()`

These add transient or celebratory feedback, but they should be used sparingly in production apps so the interface stays professional.[cite:173]

## Chart methods

### `st.line_chart(data)`, `st.bar_chart(data)`, `st.area_chart(data)`

These are quick built-in charts for fast analytics apps.[cite:173] They are great for prototypes and internal tools.

### `st.pyplot(fig=None, clear_figure=None, use_container_width=True)`

Use this for Matplotlib figures.[cite:173]

### `st.plotly_chart(figure_or_data, use_container_width=True, theme="streamlit", key=None, on_select="ignore", selection_mode=None, config=None)`

Use this for interactive Plotly charts.[cite:173] This is often the best choice for production dashboards because it supports hover, zoom, and rich interactions.

### `st.map(data)`

Displays map-based visualizations for geographic data.[cite:173]

## State management

### `st.session_state`

`st.session_state` stores data across reruns for a single user session, and widget keys are connected to session state values.[cite:177] This is essential for production apps because reruns would otherwise make the app feel stateless.

Example:

```python
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increment"):
    st.session_state.count += 1

st.write("Count:", st.session_state.count)
```

Best uses:

- Remember filter choices.
- Store selected records.
- Track wizard steps.
- Preserve login-like app state within a session.
- Coordinate multiple widgets and callbacks.[cite:177]

## Callbacks

Widgets such as `st.text_input`, `st.button`, and others can accept `on_change` or `on_click` callbacks with `args` and `kwargs`.[cite:177] Callbacks are useful when you want to update session state or trigger logic at a specific event boundary instead of mixing everything in the main flow.

Example:

```python
import streamlit as st

if "message" not in st.session_state:
    st.session_state.message = ""

def update_message(prefix):
    st.session_state.message = f"{prefix} {st.session_state.name}"

st.text_input("Name", key="name", on_change=update_message, args=("Hello",))
st.write(st.session_state.message)
```

## Caching

The official getting started material includes caching as a core feature because many apps fetch data, call APIs, or load models repeatedly.[cite:173] In production apps, caching is one of the easiest ways to improve speed and reduce resource usage.

### `@st.cache_data`

Use `@st.cache_data` for pure data-returning functions such as CSV loading, SQL queries, and API fetches where identical inputs should reuse previous results.[cite:173]

Example:

```python
@st.cache_data
def load_data(path):
    return pd.read_csv(path)
```

### `@st.cache_resource`

Use `@st.cache_resource` for long-lived heavy resources such as ML models, DB connections, tokenizers, and clients that should be initialized once and reused.[cite:173][cite:183]

Example:

```python
@st.cache_resource
def get_model():
    return load_big_model()
```

Cache design rules:

- Cache pure repeated computations.
- Do not hide user-specific state inside global cached data.
- Use session state for per-user transient values and caching for reusable shared computation.[cite:173][cite:183]

## Query parameters and deep linking

The `bind="query-params"` option in widgets such as `st.text_input` can sync widget values into the URL query string, which is useful for shareable app states and deep links.[cite:177] This is powerful for production dashboards because users can refresh or share the same filtered view.[cite:177]

## Multipage apps

Streamlit supports multipage workflows, and state plus caching patterns are commonly used to share behavior across pages.[cite:183] Production apps often use multipage structure when a single file becomes too large or when the app has clearly separate sections such as dashboard, upload, admin, and monitoring views.[cite:183]

Recommended structure:

```text
my_app/
├── app.py
├── pages/
│   ├── 1_Dashboard.py
│   ├── 2_Upload.py
│   └── 3_Settings.py
├── utils/
│   ├── data.py
│   └── charts.py
├── requirements.txt
└── .streamlit/
    └── config.toml
```

## Configuration and project files

A production app should not be only one script. It should have structure.

Useful project files:

- `requirements.txt`: Dependency list for deployment.
- `.streamlit/config.toml`: Streamlit app configuration such as theme and server behavior.
- `README.md`: Setup, run, screenshots, and deployment notes.
- `utils/`: Business logic, helpers, validation, and chart code.
- `pages/`: Separate screens for larger apps.

## Example production project structure

```text
sales_analytics_app/
├── app.py
├── pages/
│   ├── 1_Overview.py
│   ├── 2_Customer_Analysis.py
│   ├── 3_Forecasting.py
│   └── 4_Admin.py
├── components/
│   ├── filters.py
│   └── metrics.py
├── services/
│   ├── database.py
│   ├── auth.py
│   └── forecasting.py
├── utils/
│   ├── cleaning.py
│   ├── charts.py
│   └── validators.py
├── data/
├── .streamlit/
│   └── config.toml
├── requirements.txt
└── README.md
```

## Error handling best practices

Production apps need graceful handling of bad inputs, missing files, slow APIs, and model failures.

Use these patterns:

- Validate uploaded files before reading them.
- Wrap risky work in `try/except` and show `st.error` with actionable messages.[cite:173]
- Use `st.spinner` for slow tasks so users know the app is working.[cite:173]
- Use `st.warning` for incomplete filters or unsupported conditions.[cite:173]
- Log real exceptions separately if you deploy a serious app.

Example:

```python
uploaded = st.file_uploader("Upload CSV", type=["csv"])
if uploaded:
    try:
        df = pd.read_csv(uploaded)
        st.success("File loaded successfully")
        st.dataframe(df.head())
    except Exception as e:
        st.error(f"Failed to read file: {e}")
```

## Performance tips

Production-level Streamlit apps must feel responsive.

- Cache data loading and model initialization.[cite:173]
- Avoid re-reading files on every rerun.[cite:173]
- Move heavy business logic into functions.
- Use forms when many widgets should trigger one action instead of many reruns.[cite:173]
- Avoid unnecessary plotting work when no inputs changed.
- Keep app layout clean and avoid rendering huge tables by default.

## Design tips for production quality

A production app is not only about working code. It also needs clarity.

- Give the app a clear title and concise page description.
- Group filters in the sidebar.[cite:173]
- Put KPIs at the top, details below.
- Use tabs or expanders for advanced settings.[cite:173]
- Show friendly empty states when no data is available.
- Use consistent naming, labels, and units.
- Make error messages actionable.
- Avoid cluttering the main page with too many widgets.

## Security and deployment basics

Before deployment, remove hardcoded secrets from source code and use environment variables or platform secret management.[cite:173] Keep dependency versions pinned in `requirements.txt` and test the app in a clean virtual environment before shipping.[cite:182]

Basic deployment checklist:

- `requirements.txt` is complete.
- The app runs with `streamlit run app.py` in a fresh environment.[cite:171][cite:182]
- Secrets are not hardcoded.
- File paths are portable.
- Heavy resources are cached appropriately.[cite:173]
- Errors are user-friendly.
- The app is modular.

## Common beginner mistakes

- Running the app with `python app.py` instead of `streamlit run app.py`.[cite:171][cite:174]
- Forgetting that the script reruns from top to bottom on interaction.[cite:171]
- Not using `key` for widgets that need stable identity.[cite:177]
- Recomputing expensive work every rerun instead of caching it.[cite:173]
- Mixing UI code, business logic, and data access in one giant file.
- Storing everything in global variables instead of `st.session_state` when user-session persistence is needed.[cite:177]

## Learning path from zero to hero

### Stage 1: Basics

Learn these first:

- Installation and virtual environment.[cite:182]
- `st.title`, `st.write`, `st.markdown`.[cite:173]
- `st.button`, `st.text_input`, `st.selectbox`, `st.slider`.[cite:177][cite:173]
- `st.dataframe` and simple charts.[cite:173]

Practice project ideas:

- Personal profile app.
- Unit converter.
- Basic calculator.
- CSV viewer.

### Stage 2: Intermediate apps

Learn next:

- Sidebar filters.[cite:173]
- Columns, tabs, and expanders.[cite:173]
- Forms and submission flow.[cite:173]
- Session state and callbacks.[cite:177]
- `@st.cache_data` and `@st.cache_resource`.[cite:173]

Practice project ideas:

- Sales dashboard.
- Expense tracker.
- Student performance dashboard.
- Movie recommendation prototype.

### Stage 3: Production-ready apps

Master these:

- Modular project structure.
- File uploads and validation.[cite:173]
- Plotly dashboards.[cite:173]
- Multipage app design.[cite:183]
- Query-parameter binding and deep linking where useful.[cite:177]
- Deployment workflow and dependency management.[cite:182]

Practice project ideas:

- Business KPI dashboard.
- PDF or CSV analytics tool.
- AI document Q&A app.
- Forecasting or anomaly detection app.

## Full example: small production-minded app

```python
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Sales Dashboard", layout="wide")

@st.cache_data
def load_data(file):
    return pd.read_csv(file)

st.title("Sales Dashboard")
st.caption("Upload a CSV and explore performance metrics")

uploaded = st.sidebar.file_uploader("Upload sales CSV", type=["csv"])
region = st.sidebar.selectbox("Region", ["All", "North", "South", "East", "West"])

if uploaded is None:
    st.info("Upload a CSV file to get started.")
    st.stop()

try:
    df = load_data(uploaded)
except Exception as e:
    st.error(f"Unable to load file: {e}")
    st.stop()

if region != "All" and "region" in df.columns:
    df = df[df["region"] == region]

col1, col2 = st.columns(2)
with col1:
    st.metric("Rows", len(df))
with col2:
    if "sales" in df.columns:
        st.metric("Total Sales", f"{df['sales'].sum():,.2f}")

st.dataframe(df, use_container_width=True)

if "sales" in df.columns:
    st.bar_chart(df["sales"])
```

This app uses page config, sidebar inputs, file upload, caching, error handling, metrics, conditional filtering, a dataframe, and a chart, which together represent the foundation of many real business apps.[cite:173][cite:177]

## Final advice for the student

To become strong in Streamlit, do not try to memorize every method first. Learn the rerun model, widget-state relationship, session state, caching, layout, and error handling, then build many small apps and gradually refactor them into cleaner modules.[cite:171][cite:173][cite:177]

The fastest path to production-level quality is to repeatedly build apps that upload data, validate it, transform it, visualize it, and present clear actions to the user.[cite:173] When the student can structure multipage apps, manage session state intentionally, cache expensive work, and design clean workflows, the student is ready to build serious Streamlit products independently.[cite:177][cite:183]
