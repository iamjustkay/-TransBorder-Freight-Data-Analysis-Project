import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import os

# Streamlit config
st.set_page_config(page_title="Freight Dashboard", layout="wide")
st.title("📦 Freight Transport Analysis Dashboard")
st.markdown("CRISP-DM: Multi-Year Freight Insights (2020–2024)")
st.markdown("---")

# Constants
YEARS = [2020, 2021, 2022, 2023, 2024]

month_order = {
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May',
    6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
}
transtype = {1: 'Import', 2: 'Export'}
mode_dict = {
    1: 'Vessel', 3: 'Air', 4: 'Mail (U.S. Postal Service)', 5: 'Truck',
    6: 'Rail', 7: 'Pipeline', 8: 'Other', 9: 'Foreign Trade Zones (FTZs)'
}


@st.cache_data
def load_and_prepare(year):
    try:
        file = f"{year}_TransData.csv"
        df = pd.read_csv(file, low_memory=False)
        df.columns = df.columns.str.strip().str.replace(" ", "_")

        # Label mapping
        df['Mode_Label'] = df['DISAGMOT'].map(mode_dict)
        df['Trade_Type'] = df['TRDTYPE'].map(transtype)
        df['Month_Name'] = df['MONTH'].map(month_order)
        df['MONTH_ORDER'] = df['MONTH']
        df['YEAR'] = year
        return df
    except Exception as e:
        st.error(f"Failed to load {year}: {e}")
        return pd.DataFrame()


# Create year tabs
tabs = st.tabs([str(y) for y in YEARS])

for i, year in enumerate(YEARS):
    with tabs[i]:
        st.header(f"📊 Insights for {year}")
        df = load_and_prepare(year)

        if df.empty:
            st.warning("No data available.")
            continue

        # KPIs
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Shipments", f"{df.shape[0]:,}")
        col2.metric("Total Weight (tons)", f"{df['SHIPWT'].sum():,.0f}")
        col3.metric("Total Value ($)", f"{df['VALUE'].sum():,.2f}")

        st.markdown("### 1️⃣ Freight Volume by Mode Over Time")
        vol_df = (
            df.groupby(['MONTH_ORDER', 'Month_Name', 'Mode_Label'], observed=True)['SHIPWT']
            .sum().reset_index()
            .sort_values(by='MONTH_ORDER')
        )

        plt.figure(figsize=(10, 5))
        sns.set(style="whitegrid")
        line_plot = sns.lineplot(
            data=vol_df,
            x='Month_Name',
            y='SHIPWT',
            hue='Mode_Label',
            marker="o"
        )
        plt.xticks(rotation=45)
        plt.title(f"Freight Volume by Mode Over Time - {year}")
        plt.xlabel("Month")
        plt.ylabel("Weight (tons)")
        plt.tight_layout()
        st.pyplot(plt.gcf())  # Render Seaborn figure in Streamlit
        plt.clf()  # Clear figure for next loop

        st.markdown("### 2️⃣ Freight Volume by Region and Mode (Plotly)")
        region_pivot = df.pivot_table(index='USASTATE', columns='Mode_Label', values='SHIPWT', aggfunc='sum', fill_value=0)
        fig2 = px.bar(region_pivot, title="Freight Volume by State and Mode", barmode='stack')
        st.plotly_chart(fig2, use_container_width=True)

        st.markdown("### 3️⃣ Operational Costs by Mode")
        cost_sum = df.groupby('Mode_Label')['FREIGHT_CHARGES'].sum().reset_index().sort_values(by='FREIGHT_CHARGES', ascending=False)
        fig3 = px.bar(cost_sum, x='Mode_Label', y='FREIGHT_CHARGES', color='Mode_Label', title="Total Freight Charges by Mode", text_auto='.2s')
        st.plotly_chart(fig3, use_container_width=True)

        st.markdown("### 4️⃣ Value of Goods by Mode")
        value_sum = df.groupby('Mode_Label')['VALUE'].sum().reset_index().sort_values(by='VALUE', ascending=False)
        fig4 = px.bar(value_sum, x='Mode_Label', y='VALUE', color='Mode_Label', title="Total Value of Freight by Mode", text_auto='.2s')
        st.plotly_chart(fig4, use_container_width=True)

        st.markdown("### 5️⃣ Least Used Transport Modes")
        underused = df.groupby('Mode_Label')['SHIPWT'].sum().sort_values().head(5)
        fig5 = px.bar(underused, x=underused.values, y=underused.index, orientation='h', color=underused.index,
                      title="Least Used Transport Modes by Volume", labels={"x": "Volume"})
        st.plotly_chart(fig5, use_container_width=True)

        st.markdown("### 6️⃣ Export vs Import by State")
        trade = df.pivot_table(index='USASTATE', columns='Trade_Type', values='SHIPWT', aggfunc='sum', fill_value=0)
        fig6 = px.bar(trade, title="Export vs Import Volumes by State", barmode='stack')
        st.plotly_chart(fig6, use_container_width=True)


