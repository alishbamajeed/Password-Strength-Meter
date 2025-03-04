import re
import streamlit as st
import random
import string

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

# Password generator
def generate_password(length):
    characters = string.ascii_letters + string.digits + '!@#$%^&*'
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit app layout
def main():
    st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")
    st.title("🔐 Password Strength Meter")
    st.markdown("### Ensure your passwords are secure and strong!")
    st.markdown("Enter a password to check its strength or generate a strong one.")

    # History of checked passwords
    if 'password_history' not in st.session_state:
        st.session_state['password_history'] = []
    
    # Password input field
    password = st.text_input("Enter your password:", type="password")

    # Password length selection and generation
    length = st.selectbox("Select password length to generate:", [6, 8, 12])
    if st.button("Generate Password"):
        password = generate_password(length)
        st.text(f"Generated Password ({length} chars): {password}")
        st.session_state['password_history'].append(password)

    # Check password strength
    if st.button("Check Password Strength"):
        if password:
            strength, feedback, score = password_strength(password)
            st.progress(score / 5)
            
            if strength == "Weak":
                st.error(f"🔴 Password strength: **{strength}**")
            elif strength == "Moderate":
                st.warning(f"🟠 Password strength: **{strength}**")
            else:
                st.success(f"🟢 Password strength: **{strength}**")
                st.balloons()

            # Feedback
            if feedback:
                st.subheader("🔧 Suggestions to improve your password:")
                for suggestion in feedback:
                    st.markdown(f"- {suggestion}")

            # Save to history
            st.session_state['password_history'].append(password)
        else:
            st.warning("⚠️ Please enter a password or generate one.")

    # Show password history
    st.subheader("📜 Password History:")
    for pwd in st.session_state['password_history'][-5:]:  # Show last 5 passwords
        st.text(pwd)

if __name__ == "__main__":
    main()
