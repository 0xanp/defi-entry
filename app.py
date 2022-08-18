import pandas as pd
import pandas_profiling
import streamlit as st

from streamlit_pandas_profiling import st_profile_report


@st.cache(allow_output_mutation=True)
def gen_profile_report(df, *report_args, **report_kwargs):
    return df.profile_report(*report_args, **report_kwargs)

def main():
        df = pd.read_csv("./Defi_txn/BSC/router_data_with_balances")
        pr = gen_profile_report(df, explorative=True)
        st.write(df)
        with st.expander("REPORT", expanded=True):
            st_profile_report(pr)

if __name__ == "__main__":
    main()