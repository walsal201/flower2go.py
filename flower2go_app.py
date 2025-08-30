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
            "https://images.unsplash.com/photo-1519864600265-abb23847ef2c?auto=format&fit=crop&w=600&q=80",
            use_container_width=True,
            caption="Mixed Fresh Flowers for Events"
        )
        st.markdown("""
        **Special Events**  
        _"Make every event memorable with our vibrant fresh flower and rose arrangements designed for celebrations, birthdays, and more."_
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
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
    with col4:
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
    with col5:
        st.markdown('<div class="service-card">', unsafe_allow_html=True)
        st.image(
            "https://images.unsplash.com/photo-1424746219973-8fe3bd07d8e3?auto=format&fit=crop&w=600&q=80",
            use_container_width=True,
            caption="Colorful Spring Flower Basket"
        )
        st.markdown("""
        **Spring Flower Baskets**  
        _"Welcome spring year-round with baskets full of roses, daisies, tulips, and seasonal blooms."_  
        """)
        st.markdown('</div>', unsafe_allow_html=True)
