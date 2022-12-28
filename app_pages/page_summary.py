import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Mildew is a fungal disease that is affecting the cherry plantations at Farmy & Foods.\n"
        f"* A powdery mildew is a fungus that attacks plants, "
        "causing a white, dusty coating on leaves, stems, also flowers.\n"
        f"* A random set of leaves was collected and examined by raw eyes. "
        "Visual criteria are used to detect powdery mildew. \n"
        f"Powdery mildew may cause leaves to turn completely yellow, die,"
        "then fall off, which may expose fruit to sunburn. \n"
        f"On some plants, powdery mildew may cause leaves to twist,"
        "buckle, or otherwise be deformed")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/Vannesha2021/MildewDetectionApp/blob/main/README.md).")

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1. The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from the one that contains powdery mildew.\n"
        f"* 2. The client is interested in predicting if a cherry tree is healthy or contains powdery mildew.")