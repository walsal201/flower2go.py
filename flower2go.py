import streamlit as st

# Set page config
st.set_page_config(
    page_title="Flower2Go - Your Premier Flower Shop in Addis Ababa",
    page_icon="🌸",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
body {
    background-color: #FFD1DC;
    font-family: Arial, sans-serif;
}
.navbar {
    background-color: #f8f9fa;
    padding: 10px;
    border-radius: 5px;
}
.hero {
    background-color: #FFD1DC;
    padding: 50px 0;
    text-align: center;
    color: #333;
}
.section {
    padding: 40px 0;
}
.footer {
    background-color: #000;
    color: #fff;
    padding: 20px 0;
    text-align: center;
}
.wedding-service, .daily-delivery {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
.special-event {
    background-color: #FFDAB9;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
.about {
    background-color: #FFB6C1;
    padding: 40px 0;
    border-radius: 8px;
}
.contact {
    background-color: #FFDAB9;
    padding: 40px 0;
}
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Flower2Go Navigation")
page = st.sidebar.radio("Go to", ["Home", "Services", "About", "Contact"])

# Logo
st.sidebar.image("logo.png", width=100)

if page == "Home":
    st.markdown("""
    <div class="hero">
        <h1>Welcome to Flower2Go</h1>
        <p>Your Premier Flower Shop in Addis Ababa</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "Services":
    st.markdown("""
    <div class="section">
        <h2 class="text-center mb-4">Our Services</h2>
    </div>
    """, unsafe_allow_html=True)

    # Wedding Services
    st.markdown("""
    <div class="wedding-service">
        <h3 class="text-center mb-3">Wedding Services</h3>
        <p class="text-center">
            You've said yes to the one person you're planning on spending your life with, and now it's time to plan for that special big day. At Flower 2 Go, we offer a variety of wedding bouquets that are catered to your specific needs. Our Bridal Bouquets are custom designed for your tastes, and make a great addition at any wedding ceremony!
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Special Events
    st.markdown("""
    <div class="special-event">
        <h3>Special Events</h3>
        <p>
            Bridesmaid Bouquets Some would say that there's nothing more exciting than planning a wedding. If you've just taken your relationship to that next level, then congratulations — it's time to plan for the big day! At Flower 2 Go, we have a variety of floral arrangements that are perfect for your special day. Our Bridesmaid Bouquets are designed with your needs in mind, and make for a great addition as you walk down the aisle!
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Daily Deliveries
    st.markdown("""
    <div class="daily-delivery">
        <h3>Daily Deliveries</h3>
        <p>
            At Flower 2 Go, we're flower experts. We spend our days creating beautiful arrangements that you're sure to love and enjoy. We offer a wonderful variety of fresh cut flowers, gorgeous arrangements and specialty products. Our clients have the chance to select from a large assortment of options that are suitable for every occasion.
        </p>
        <a href="#contact" class="btn btn-primary mt-3">Order Now</a>
        <p><a href="https://www.dropbox.com/scl/fi/ae3lkv4dzuejnl481k658/Flower2go-1-.pdf1010.pdf?rlkey=1rtn5hsf649a2z8i75h8q5g1k&st=tt1qmu2t&dl=0">Download Flower2Go PDF</a></p>
    </div>
    """, unsafe_allow_html=True)

elif page == "About":
    st.markdown("""
    <div class="about">
        <div class="container">
            <h2 class="text-center mb-4">About Us</h2>
            <p class="text-center">
                Welcome to Flower2Go, your premier destination for exquisite floral arrangements. We specialize in creating beautiful bouquets and arrangements for all occasions, from weddings to daily celebrations. Our experienced florists are dedicated to bringing your floral visions to life.
            </p>
            <div class="video-container">
                <iframe src="https://www.youtube.com/embed/-g7tuPXRenk" title="Flower2Go Video" allowfullscreen style="width:100%; height:400px;"></iframe>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif page == "Contact":
    st.markdown("""
    <div class="contact">
        <div class="container">
            <h2 class="text-center mb-4">Contact Us</h2>
            <div class="contact-info text-center">
                <p><i class="fas fa-envelope"></i> Email: <a href="mailto:walsal201@gmail.com">walsal201@gmail.com</a></p>
                <p><i class="fas fa-phone"></i> Tel: <a href="tel:00251911628248">+251-911-628248</a></p>
                <p><i class="fas fa-map-marker-alt"></i> Location: Bole, Atlas Hotel<br>Addis Ababa, Ethiopia</p>
            </div>
            <div class="row">
                <div class="col-md-6">
                    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3940.5985087373434!2d38.79281!3d9.005583!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x164b85f0f9a06d85%3A0x4331551f2e0d81cb!2sAtlas%20Hotel!5e0!3m2!1sen!2set!4v1642277456789!5m2!1sen!2set" width="100%" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
                </div>
                <div class="col-md-6">
                    <h4>Get in Touch</h4>
                    <p><i class="fas fa-user"></i> Manager: Walid Ibrahim</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>&copy; 2025 Flower2Go. All rights reserved.</p>
    <div>
        <a href="#" class="mx-2">Privacy Policy</a>
        <a href="#" class="mx-2">Terms of Service</a>
        <a href="#contact" class="mx-2">Contact Us</a>
    </div>
</div>
""", unsafe_allow_html=True)
