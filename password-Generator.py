import re
import streamlit as st

# Password strength checker function
def password_strength(password):
    score = 0
    feedback = []
    
    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔒 Password should be at least 8 characters long.")
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("🔠 Add at least one uppercase letter.")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("🔡 Add at least one lowercase letter.")
    
    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("🔢 Include at least one digit (0-9).")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("✨ Use at least one special character (!@#$%^&*).")
    
    # Determine strength level
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"
    
    return strength, feedback, score

# Streamlit app layout
def main():
    st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")
    st.title("🔐 Password Strength Meter")
    st.markdown("### Ensure your passwords are secure and strong!")
    st.markdown("Enter a password to check its strength and receive real-time feedback on how to improve it.")
    
  
    # Password input field
    password = st.text_input("Enter your password:", type="password")
    
    # Check password strength on button click
    if st.button("Check Password Strength"):
        if password:
            strength, feedback, score = password_strength(password)
            
            # Progress bar for strength
            st.progress(score / 5)
            
            # Display password strength with dynamic coloring
            if strength == "Weak":
                st.error(f"🔴 Password strength: **{strength}**")
            elif strength == "Moderate":
                st.warning(f"🟠 Password strength: **{strength}**")
            else:
                st.success(f"🟢 Password strength: **{strength}**")
                st.balloons()
            
            # Provide feedback for improvement
            if feedback:
                st.subheader("🔧 Suggestions to improve your password:")
                for suggestion in feedback:
                    st.markdown(f"- {suggestion}")
            else:
                st.markdown("🎯 Your password is **secure and strong**! Great job!")
        else:
            st.warning("⚠️ Please enter a password.")

# Run the app
if __name__ == "__main__":
    main()