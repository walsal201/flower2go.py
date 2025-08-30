import streamlit as st

st.set_page_config(
    page_title="Flower2Go - Your Premier Flower Shop in Addis Ababa",
    page_icon="🌸",
    layout="wide"
)

st.markdown("""
    <style>
        body, .stApp {
            background-color: #FFD1DC;
            font-family: Arial, sans-serif;
        }
        .navbar {
            border-radius: 8px;
            padding: 0.5rem 1rem;
            margin-bottom: 2rem;
            background: #f8f9fa;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 100;
        }
        .navbar img {
            height: 48px;
            border-radius: 7px;
            margin-right: 20px;
        }
        .navbar-links a {
            font-size: 1.1rem;
            color: #333;
            margin: 0 18px;
            text-decoration: none;
        }
        .navbar-links a:hover {
            color: #007bff;
            text-decoration: underline;
        }
        .hero-section {
            background-color: #FFD1DC;
            padding: 64px 20px 40px 20px;
            border-radius: 12px;
            box-shadow: 0 4px 23px rgba(0,0,0,0.07);
            text-align: center;
        }
        h1 {
            font-size: 3rem;
            color: #007bff;
            margin-bottom: 0.5rem;
        }
        h2 {
            margin-top: 2rem;
            color: #007bff;
            text-align: center;
        }
        .service-card, .about-card, .delivery-card {
            background: #fff;
            border-radius: 12px;
            box-shadow: 0 3px 16px rgba(0,0,0,.14);
            margin: 24px 0;
            padding: 1.2rem 1.6rem;
        }
        .service-img, .about-img {
            max-width: 100%;
            border-radius: 10px;
            margin-bottom: 1.2rem;
        }
        .footer {
            text-align: center;
            margin-top: 2.5rem;
            color: white;
            background: #35363A;
            border-radius: 8px;
            padding: 1.5rem;
        }
        .footer a {
            color: #fff;
            margin: 0 8px;
        }
        .contact-info i {
            margin-right: 7px;
        }
        .contact-btn {
            background: #007bff;
            color: #fff;
            padding: 0.7rem 1.2rem;
            border-radius: 6px;
            border: none;
            cursor: pointer;
            margin-top: 1rem;
            font-size: 1rem;
        }
        .contact-btn:hover {
            background: #0056b3;
        }
        .pdf-link {
            color: #007bff;
            font-weight: bold;
            text-decoration: underline;
        }
        .pdf-link:hover {
            color: #0056b3;
        }
    </style>
""", unsafe_allow_html=True)

# Navbar
st.markdown("""
<div class="navbar">
    <div style="display:flex; align-items:center">
        <img src="https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=crop&w=80&q=80" alt="Flower2Go Logo">
        <span style="font-size: 1.6rem; color: #007bff; font-weight: bold;">Flower2Go</span>
    </div>
    <div class="navbar-links">
        <a href="#home">Home</a>
        <a href="#services">Services</a>
        <a href="#about-us">About</a>
        <a href="#contact">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown('<div class="hero-section" id="home">', unsafe_allow_html=True)
st.write("## Welcome to Flower2Go")
st.write("**Your Premier Flower Shop in Addis Ababa**")
st.markdown('</div>', unsafe_allow_html=True)

# Services Section
st.markdown('<hr id="services">', unsafe_allow_html=True)
st.markdown('<h2>Our Services</h2>', unsafe_allow_html=True)

with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown('<div class="service-card">', unsafe_allow_html=True)
        st.image(
            "https://images.unsplash.com/photo-1509042239860-f550ce710b93?auto=format&fit=crop&w=600&q=80",
            use_container_width=True,
            caption="Beautiful Arrangement of Roses"
        )
        st.markdown("""
        **Wedding Bouquets & Arrangements**  
        _"Custom wedding bouquets featuring elegant roses and premium flowers, tailored to your special day by Flower2Go's master florists."_
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="service-card">', unsafe_allow_html=True)
        st.image(
            "https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=600&q=80",
            use_container_width=True,
            caption="Classic Red Rose Display"
        )
        st.markdown("""
        **Red Rose Display**  
        _"Classic red roses, handpicked for the perfect romantic gesture or grand celebration."_  
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="service-card">', unsafe_allow_html=True)
        st.image(
            "https://images.unsplash.com/photo-1519864600265-abb23847ef2c?auto=format&fit=crop&w=600&q=80",
            use_container_width=True,
            caption="Mixed Fresh Flowers for Events"
        )
        st.markdown("""
        **Special Events**  
        _"Make every event memorable with our vibrant fresh flower and rose arrangements designed for celebrations, birthdays, and more."_
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="service-card">', unsafe_allow_html=True)
        st.image(
            "https://images.unsplash.com/photo-1465101022946-4377e57745c3?auto=format&fit=crop&w=600&q=80",
            use_container_width=True,
            caption="Bouquet of Pink Roses – Daily Delivery"
        )
        st.markdown("""
        **Daily Deliveries**  
        _"Enjoy daily deliveries of delightful roses and fresh floral bouquets, perfect for brightening any day or occasion."_  
        [Order Now](#contact)
        """)
        st.markdown('<a href="https://www.dropbox.com/scl/fi/ae3lkv4dzuejnl481k658/Flower2go-1-.pdf1010.pdf?rlkey=1rtn5hsf649a2z8i75h8q5g1k&st=tt1qmu2t&dl=0" target="_blank" class="pdf-link">Download Flower2Go PDF</a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with col5:
        st.markdown('<div class="service-card">', unsafe_allow_html=True)
        st.image(
            "https://images.unsplash.com/photo-1468327768560-75b778cbb551?auto=format&fit=crop&w=600&q=80",
            use_container_width=True,
            caption="Elegant White Rose Centerpieces"
        )
        st.markdown("""
        **Elegant Centerpieces**
        _"Grace your venue with tall, elegant white rose centerpieces, perfect for special dinners and luxury events."_
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# About Section
st.markdown('<hr id="about-us">', unsafe_allow_html=True)
st.markdown('<h2>About Us</h2>', unsafe_allow_html=True)
st.markdown('<div class="about-card">', unsafe_allow_html=True)
st.write("""
Welcome to Flower2Go, your premier destination for exquisite floral arrangements.
We specialize in creating stunning rose and flower bouquets for all occasions, expertly crafted by experienced florists.
""")
st.video("https://www.youtube.com/embed/-g7tuPXRenk")
st.markdown('</div>', unsafe_allow_html=True)

# Contact Section
st.markdown('<hr id="contact">', unsafe_allow_html=True)
st.markdown('<h2>Contact Us</h2>', unsafe_allow_html=True)
col4, col5 = st.columns([2, 1])
with col4:
    st.markdown("""
    <div class="contact-info">
    <p>📧 <b>Email:</b> <a href="mailto:walsal201@gmail.com">walsal201@gmail.com</a></p>
    <p>📞 <b>Tel:</b> <a href="tel:+251911628248">+251-911-628248</a></p>
    <p>📍 <b>Location:</b> Bole, Atlas Hotel, Addis Ababa, Ethiopia</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <h4>Get in Touch</h4>
    <p>👤 <b>Manager:</b> Walid Ibrahim</p>
    """, unsafe_allow_html=True)
with col5:
    st.markdown("""
    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3940.5985087373434!2d38.79281!3d9.005583!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x164b85f0f9a06d85%3A0x4331551f2e0d81cb!2sAtlas%20Hotel!5e0!3m2!1sen!2set!4v1642277456789!5m2!1sen!2set"
            width="100%" height="230" style="border:0; border-radius: 10px;" allowfullscreen="" loading="lazy"></iframe>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>&copy; 2025 Flower2Go. All rights reserved.</p>
    <div>
        <a href="#">Privacy Policy</a> |
        <a href="#">Terms of Service</a> |
        <a href="#contact">Contact Us</a>
    </div>
</div>
""", unsafe_allow_html=True)
