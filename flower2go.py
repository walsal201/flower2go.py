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
    
    .wedding-service, .
