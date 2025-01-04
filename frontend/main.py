import httpx
import polars as pl
import streamlit as st

API_URL = "http://localhost:8000"


def get_model_runs():
    """Get model runs."""
    resp = httpx.get(f"{API_URL}/modelruns")
    resp_json = resp.json()

    show_json = st.toggle("Show as JSON", value=False, key="modelruns")
    if show_json:
        st.json(resp_json)
    else:
        df = pl.DataFrame(resp_json)
        st.dataframe(df, on_select="rerun", selection_mode="single-row")


def get_final_runs():
    """Get final runs."""
    resp = httpx.get(f"{API_URL}/finalruns")
    resp_json = resp.json()

    show_json = st.toggle("Show as JSON", value=False, key="finalruns")
    if show_json:
        st.json(resp_json)
    else:
        df = pl.DataFrame(resp_json)
        st.dataframe(df)


def main():
    """Main function."""
    st.title("Model Run Approval")

    st.subheader("Model Runs")
    get_model_runs()

    st.subheader("Final Runs")
    get_final_runs()


if __name__ == "__main__":
    main()
