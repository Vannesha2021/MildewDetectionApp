import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* We suspect mildew infected leaves has cloudy residue on the leaf, "
        f"typically the colour of the leaf, that can differentiate, from a "
        f" healthy leaf. \n\n"
        f"* An Image Montage, shows that typically a infected leaf has white "
        f" powder across. \n\n"
        f"Average Image, Variability Image and Difference between averages studies didn't reveal "
        f"any clear pattern to differentiate one to another."
    )