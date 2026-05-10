import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Mechanical Unit & Density Checker", layout="centered")

# --- Header & Identification ---
st.title("⚙️ Mechanical Unit Converter & Material Density Checker")
st.markdown(f"**Developer:** Zain Abbas | **ID:** 159")
st.divider()

# --- Sidebar Navigation ---
option = st.sidebar.selectbox("Select Functionality", ["Unit Converter", "Material Density Checker"])

# --- Functionality 1: Unit Converter ---
if option == "Unit Converter":
    st.header("📏 Mechanical Unit Converter")
    
    col1, col2 = st.columns(2)
    
    with col1:
        category = st.selectbox("Category", ["Pressure", "Power", "Force"])
        input_value = st.number_input("Enter Value", value=1.0)

    if category == "Pressure":
        # Conversion: 1 bar = 100,000 Pa = 14.5038 psi
        st.subheader("Results")
        st.write(f"**Pascals (Pa):** {input_value * 100000:,.2f}")
        st.write(f"**PSI (lb/in²):** {input_value * 14.5038:.4f}")
        st.info("Input unit: **Bar**")

    elif category == "Power":
        # Conversion: 1 hp = 745.7 Watts
        st.subheader("Results")
        st.write(f"**Watts (W):** {input_value * 745.7:,.2f}")
        st.write(f"**Kilowatts (kW):** {(input_value * 745.7)/1000:.4f}")
        st.info("Input unit: **Horsepower (hp)**")

    elif category == "Force":
        # Conversion: 1 kgf = 9.80665 N
        st.subheader("Results")
        st.write(f"**Newtons (N):** {input_value * 9.80665:.4f}")
        st.write(f"**Pounds-force (lbf):** {input_value * 2.20462:.4f}")
        st.info("Input unit: **Kilogram-force (kgf)**")

# --- Functionality 2: Material Density Checker ---
else:
    st.header("🔬 Material Density Checker")
    
    # Dictionary of Common Materials (kg/m^3)
    densities = {
        "Steel": 7850,
        "Aluminum": 2700,
        "Copper": 8960,
        "Titanium": 4506,
        "Cast Iron": 7200,
        "Water": 1000
    }
    
    selected_material = st.selectbox("Select Material", list(densities.keys()))
    volume = st.number_input("Enter Volume ($m^3$)", value=1.0, min_value=0.01)
    
    density = densities[selected_material]
    mass = density * volume
    
    st.success(f"The density of **{selected_material}** is **{density} $kg/m^3$**.")
    st.metric(label="Calculated Mass (kg)", value=f"{mass:,.2f} kg")
    
    st.info("Formula used: $Mass = Density \\times Volume$")

# --- Footer ---
st.divider()
st.caption("Final Project Submission - Zain Abbas (159)")
