import streamlit as st
from PIL import Image

def app():
    st.title("About Us")

    st.header("Our Mission")
    st.write("""
    We aim to democratize access to financial insights and empower users with the tools they need to navigate the complexities of credit and lending. Our goals include:
    
    1. **Enhancing Financial Literacy**
       - Offering educational resources and tools to help users understand credit scoring and loan processes.
    
    2. **Promoting Financial Inclusion**
       - Providing fair and unbiased credit assessments to ensure everyone has access to credit opportunities.
    
    3. **Supporting Financial Planning**
       - Enabling users to make well-informed financial decisions with reliable data and predictive insights.
    
    4. **Innovating Continuously**
       - Staying at the forefront of technology by continuously improving our algorithms and models to deliver the best possible service.
    """)

    st.header("Why Choose Us?")
    st.write("""
    1. **Cutting-Edge Technology**
       - We use the latest AI and ML algorithms to deliver precise and reliable results.
    
    2. **User-Centric Approach**
       - Our tools are designed to be user-friendly and easy to understand.
    
    3. **Transparency and Trust**
       - We believe in transparent processes and aim to build trust through accuracy and integrity.
    
    4. **Comprehensive Support**
       - Our dedicated team is here to provide excellent support and guidance at every step.
    """)

    st.header("Meet the Team")
    col1, col2, col3 = st.columns(3)

    def resize_image(image_path, height=300):
        img = Image.open(image_path)
        aspect_ratio = img.width / img.height
        new_width = int(height * aspect_ratio)
        return img.resize((new_width, height))
    
    with col1:
        st.image(".\pages\Deekshit.png", caption="Deekshit", use_column_width=True)

    with col2:
        st.image(".\pages\good img.JPG", caption="Aniruddha", use_column_width=True)

    with col3:
        st.image(".\pages\sanika.png", caption="Sanika", use_column_width=True)

if __name__ == "__main__":
    app()
