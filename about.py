import streamlit as st

# Set page config
st.set_page_config(
    page_title="Flower2Go - About",
    page_icon="🌸",
    layout="wide"
)

# Inject Bootstrap CSS, FontAwesome CSS, and custom CSS
st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
.hero { background-color: #FFD1DC; padding: 100px 0; color: #333; }
.section { padding: 60px 0; }
.footer { background-color: #000; color: #fff; padding: 20px 0; }
.footer-links a { color: #fff; text-decoration: none; }
.footer-links a:hover { text-decoration: underline; }
.wedding-service, .daily-delivery { background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); }
.card { transition: transform 0.3s ease; border: none; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); padding: 20px; background-color: #fff; }
.card-title { font-size: 1.5rem; font-weight: bold; margin-bottom: 1rem; }
.card-text { font-size: 1.1rem; }
.card:hover { transform: translateY(-5px); box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15); }
.btn-primary { background-color: #007bff; border-color: #007bff; }
.btn-primary:hover { background-color: #0056b3; border-color: #0056b3; }
.wedding-image, .event-image, .delivery-image { position: relative; overflow: hidden; border-radius: 10px; margin-bottom: 20px; }
.wedding-image img, .event-image img, .delivery-image img { width: 100%; height: auto; object-fit: cover; transition: transform 0.5s ease; }
.price-table { background-color: #fff; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); padding: 20px; margin-bottom: 20px; }
@media (max-width: 768px) { body { margin-top: 76px; }
.section { padding: 40px 0; }
.wedding-service, .special-event, .daily-delivery { padding: 15px; } }
.hero h1 { font-size: 3.5rem; margin-bottom: 20px; }
.navbar-brand { display: flex; align-items: center; }
.navbar-brand img { transition: transform 0.3s ease; height: 45px; width: auto; object-fit: contain; margin-right: 15px; padding: 5px; }
.navbar-brand img:hover { transform: scale(1.1); }
.card:hover { transform: translateY(-5px); }
.contact-info { padding: 20px; background: #f8f9fa; border-radius: 10px; }
.contact-info p { margin-bottom: 15px; }
.contact-info a { color: #007bff; text-decoration: none; transition: color 0.3s ease; }
.contact-info a:hover { color: #0056b3; text-decoration: underline; }
.contact-info i { margin-right: 10px; color: #007bff; }
.map-container { border-radius: 10px; overflow: hidden; box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1); }
.wedding-service { background-color: #FFB6C1; padding: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); margin-bottom: 40px; }
.wedding-content { padding: 25px 15px; background-color: rgba(255, 255, 255, 0.9); border-radius: 8px; }
.wedding-quote { font-size: 1.1rem; line-height: 1.8; color: #555; max-width: 900px; margin: 0 auto; font-style: italic; }
.wedding-service h3 { color: #007bff; font-size: 2rem; margin-bottom: 20px; }
.additional-wedding-image { max-width: 600px; margin: 0 auto; overflow: hidden; border-radius: 10px; }
.additional-wedding-image img { width: 100%; height: auto; transform: scale(1); transition: transform 0.5s ease; object-fit: cover; }
.additional-wedding-image:hover img { transform: scale(1.02); }
.special-event { background-color: #FFDAB9; padding: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); margin: 30px 0; }
.event-content { padding: 20px; background-color: rgba(255, 255, 255, 0.9); border-radius: 8px; }
.event-content h3 { color: #007bff; font-size: 2.2rem; margin-bottom: 25px; position: relative; }
.event-content h3:after { content: ''; position: absolute; bottom: -10px; left: 0; width: 60px; height: 3px; background: #007bff; }
.event-quote { font-size: 1.1rem; line-height: 1.8; color: #555; margin-top: 20px; }
.event-image { position: relative; overflow: hidden; border-radius: 10px; }
.event-image img { width: 100%; height: auto; transform: scale(1); transition: transform 0.5s ease; }
.event-image:hover img { transform: scale(1.05); }
.daily-delivery { background-color: #FFDAB9; padding: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); margin: 30px 0; }
.delivery-content { padding: 20px 30px; background-color: rgba(255, 255, 255, 0.9); border-radius: 8px; }
.delivery-content h3 { color: #007bff; font-size: 2.2rem; margin-bottom: 25px; position: relative; }
.delivery-content h3:after { content: ''; position: absolute; bottom: -10px; left: 0; width: 60px; height: 3px; background: #007bff; }
.delivery-quote { font-size: 1.1rem; line-height: 1.8; color: #555; margin-top: 20px; }
.delivery-image { position: relative; overflow: hidden; border-radius: 10px; box-shadow: 0 6px 25px rgba(0, 0, 0, 0.1); }
.delivery-image img { width: 100%; height: auto; transform: scale(1); transition: transform 0.6s ease; }
.delivery-image:hover img { transform: scale(1.05); }
.about-us { background-color: #FFB6C1; padding: 40px 0; margin: 20px 0; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); }
.about-content { background-color: rgba(255, 255, 255, 0.9); padding: 25px; border-radius: 8px; margin: 15px 0; }
.about-us h2 { color: #333; margin-bottom: 20px; }
.about-us p { color: #444; line-height: 1.8; }
@media (max-width: 768px) { .hero h1 { font-size: 2.5rem; }
.contact-info { margin-bottom: 30px; }
.special-event { padding: 20px; }
.event-content { padding: 15px; text-align: center; }
.event-content h3:after { left: 50%; transform: translateX(-50%); }
.daily-delivery { padding: 20px; }
.delivery-content { padding: 15px; text-align: center; }
.delivery-content h3:after { left: 50%; transform: translateX(-50%); }
.delivery-image { margin-bottom: 20px; } }
.video-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; }
.video-container iframe { position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none; }
@media (max-width: 768px) { .video-container { margin-top: 20px; } }
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
                <li class="nav-item"><a class="nav-link" href="app">Home</a></li>
                <li class="nav-item"><a class="nav-link" href="services">Services</a></li>
                <li class="nav-item"><a class="nav-link" href="about">About</a></li>
                <li class="nav-item"><a class="nav-link" href="contact">Contact</a></li>
            </ul>
        </div>
    </div>
</nav>
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

# Footer
st.markdown("""
<footer class="footer">
    <div class="container">
        <div class="footer-content text-center">
            <p class="mb-3">&copy; 2025 Flower2Go. All rights reserved.</p>
            <div class="footer-links">
                <a href="app" class="mx-2">Home</a>
                <a href="services" class="mx-2">Services</a>
                <a href="about" class="mx-2">About</a>
                <a href="contact" class="mx-2">Contact</a>
            </div>
        </div>
    </div>
</footer>
""", unsafe_allow_html=True)
