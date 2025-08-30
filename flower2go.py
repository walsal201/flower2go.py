import streamlit as st
import os

st.set_page_config(
    page_title="Flower2Go - Your Premier Flower Shop in Addis Ababa",
    page_icon="🌸",
    layout="wide"
)

# Inject Bootstrap CSS, FontAwesome CSS, and custom CSS
st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
/* General Styles */
body {
    background-color: #FFD1DC; /* Peach-pink color */
    font-family: Arial, sans-serif;
    margin-top: 56px; /* Adjust for fixed navbar */
}

.navbar {
    background-color: #f8f9fa;
}

.hero {
    background-color: #FFD1DC; /* Match body background */
    padding: 100px 0;
    color: #333;
}

.section {
    padding: 60px 0;
}

.footer {
    background-color: #000; /* Black color */
    color: #fff;
    padding: 20px 0;
}

.footer-links a {
    color: #fff;
    text-decoration: none;
}

.footer-links a:hover {
    text-decoration: underline;
}

/* Additional Styles */
.wedding-service, .daily-delivery {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.card {
    transition: transform 0.3s ease;
    border: none;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    padding: 20px;
    background-color: #fff;
}

.card-title {
    font-size: 1.5rem;
    font-weight: bold;
    margin-bottom: 1rem;
}

.card-text {
    font-size: 1.1rem;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}

.btn-primary {
    background-color: #007bff;
    border-color: #007bff;
}

.btn-primary:hover {
    background-color: #0056b3;
    border-color: #0056b3;
}

/* Maintain existing image styles */
.wedding-image, .event-image, .delivery-image {
    position: relative;
    overflow: hidden;
    border-radius: 10px;
    margin-bottom: 20px;
}

.wedding-image img, .event-image img, .delivery-image img {
    width: 100%;
    height: auto;
    object-fit: cover;
    transition: transform 0.5s ease;
}

/* Price table styles */
.price-table {
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    padding: 20px;
    margin-bottom: 20px;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    body {
        margin-top: 76px;
    }
    
    .section {
        padding: 40px 0;
    }
    
    .wedding-service, .special-event, .daily-delivery {
        padding: 15px;
    }
}

/* Hero Section */
.hero h1 {
    font-size: 3.5rem;
    margin-bottom: 20px;
}

/* Navigation */
.navbar-brand {
    display: flex;
    align-items: center;
}

.navbar-brand img {
    transition: transform 0.3s ease;
    height: 45px;
    width: auto;
    object-fit: contain;
    margin-right: 15px;
    padding: 5px;
}

.navbar-brand img:hover {
    transform: scale(1.1);
}

/* Services Section */
.card:hover {
    transform: translateY(-5px);
}

/* Contact Section */
.contact-info {
    padding: 20px;
    background: #f8f9fa;
    border-radius: 10px;
}

.contact-info p {
    margin-bottom: 15px;
}

.contact-info a {
    color: #007bff;
    text-decoration: none;
    transition: color 0.3s ease;
}

.contact-info a:hover {
    color: #0056b3;
    text-decoration: underline;
}

.contact-info i {
    margin-right: 10px;
    color: #007bff;
}

.map-container {
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
}

/* Wedding Service Section */
.wedding-service {
    background-color: #FFB6C1; /* Light pink color */
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    margin-bottom: 40px;
}

.wedding-content {
    padding: 25px 15px;
    background-color: rgba(255, 255, 255, 0.9); /* Semi-transparent white */
    border-radius: 8px;
}

.wedding-quote {
    font-size: 1.1rem;
    line-height: 1.8;
    color: #555;
    max-width: 900px;
    margin: 0 auto;
    font-style: italic;
}

.wedding-service h3 {
    color: #007bff;
    font-size: 2rem;
    margin-bottom: 20px;
}

.additional-wedding-image {
    max-width: 600px;
    margin: 0 auto;
    overflow: hidden;
    border-radius: 10px;
}

.additional-wedding-image img {
    width: 100%;
    height: auto;
    transform: scale(1);
    transition: transform 0.5s ease;
    object-fit: cover;
}

.additional-wedding-image:hover img {
    transform: scale(1.02);
}

/* Special Events Section */
.special-event {
    background-color: #FFDAB9; /* Peach color */
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    margin: 30px 0;
}

.event-content {
    padding: 20px;
    background-color: rgba(255, 255, 255, 0.9); /* Semi-transparent white */
    border-radius: 8px;
}

.event-content h3 {
    color: #007bff;
    font-size: 2.2rem;
    margin-bottom: 25px;
    position: relative;
}

.event-content h3:after {
    content: '';
    position: absolute;
    bottom: -10px;
    left: 0;
    width: 60px;
    height: 3px;
    background: #007bff;
}

.event-quote {
    font-size: 1.1rem;
    line-height: 1.8;
    color: #555;
    margin-top: 20px;
}

.event-image {
    position: relative;
    overflow: hidden;
    border-radius: 10px;
}

.event-image img {
    width: 100%;
    height: auto;
    transform: scale(1);
    transition: transform 0.5s ease;
}

.event-image:hover img {
    transform: scale(1.05);
}

/* Daily Deliveries Section */
.daily-delivery {
    background-color: #FFDAB9; /* Peach color */
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    margin: 30px 0;
}

.delivery-content {
    padding: 20px 30px;
    background-color: rgba(255, 255, 255, 0.9); /* Semi-transparent white */
    border-radius: 8px;
}

.delivery-content h3 {
    color: #007bff;
    font-size: 2.2rem;
    margin-bottom: 25px;
    position: relative;
}

.delivery-content h3:after {
    content: '';
    position: absolute;
    bottom: -10px;
    left: 0;
    width: 60px;
    height: 3px;
    background: #007bff;
}

.delivery-quote {
    font-size: 1.1rem;
    line-height: 1.8;
    color: #555;
    margin-top: 20px;
}

.delivery-image {
    position: relative;
    overflow: hidden;
    border-radius: 10px;
    box-shadow: 0 6px 25px rgba(0, 0, 0, 0.1);
}

.delivery-image img {
    width: 100%;
    height: auto;
    transform: scale(1);
    transition: transform 0.6s ease;
}

.delivery-image:hover img {
    transform: scale(1.05);
}

/* About Us Section */
.about-us {
    background-color: #FFB6C1; /* Light pink color */
    padding: 40px 0;
    margin: 20px 0;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.about-content {
    background-color: rgba(255, 255, 255, 0.9);
    padding: 25px;
    border-radius: 8px;
    margin: 15px 0;
}

.about-us h2 {
    color: #333;
    margin-bottom: 20px;
}

.about-us p {
    color: #444;
    line-height: 1.8;
}

/* Responsive Design */
@media (max-width: 768px) {
    .hero h1 {
        font-size: 2.5rem;
    }
    
    .contact-info {
        margin-bottom: 30px;
    }
    
    .special-event {
        padding: 20px;
    }
    
    .event-content {
        padding: 15px;
        text-align: center;
    }
    
    .event-content h3:after {
        left: 50%;
        transform: translateX(-50%);
    }
    
    .daily-delivery {
        padding: 20px;
    }
    
    .delivery-content {
        padding: 15px;
        text-align: center;
    }
    
    .delivery-content h3:after {
        left: 50%;
        transform: translateX(-50%);
    }
    
    .delivery-image {
        margin-bottom: 20px;
    }
}

.video-container {
    position: relative;
    padding-bottom: 56.25%; /* 16:9 aspect ratio */
    height: 0;
    overflow: hidden;
    max-width: 100%;
}

.video-container iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border: none;
}

@media (max-width: 768px) {
    .video-container {
        margin-top: 20px;
    }
}
</style>
""", unsafe_allow_html=True)

# Navigation
st.markdown("""
<nav class="navbar navbar-expand-lg navbar-light bg-light" style="position: sticky; top: 0; z-index: 1000;">
    <div class="container">
        <a class="navbar-brand" href="#">
            🌸 Flower2Go
        </a>
        <div class="d-flex justify-content-end" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item"><a class="nav-link" href="#home">Home</a></li>
                <li class="nav-item"><a class="nav-link" href="#services">Services</a></li>
                <li class="nav-item"><a class="nav-link" href="#about">About</a></li>
                <li class="nav-item"><a class="nav-link" href="#contact">Contact</a></li>
            </ul>
        </div>
    </div>
</nav>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<header id="home" class="hero">
    <div class="container text-center">
        <h1>Welcome to Flower2Go</h1>
        <p>Your Premier Flower Shop in Addis Ababa</p>
    </div>
</header>
""", unsafe_allow_html=True)

# Services Section
st.markdown("""
<section id="services" class="py-5">
    <div class="container">
        <h2 class="text-center mb-4">Our Services</h2>
        <div class="row">
""", unsafe_allow_html=True)

# Wedding Services
st.markdown("""
            <div class="col-md-12 mb-5">
                <div class="wedding-service">
                    <div class="wedding-image">
""", unsafe_allow_html=True)
if os.path.exists("20.jpg"):
    st.image("20.jpg", caption="Luxury Wedding Table Setting with Purple Lighting", use_column_width=True)
else:
    st.write("Image: 20.jpg not found")
st.markdown("""
                    </div>
                    <div class="wedding-content mt-4">
                        <h3 class="text-center mb-3">Wedding Services</h3>
                        <p class="text-center wedding-quote">
                            You've said yes to the one person you're planning on spending your life with, and now it's time to plan for that special big day. At Flower 2 Go, we offer a variety of wedding bouquets that are catered to your specific needs. Our Bridal Bouquets are custom designed for your tastes, and make a great addition at any wedding ceremony!
                        </p>
                    </div>
                </div>
            </div>
""", unsafe_allow_html=True)

# Special Events
st.markdown("""
        <div class="col-md-12 mb-5">
            <div class="special-event">
                <div class="row align-items-center">
                    <div class="col-md-6">
                        <div class="event-content">
                            <h3>Special Events</h3>
                            <p class="event-quote">
                                Bridesmaid Bouquets Some would say that there's nothing more exciting than planning a wedding. If you've just taken your relationship to that next level, then congratulations — it's time to plan for the big day! At Flower 2 Go, we have a variety of floral arrangements that are perfect for your special day. Our Bridesmaid Bouquets are designed with your needs in mind, and make for a great addition as you walk down the aisle!
                            </p>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="event-image">
""", unsafe_allow_html=True)
if os.path.exists("Beautiful Bridesmaid.jpg"):
    st.image("Beautiful Bridesmaid.jpg", caption="Beautiful Bridesmaid", use_column_width=True)
else:
    st.write("Image: Beautiful Bridesmaid.jpg not found")
st.markdown("""
                        </div>
                    </div>
                </div>
            </div>
        </div>
""", unsafe_allow_html=True)

# Daily Deliveries
st.markdown("""
        <div class="col-md-12 mb-5">
            <div class="daily-delivery">
                <div class="row align-items-center">
                    <div class="col-md-6">
                        <div class="delivery-image">
""", unsafe_allow_html=True)
if os.path.exists("Elegant Floral Arrangement.jpg"):
    st.image("Elegant Floral Arrangement.jpg", caption="Elegant Floral Arrangement", use_column_width=True)
else:
    st.write("Image: Elegant Floral Arrangement.jpg not found")
st.markdown("""
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="delivery-content">
                            <h3>Daily Deliveries</h3>
                            <p class="delivery-quote">
                                At Flower 2 Go, we're flower experts. We spend our days creating beautiful arrangements that you're sure to love and enjoy. We offer a wonderful variety of fresh cut flowers, gorgeous arrangements and specialty products. Our clients have the chance to select from a large assortment of options that are suitable for every occasion.
                            </p>
""", unsafe_allow_html=True)
if st.button("Order Now"):
    st.write("Order functionality not implemented yet.")
st.markdown("""
                            <p><a href="https://www.dropbox.com/scl/fi/ae3lkv4dzuejnl481k658/Flower2go-1-.pdf1010.pdf?rlkey=1rtn5hsf649a2z8i75h8q5g1k&st=tt1qmu2t&dl=0">Download Flower2Go PDF</a></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-md-12 text-center">
            <div class="card mb-4 mx-auto" style="max-width: 400px; background-color: #007bff; color: white;">
                <div class="card-body">
                    <h5 class="card-title">Daily Deliveries</h5>
                    <p class="card-text">Fresh flowers delivered to your door.</p>
                </div>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# About Section
st.markdown("""
<section id="about" class="about py-5" style="background-color: #FFB6C1; padding: 40px 0; border-radius: 8px;">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-10">
                <div style="background-color: rgba(255, 255, 255, 0.9); padding: 30px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
                    <h2 class="text-center mb-4">About Us</h2>
                    <div class="row">
                        <div class="col-md-12">
                            <div class="about-content text-center">
                                <p>Welcome to Flower2Go, your premier destination for exquisite floral arrangements. We specialize in creating beautiful bouquets and arrangements for all occasions, from weddings to daily celebrations. Our experienced florists are dedicated to bringing your floral visions to life.</p>
                            </div>
                        </div>
                    </div>
                    <div class="row mt-4">
                        <div class="col-md-12">
                            <div class="video-container text-center">
                                <div class="embed-responsive embed-responsive-16by9">
                                    <iframe class="embed-responsive-item" 
                                            src="https://www.youtube.com/embed/-g7tuPXRenk" 
                                            title="Flower2Go Video"
                                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                                            allowfullscreen
                                            style="border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); width: 100%; height: 400px;">
                                    </iframe>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# Contact Section
st.markdown("""
<section id="contact" class="py-5" style="background-color: #FFDAB9;">
    <div class="container">
        <h2 class="text-center mb-4">Contact Us</h2>
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="contact-info text-center">
                    <p><i class="fas fa-envelope"></i> Email: <a href="mailto:walsal201@gmail.com">walsal201@gmail.com</a></p>
                    <p><i class="fas fa-phone"></i> Tel: <a href="tel:00251911628248">+251-911-628248</a></p>
                    <p><i class="fas fa-map-marker-alt"></i> Location: Bole, Atlas Hotel<br>Addis Ababa, Ethiopia</p>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-md-6">
                <div class="map-container">
                    <iframe 
                        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3940.5985087373434!2d38.79281!3d9.005583!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x164b85f0f9a06d85%3A0x4331551f2e0d81cb!2sAtlas%20Hotel!5e0!3m2!1sen!2set!4v1642277456789!5m2!1sen!2set"
                        width="100%" 
                        height="300" 
                        style="border:0;" 
                        allowfullscreen="" 
                        loading="lazy">
                    </iframe>
                </div>
            </div>
            <div class="col-md-6">
                <div class="contact-info">
                    <h4>Get in Touch</h4>
                    <p><i class="fas fa-user"></i> Manager: Walid Ibrahim</p>
                </div>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<footer class="footer">
    <div class="container">
        <div class="footer-content text-center">
            <p class="mb-3">&copy; 2025 Flower2Go. All rights reserved.</p>
            <div class="footer-links">
                <a href="#" class="mx-2">Privacy Policy</a>
                <a href="#" class="mx-2">Terms of Service</a>
                <a href="#contact" class="mx-2">Contact Us</a>
            </div>
        </div>
    </div>
</footer>
""", unsafe_allow_html=True)
# Set page config
