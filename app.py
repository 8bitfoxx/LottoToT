import streamlit as st
import pandas as pd
import time
import random


def validate_numeric_input(value, field_name):
    """
    Validate that the input is a valid numeric value.
    Returns the numeric value if valid, None if invalid.
    """
    if value == "":
        return None
    try:
        return float(value)
    except ValueError:
        st.error(f"Please enter a valid number for {field_name}")
        return None


def show_loading_animation(category_name):
    """Show a playful loading animation for calculations"""
    loading_messages = [
        f"🧮 Crunching {category_name} numbers...",
        f"⚡ Processing {category_name} data...", 
        f"🎯 Calculating {category_name} results...",
        f"🔢 Working on {category_name} math...",
        f"💫 Almost done with {category_name}...",
        f"🚀 Computing {category_name} magic...",
        f"🎲 Rolling the {category_name} dice...",
        f"⚙️ Fine-tuning {category_name} calculations..."
    ]
    
    message = random.choice(loading_messages)
    placeholder = st.empty()
    
    # Show loading message with spinner and progress
    with placeholder:
        with st.spinner(message):
            # Add a brief progress simulation
            progress_bar = st.progress(0)
            for i in range(100):
                progress_bar.progress(i + 1)
                time.sleep(0.006)  # Total animation time: 0.6 seconds
            progress_bar.empty()
    
    placeholder.empty()


def calculate_shift_differences(shift1, shift2, shift3, category_name=None):
    """
    Calculate the shift differences: 
    - First: Shift 2 - Shift 1
    - Second: Shift 3 - Shift 1 - (Shift 2 - Shift 1)
    Returns tuple of (shift3_result, shift2_result) or (None, None) if any input is invalid
    """
    if shift1 is None or shift2 is None or shift3 is None:
        return None, None

    # Show loading animation if category name is provided
    if category_name:
        show_loading_animation(category_name)

    # Calculate shift 2 - shift 1
    shift2_result = shift2 - shift1

    # Calculate shift 3 - shift 1 - (shift 2 - shift 1)
    shift3_result = shift3 - shift1 - shift2_result

    return shift3_result, shift2_result


def main():
    st.title("Shift Subtraction Calculator")
    st.write(
        "Enter values for three sets of shifts. For each set, we calculate: Shift 2 - Shift 1, then Shift 3 - Shift 1 - (Shift 2 result)."
    )

    # Initialize session state for storing values if not already present
    if 'calculations' not in st.session_state:
        st.session_state.calculations = {}

    # Physical Sales
    st.subheader("📊 Physical Sales")

    # Input fields for Physical Sales in columns for better mobile layout
    col1_1, col1_2, col1_3 = st.columns(3)
    with col1_1:
        set1_shift1_input = st.text_input("Shift 1",
                                          key="set1_shift1",
                                          placeholder="Enter number")
    with col1_2:
        set1_shift2_input = st.text_input("Shift 2",
                                          key="set1_shift2",
                                          placeholder="Enter number")
    with col1_3:
        set1_shift3_input = st.text_input("Shift 3",
                                          key="set1_shift3",
                                          placeholder="Enter number")

    # Validate inputs for Physical Sales
    set1_shift1 = validate_numeric_input(set1_shift1_input,
                                         "Physical Sales Shift 1")
    set1_shift2 = validate_numeric_input(set1_shift2_input,
                                         "Physical Sales Shift 2")
    set1_shift3 = validate_numeric_input(set1_shift3_input,
                                         "Physical Sales Shift 3")

    # Calculate differences for Physical Sales
    set1_shift3_result, set1_shift2_result = calculate_shift_differences(
        set1_shift1, set1_shift2, set1_shift3, "Physical Sales")

    # Final Results - Prominent Display
    if set1_shift3_result is not None and set1_shift2_result is not None:
        st.success("**Physical Sales Results:**")
        col_r1, col_r2, col_r3 = st.columns(3)
        with col_r1:
            st.metric("Shift 1", set1_shift1)
        with col_r2:
            st.metric("Shift 2", set1_shift2_result)
        with col_r3:
            st.metric("Shift 3", set1_shift3_result)
    else:
        st.info("Enter all Physical Sales values to see results")

    with st.expander("View Physical Sales Calculations"):
        if set1_shift3_result is not None and set1_shift2_result is not None:
            st.write(
                f"Shift 2 - Shift 1 = {set1_shift2} - {set1_shift1} = **{set1_shift2_result}**"
            )
            st.write(
                f"Shift 3 - Shift 1 - ({set1_shift2_result}) = {set1_shift3} - {set1_shift1} - {set1_shift2_result} = **{set1_shift3_result}**"
            )
        else:
            st.write("Please enter all values to see calculations")

    st.markdown("---")

    # Physical Cashes
    st.subheader("💰 Physical Cashes")

    # Input fields for Physical Cashes in columns for better mobile layout
    col2_1, col2_2, col2_3 = st.columns(3)
    with col2_1:
        set2_shift1_input = st.text_input("Shift 1",
                                          key="set2_shift1",
                                          placeholder="Enter number")
    with col2_2:
        set2_shift2_input = st.text_input("Shift 2",
                                          key="set2_shift2",
                                          placeholder="Enter number")
    with col2_3:
        set2_shift3_input = st.text_input("Shift 3",
                                          key="set2_shift3",
                                          placeholder="Enter number")

    # Validate inputs for Physical Cashes
    set2_shift1 = validate_numeric_input(set2_shift1_input,
                                         "Physical Cashes Shift 1")
    set2_shift2 = validate_numeric_input(set2_shift2_input,
                                         "Physical Cashes Shift 2")
    set2_shift3 = validate_numeric_input(set2_shift3_input,
                                         "Physical Cashes Shift 3")

    # Calculate differences for Physical Cashes
    set2_shift3_result, set2_shift2_result = calculate_shift_differences(
        set2_shift1, set2_shift2, set2_shift3, "Physical Cashes")

    # Final Results - Prominent Display
    if set2_shift3_result is not None and set2_shift2_result is not None:
        st.success("**Physical Cashes Results:**")
        col_r1, col_r2, col_r3 = st.columns(3)
        with col_r1:
            st.metric("Shift 1", set2_shift1)
        with col_r2:
            st.metric("Shift 2", set2_shift2_result)
        with col_r3:
            st.metric("Shift 3", set2_shift3_result)
    else:
        st.info("Enter all Physical Cashes values to see results")

    with st.expander("View Physical Cashes Calculations"):
        if set2_shift3_result is not None and set2_shift2_result is not None:
            st.write(
                f"Shift 2 - Shift 1 = {set2_shift2} - {set2_shift1} = **{set2_shift2_result}**"
            )
            st.write(
                f"Shift 3 - Shift 1 - ({set2_shift2_result}) = {set2_shift3} - {set2_shift1} - {set2_shift2_result} = **{set2_shift3_result}**"
            )
        else:
            st.write("Please enter all values to see calculations")

    st.markdown("---")

    # Scratch Cashes
    st.subheader("🎫 Scratch Cashes")

    # Input fields for Scratch Cashes in columns for better mobile layout
    col3_1, col3_2, col3_3 = st.columns(3)
    with col3_1:
        set3_shift1_input = st.text_input("Shift 1",
                                          key="set3_shift1",
                                          placeholder="Enter number")
    with col3_2:
        set3_shift2_input = st.text_input("Shift 2",
                                          key="set3_shift2",
                                          placeholder="Enter number")
    with col3_3:
        set3_shift3_input = st.text_input("Shift 3",
                                          key="set3_shift3",
                                          placeholder="Enter number")

    # Validate inputs for Scratch Cashes
    set3_shift1 = validate_numeric_input(set3_shift1_input,
                                         "Scratch Cashes Shift 1")
    set3_shift2 = validate_numeric_input(set3_shift2_input,
                                         "Scratch Cashes Shift 2")
    set3_shift3 = validate_numeric_input(set3_shift3_input,
                                         "Scratch Cashes Shift 3")

    # Calculate differences for Scratch Cashes
    set3_shift3_result, set3_shift2_result = calculate_shift_differences(
        set3_shift1, set3_shift2, set3_shift3, "Scratch Cashes")

    # Final Results - Prominent Display
    if set3_shift3_result is not None and set3_shift2_result is not None:
        st.success("**Scratch Cashes Results:**")
        col_r1, col_r2, col_r3 = st.columns(3)
        with col_r1:
            st.metric("Shift 1", set3_shift1)
        with col_r2:
            st.metric("Shift 2", set3_shift2_result)
        with col_r3:
            st.metric("Shift 3", set3_shift3_result)
    else:
        st.info("Enter all Scratch Cashes values to see results")

    with st.expander("View Scratch Cashes Calculations"):
        if set3_shift3_result is not None and set3_shift2_result is not None:
            st.write(
                f"Shift 2 - Shift 1 = {set3_shift2} - {set3_shift1} = **{set3_shift2_result}**"
            )
            st.write(
                f"Shift 3 - Shift 1 - ({set3_shift2_result}) = {set3_shift3} - {set3_shift1} - {set3_shift2_result} = **{set3_shift3_result}**"
            )
        else:
            st.write("Please enter all values to see calculations")

    # Summary section
    st.markdown("---")
    st.subheader("📋 Summary of All Final Values")

    # Create summary in a more mobile-friendly format
    summary_data = []

    if set1_shift3_result is not None and set1_shift2_result is not None:
        summary_data.append({
            "Category": "Physical Sales",
            "Shift 1": set1_shift1,
            "Shift 2": set1_shift2_result,
            "Shift 3": set1_shift3_result
        })

    if set2_shift3_result is not None and set2_shift2_result is not None:
        summary_data.append({
            "Category": "Physical Cashes",
            "Shift 1": set2_shift1,
            "Shift 2": set2_shift2_result,
            "Shift 3": set2_shift3_result
        })

    if set3_shift3_result is not None and set3_shift2_result is not None:
        summary_data.append({
            "Category": "Scratch Cashes",
            "Shift 1": set3_shift1,
            "Shift 2": set3_shift2_result,
            "Shift 3": set3_shift3_result
        })

    if summary_data:
        df = pd.DataFrame(summary_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.info("Enter values in any category above to see the summary table.")

    # Clear all button
    st.markdown("---")
    if st.button("Clear All Values", type="secondary"):
        # Clear all input fields by rerunning the app
        keys_to_delete = []
        for key in st.session_state.keys():
            if isinstance(key, str) and key.startswith(
                ('set1_', 'set2_', 'set3_')):
                keys_to_delete.append(key)

        for key in keys_to_delete:
            del st.session_state[key]

        st.rerun()

    # Instructions
    st.markdown("---")
    st.subheader("Instructions")
    st.write("""
    1. **Enter Values**: Input numeric values for each shift in all three sets
    2. **Real-time Calculations**: Results update automatically as you type
    3. **Supported Formats**: Integers, decimals, and negative numbers are all supported
    4. **Error Handling**: Invalid inputs will show error messages
    5. **Clear Data**: Use the "Clear All Values" button to reset all fields
    
    **Example**: If Set 1 has Shift 1 = 1, Shift 2 = 2, Shift 3 = 3:
    - Shift 2 - Shift 1 = 2 - 1 = 1
    - Shift 3 - Shift 1 - (1) = 3 - 1 - 1 = 1
    """)


if __name__ == "__main__":
    main()
