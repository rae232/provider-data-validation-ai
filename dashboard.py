import streamlit as st
import pandas as pd
import requests
import io

st.set_page_config(page_title="Provider Data Validation AI", layout="wide")

st.title("🏥 Provider Data Validation Dashboard")
st.write("Upload provider data (CSV or Excel) and run Agentic AI validation")

# File uploader (CSV + Excel)
uploaded_file = st.file_uploader(
    "Upload Provider File",
    type=["csv", "xlsx"]
)

if uploaded_file:
    file_name = uploaded_file.name

    # Read file based on extension
    try:
        if file_name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif file_name.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file)
        else:
            st.error("Unsupported file format")
            st.stop()

        st.subheader("📄 Uploaded Provider Data")
        st.dataframe(df)

    except Exception as e:
        st.error(f"Error reading file: {e}")
        st.stop()

    # Run validation
    if st.button("🚀 Run Validation"):
        with st.spinner("Running Agentic AI pipeline..."):

            # Reset file pointer before sending
            uploaded_file.seek(0)

            response = requests.post(
                "http://127.0.0.1:8000/validate",
                files={
                    "file": (
                        file_name,
                        uploaded_file,
                        "application/octet-stream"
                    )
                }
            )

        if response.status_code == 200:
            result = response.json()

            if "validated_records" in result:
                validated_df = pd.DataFrame(result["validated_records"])

                st.success("✅ Validation Completed")
                st.subheader("📊 Validated Provider Data")
                st.dataframe(validated_df)

                # Confidence score visualization
                if "confidence_score" in validated_df.columns:
                    st.subheader("📈 Confidence Score Distribution")
                    st.bar_chart(validated_df["confidence_score"])
            else:
                st.error(result.get("error", "Unknown error occurred"))
        else:
            st.error("❌ Backend error occurred")
